# KidoMart

Kidomart is an e-commerce website that sells a variety of children's products. We give you a wide range of categories consisting of dolls, toys, clothing, electronics, beauty and accessories to choose from. And as part of our inaugurational promotion, we deliver it to your doorstep free of charge.

The live link can be found here: [Live Site - KidoMart](https://kidomart-78f25893d540.herokuapp.com/)

![Mock Up](media/docs/readme-images/mockup-kidomart.jpg)

## Table of Contents
- [KidoMart](#kidomart)
  - [Table of Contents](#table-of-contents)
- [User-Experience-Design](#user-experience-design)
  - [The-Strategy-Plane](#the-strategy-plane)
    - [Site-Goals](#site-goals)
    - [Agile Planning](#agile-planning)
      - [Epics](#epics)
      - [User Stories](#user-stories)
  - [The-Scope-Plane](#the-scope-plane)
  - [The-Structure-Plane](#the-structure-plane)
    - [Features](#features)
    - [Features Left To Implement](#features-left-to-implement)
  - [The-Skeleton-Plane](#the-skeleton-plane)
    - [Wireframes](#wireframes)
    - [Database-Design](#database-design)
    - [Security](#security)
  - [The-Surface-Plane](#the-surface-plane)
    - [Design](#design)
    - [Colour-Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
  - [Technolgies](#technolgies)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Version Control](#version-control)
    - [Heroku Deployment](#heroku-deployment)
  - [Credits](#credits)

# User-Experience-Design

## The-Strategy-Plane

### Site-Goals

The website is aimed at providing a platform for parents, wards and children themselves to easily shop online. Registered users are able to easily purchase items ranging from toys to educational essentials online.

Our free inaugral and promotional nation-wide delivery ensures that ordered products with the 'paid' status are rightfully delivered to the associated billing addresses on time.

We look forward to becoming the best seller for children's products.

### Agile Planning

This project was developed using agile methodologies by delivering small features in incremental sprints. There were 9 sprints in total, spaced out evenly over eight weeks.

The kanban issues were assigned to epics and were labelled as 'must have' and 'could have'. They were assigned to sprints based on their level of priority. It was done this way to ensure that core requirements are first taken care of.

The Kanban board was created using github projects and can be located [here](https://github.com/users/samuelandersoncodes/projects/2) Each issue within it consists of a user story, acceptance criteria and tasks that defines the required functionality and its associated tasks to be executed. In total, there were 22 issues. 

### KidoMart Project Board
![Kanban project image](media/docs/readme-images/kanban-project.jpg)

### KidoMart Issues
![Kanban issues image](media/docs/readme-images/kidomart-issues.jpg)

#### Epics

The project had 6 main Epics:

**EPIC 1 - Deployment Epic**

The app was first deployed to heroku so that the site is live for users. All dependencies were put in place and thouroughly tested to ensure that the live app is properly set up and has no problems. This epic was implemented first in order to avoid last minute deployment descrepancies. 

**EPIC 2 - Base Setup**

The base setup epic is for all stories needed for the base set up of the application. Without the base setup, the app would not be possible so it was the next epic to be delivered after deployment as all other features depend on it. Here, the home page view, page navigation, product detail views and admin store management were executed.

**EPIC 3 - Registration and User Account**

In the registration and user account epic, user and super user accounts management, user registration, user authentication, password recovery, password recovery email confirmation and user profile management were executed. This epic was very important because shoppers can only make a purchase if they are authenticated. It was therefore considered as the next epic after the base setup.

**EPIC 4 - Product Sorting and Searching Epic**

The Product sorting and searching epic is for all stories related to the product sorting functionality, product categories and the product search functionality. This is very crucial for the grouping of products for easy identification and user search.

**EPIC 5 - Purchasing and Checkout**

The purchasing and checkout epic is for all stories that relate to product purchasing customization, shopping cart management, cart quantity management, checkout summary, order confirmation management, order confirmation email as well as rating and reviews.

**EPIC 6 - Documentation**

This epic is for all documentation related stories and tasks that are needed to document the software development lifecycle of the application. It aims to deliver quality documentation, explaining all stages of development and necessary information on running, deploying and using the application.

#### Sprints

**EPIC 1 - Deployment Epic**

**Sprint 1**

##### User Stories

As a developer I want the application to be deployed on Heroku successfully so that is live and accessible through the Heroku domain.

As a developer, I want the necessary environment variables to be configured on Heroku so that I am sure that all dependencies like AWS s3 bucket, postgresql, stripe and django are properly wired up for the full and overall functionality of the deployed app.

As a developer, I want the application to make use of the ElephantSQL database in the production environment so that all my database schema, tables and its associated data are well structured for data storage and display.

As a developer, I want to configure the application to use AWS S3 so that all static files are safely stored and served.

##### Acceptance Criteria

- The application is successfully deployed on Heroku. The deployed application must be accessible through a Heroku domain.
- All necessary environment variables are configured on Heroku.
- The application seamlessly interacts with the ElephantSQL database on Heroku.
- Static and media files are stored and served from the configured AWS S3 bucket.
- The DEBUG setting is finally set to False.

##### Tasks

- Create a kidomart Github repository.
- Create a Heroku app for kidomart and link it to the kidomart repository on Github.
- Install Django and create the kidomart project.
- Wire up the settings for database, wsgi procfile, middleware, static and media file setups.
- Make the initial commit when the app is set and live.
- Set all necessary environment variables both in the gitpod workspace and in the Heroku settings.
- Ensure that no secret key is commited to the kidomart repository.
- Set up all dependecies for Django, AWS s3 bucket, elephant postgresql, whitenoise, stripe and email host.   
- Ensure the project's dependencies and configurations are compatible with Heroku and all other used dependencies.
- Make regular commits after every bit of significant increment.

**EPIC 2 - Base Setup**

**Sprint 2**

#### Product Display

##### User Story
As a shopper, I want to see a list of all available products so that I can browse through and make informed purchase decisions.

##### Acceptance Criteria 
- The product list should display product names, images, price and rating.

- There is a drop down menu that displays available categories.

- The page should include a search bar to enable users to search for specific products by name, description or category.

##### Tasks
- Design and implement a responsive product list interface using HTML and CSS.

- Retrieve product data from the database and display it dynamically with Python and Django on the product list page.

#### Product Detail Page

##### User Story

As a shopper, I want to view detailed product information, including descriptions, images, ratings, reviews and pricing, so that I can make informed purchase decisions.

##### Acceptance Criteria

- The product details page should display the product name, description, images, price, ratings, reviews and any available variations of colour and or size.

- The product details page should include a section for customer reviews and ratings.

- Given the product details page, the user should be able to see high-resolution images of the product.

- The product details page should display the product's stock information. Shopper should be informed if a particular product is out of stock.

##### Tasks

- Design and implement a product details page template with a user-friendly layout using HTML and CSS.

- Retrieve and display detailed product information dynamically on the product details page, including product description, images, average rating, reviews and pricing.

- Implement a system to display product variations, if applicable. For instance, size, color and quantity to choose from.

- Develop a feature to enable customers to leave reviews and ratings for purchased products and display them on the product details page.

- Ensure that the product details page is responsive and compatible with various devices and screen sizes.

#### Home Page Pagination

##### User Story

As a site user I want to be able to easily navigate through multiple pages of product listings so that I can find and view the products I am interested in.

##### Acceptance Criteria

- When viewing products or category of products with twelve and eight  products respectively, I should see a pagination component at the bottom of the page.

- The pagination component should display page numbers and navigation controls, such as "PREV" and "NEXT."

- Clicking on a page number should load and display the corresponding set of products on the page.

- The current page should be visually highlighted for good user experience.

- The "PREV" button should be disabled if the user is on the first page and the "NEXT." button should be disabled if the user is on the last page.

Implement logic in the backend to paginate product listings based on  home page products, the selected category or search query.

##### Tasks

- Utilize Django's Paginator mechanism to handle the pagination logic efficiently.

- Create a reusable frontend component for pagination. Ensure the component can dynamically render the page numbers and adjust the display based on the current page and total number of pages.

- Apply appropriate styles to the pagination component for a cohesive and visually appealing design.

- Ensure the pagination is responsive and works well on various screen sizes and devices.

- Ensure that clicking on a page number triggers the appropriate calls to retrieve and display the corresponding products.

- Conduct a thorough test to ensure the pagination component works well without errors.