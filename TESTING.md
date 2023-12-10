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