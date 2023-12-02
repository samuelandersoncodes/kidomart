from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product, ReviewRating
from .forms import ReviewForm


def submit_review(request, item_id):
    """
    This function handles the submission of product reviews.
    It retrieves the URL of the previous page using the HTTP_REFERER header.
    Checks if the form submission method is POST.
    If a review by the current user for the specified product already exists,
    It loads the existing review into the ReviewForm for an update.
    If no existing review is found, it creates a new review rating instance
    using the ReviewForm data.
    """
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            product = get_object_or_404(Product, item_id=item_id)
            reviews = ReviewRating.objects.get(
                user__id=request.user.id, product=product)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(
                request, 'Your review has been successfully updated')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product = get_object_or_404(Product, item_id=item_id)
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Thanks! Your review is added.')
                return redirect(url)
