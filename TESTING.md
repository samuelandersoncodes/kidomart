## Testing

## Functional Testing

**Registration**

Description:

Ensure a user can successfully register on the Kidomart e-commerce website.

Steps:

1. Navigate to [KidoMart](https://kidomart-78f25893d540.herokuapp.com/) and click on the "Register" link.
2. Enter your details in the registration form (All fields are required):
- First Name: John
- Last Name: Doe
- Email Address: john.doe@example.com (must be an active email)
- Phone Number: +1 555-123-4567
- Create Password: Password123
- Confirm Password: Password123
3. Click the "Register" button.

Expected:

An activation email is sent to the user with a secure link to activate their account. Upon clicking the link in the email, user is redirected to the login page with an activation success message.

Actual:

User recieves an activation link via email. After account activation, user is redirected to the login page with a success message confirming the account registration and activation.

<hr>

**Login**

Description:

Ensure a user can successfully log in to his or her Kido account.

Steps:

1. Navigate to [KidoMart](https://kidomart-78f25893d540.herokuapp.com/) and click on the "Login" link.
2. Enter your details in the registration form (All fields are required):
- Email Address: john.doe@example.com (must be the exact email user registered with)
- Password: Password123 (user's exact password)
3. Click the "Login" button.

Expected:

User is successfully logged in to his or her account dashboard with a login success message.

Actual:

User is successfully logged in to his or her account dashboard with a login success message.

<hr>

**Logout**

Description:

Ensure a user can log out

Steps:

1. Login to the website
2. Click the logout button from the navbar or on the dashboard side bar

Expected:

User is logged out and a logout success message is displayed.

Actual:

User is logged out and a logout success message is displayed.

<hr>

**Password Reset**

Description:

Ensure a user can successfully reset their password on the Kidomart website.

Steps:

1. Navigate to the [KidoMart login page](https://kidomart-78f25893d540.herokuapp.com/accounts/login/)  and click on the "Forgot Password" link on top of the login button.
2. Verify that the user is redirected to the "Password Reset" page with the heading and instructions.
3. Fill in the email address you registered with and click the "Submit" button.
4. Verify that a verification email is sent to the provided email address.
5. Check the email inbox and click on the verification link in the password reset email.
6. Verify that the user is redirected to the "Password Reset" page.
7. Enter a new password and confirm the new password.
8. Click the "Reset Password" button.
9. Verify that the user is redirected to the login page with a success message indicating the password reset was successful.
10. Log in with the new password to ensure successful login.

Expected:

The user can successfully initiate a password reset from the "Forgot Password" link.
The user receives a verification email and can click the link to reset the password.
After successfully resetting the password, the user is redirected to the login page with a success message.
The user is able to log in with the new password.

Actual:

The user can successfully initiate a password reset from the "Forgot Password" link.
The user receives a verification email and can click the link to reset the password.
After successfully resetting the password, the user is redirected to the login page with a success message.
The user can log in with the new password.

<hr>

**Change Password**

Description:

Ensure a user can successfully change their password on the Kidomart website.

Steps:

1. Navigate to the [KidoMart Dashboard](https://kidomart-78f25893d540.herokuapp.com/accounts/change_password/) and click on the "Change Password" on the the sidebar.
2. Enter your current password.
3. Create new password.
4. Confirem new password. (Make sure the new password is exactly what you enter here)
5. Click on the 'Change' button.

Expected:

After successfully changing the password, the user is redirected to the password change success page. The success page contains a heading and a text indicating the success of the password change.
The user can either log in or go to the home page from the success page by clicking the "Login" or the 'home' button. Logging in with the updated password is successful.

Actual:

After successfully changing the password, the user is redirected to the password change success page. The success page contains a heading and a text indicating the success of the password change.
The user can either log in or go to the home page from the success page by clicking the "Login" or the 'home' button. Logging in with the updated password is successful.


