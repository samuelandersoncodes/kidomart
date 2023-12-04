from django.shortcuts import render, redirect
from .forms import RegistrationForm, UserForm, UserProfileForm
from .models import Account, UserProfile
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404
from carts.views import _cart_id
from carts.models import Cart, CartItem
from orders.models import Order
import requests


def register(request):
    """
    Handles user registration
    It validates the registration form, creates a new user account,
    and saves it to the database if the form is valid.
    an email is the sent to the user for account activation
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            tel = form.cleaned_data['tel']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )
            user.tel = tel
            user.save()

            current_site = get_current_site(request)
            mail_subject = 'Please activate your Kido account'
            message = render_to_string('accounts/account_verification_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            return redirect('/accounts/login/?command=verification&email='+email)
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


def login(request):
    """
    This function handles user login based on provided email and password.
    It then authenticates the user using the provided email and password
    And assigns respective user cart
    It also takes care of the product variations in adding cart item 
    """
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        username = email.split("@")[0]
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            try:
                cart = Cart.objects.get(cart_id=_cart_id(request))
                cart_item_exists = CartItem.objects.filter(cart=cart).exists()
                if cart_item_exists:
                    cart_item = CartItem.objects.filter(cart=cart)
                    product_variation = []
                    for item in cart_item:
                        variation = item.variations.all()
                        product_variation.append(list(variation))
                    cart_item = CartItem.objects.filter(user=user)
                    old_variation_list = []
                    id = []
                    for item in cart_item:
                        existing_variation = item.variations.all()
                        old_variation_list.append(list(existing_variation))
                        id.append(item.id)
                    for pv in product_variation:
                        if pv in old_variation_list.index(pv):
                            cart_item_id = id[index]
                            item = CartItem.objects.get(id=cart_item_id)
                            item.quantity += 1
                            item.user = user
                            item.save()
                        else:
                            cart_item = CartItem.objects.filter(cart=cart)
                            for item in cart_item:
                                item.user = user
                                item.save()
            except:
                pass
            auth.login(request, user)
            messages.success(request, f'You are logged in as {username}')
            url = request.META.get('HTTP_REFERER')
            try:
                query = requests.utils.urlparse(url).query
                params = dict(x.split('=') for x in query.split('&'))
                if 'next' in params:
                    nextPage = params['next']
                    return redirect(nextPage)
            except:
                return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')


@login_required(login_url='login')
def logout(request):
    # logout view
    auth.logout(request)
    messages.success(request, 'You just logged out!')
    return redirect('login')


def activate(request, uidb64, token):
    """
     This function activates user account based on UID and activation token.
     This function attempts to activate a user account
     using the provided UID and activation token.
     It decodes the UID, retrieves the corresponding user from the database,
     and checks if the token is valid. If successful, it sets the user as active,
     saves the changes, and redirects to the login page with a success message.
     If unsuccessful, it redirects to the registration page with an error message.
     """
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Your Kido account is activated!')
        return redirect('login')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('register')


@login_required(login_url='login')
def dashboard(request):
    """
    This function retrieves and displays the orders made by the logged-in user
    in descending order of creation date. It also calculates and provides the
    count of the user's orders.
    """
    orders = Order.objects.order_by(
        '-created_at').filter(user_id=request.user.id, is_ordered=True)
    orders_count = orders.count()
    context = {
        'orders_count': orders_count,
    }
    return render(request, 'accounts/dashboard.html', context)


def forgotPassword(request):
    """
    This function handles the initiation of a password reset for a user account.
    It retrieves the user email which was submitted through the form.
    Checks if an account with the provided email exists,
    If the account exists, it generates a password reset email.
    Sends the email with a unique user ID and token to the user,
    Sets a success message and redirects the user to the login page.
    If the account does not exist, it sets an error message
    and redirects the user back to the 'forgotPassword' page.
    """
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)
            current_site = get_current_site(request)
            mail_subject = 'Please reset your password'
            message = render_to_string('accounts/reset_password_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            messages.success(
                request, 'Password reset email has been sent to your email address.')
            return redirect('login')
        else:
            messages.error(request, 'This account does not exist')
            return redirect('forgotPassword')
    return render(request, 'accounts/forgotPassword.html')


def reset_password_validate(request, uidb64, token):
    """
    This function validates the user and token when resetting password.
    It decodes the base64-encoded user ID and retrieves the user.
    If the user exists and the token is valid,
    It stores the user ID in the session for later password reset confirmation.
    Shows a success message.
    And then redirects the user to the resetPassword page.
    If the user does not exist or the token is invalid,
    It shows an error message.
    Then redirects the user to the forgotPassword page.
    """
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Please reset your password')
        return redirect('resetPassword')
    else:
        messages.error(
            request, 'This link is expired, please resubmit your email')
        return redirect('forgotPassword')


def resetPassword(request):
    """
    This function checks if the both created
    and confirmed passwords are the same,
    if they are, user is allowed to reset their password.
    If not, an error message is shown and use ris redirected
    to the reset password page.
    """
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password reset successful!')
            return redirect('login')
        else:
            messages.error(request, 'Password does not match')
            return redirect('resetPassword')
    else:
        return render(request, 'accounts/resetPassword.html')


def my_orders(request):
    """
    This function retrieves a list of orders made by the currently logged-in user,
    filters them to include only those that have been ordered, and then orders them
    by their creation date in descending order. The resulting list of orders is then
    passed to the my orders template
    """
    orders = Order.objects.filter(
        user=request.user, is_ordered=True).order_by('-created_at')
    context = {
        'orders': orders,
    }
    return render(request, 'accounts/my_orders.html', context)


@login_required(login_url='login')
def edit_profile(request):
    """
    This function handles the editing of a user's profile information.
    It retrieves the user's profile using the logged-in user's information.
    If the request method is POST, it processes the form submissions,
    Updates the user's information and redirects to the edit profile page
    with a success message. If the request method is GET,
    it renders the edit profile form with the current user information.
    """
    userprofile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(
            request.POST, request.FILES, instance=userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(
                request, 'Your profile has been successfully updated')
            return redirect('edit_profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=userprofile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'userprofile': userprofile,
    }
    return render(request, 'accounts/edit_profile.html', context)


@login_required(login_url='login')
def change_password(request):
    """
    This function processes a POST request containing current and new password
    information. It verifies the current password, updates it with the new one
    if the current password is correct and redirects the user with appropriate
    success or error messages.
    """
    if request.method == 'POST':
        current_password = request.POST['current_password']
        create_new_password = request.POST['create_new_password']
        confirm_new_password = request.POST['confirm_new_password']
        user = Account.objects.get(username__exact=request.user.username)
        if create_new_password == confirm_new_password:
            success = user.check_password(current_password)
            if success:
                user.set_password(create_new_password)
                user.save()
                messages.success(
                    request, 'Your password has been successfully updated')
                return redirect('change_password')
            else:
                messages.error(
                    request, 'Please enter your exact current password')
                return redirect('change_password')
        else:
            messages.error(request, 'Password does not match')
            return redirect('change_password')

    return render(request, 'accounts/change_password.html')
