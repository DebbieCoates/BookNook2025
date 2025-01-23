# **BookNook**

## Overview

**BookNook** BookNook is a community platform designed to connect readers and literary enthusiasts, providing a space for members to easily discover new books. The platform caters to book lovers who wish to delve into book details, save their favorite titles for future reading, and engage with the community by writing reviews. Aimed primarily at adult readers, the site fosters connections among like-minded individuals through shared book reviews. Additionally, it offers robust tools for administrators to effectively manage content, moderate reviews, and maintain the book database.

This project is part of the Code Institute's Full-Stack Developer course and focuses on the Django framework, database manipulation, and CRUD functionality.

<!-- 
[Live project](https://book-club-acf9649c2594.herokuapp.com/)

[Django administration](https://book-club-acf9649c2594.herokuapp.com/admin/) -->

Admin Username: bookend

Password: debbiesproject

[Project Board](https://github.com/users/DebbieCoates/projects/13)

## UX - User Experience

### Design Inspiration

My inspiration for designing this book review project stems from my deep love of books. I aimed to create a clean and 
uncluttered interface, with clear, crisp forms and reader-friendly fonts, to ensure an enjoyable and seamless experience for all book lovers.

### Colour Scheme
<!--
 In line with the healthcare theme, I chose a neutral, clean palette:
 - **Primary Color:** #17A2B8 (Navy Blue-Grey)
 - **Secondary Color:** #132B67 (Hospital Blue)
 - **Accent Color:** #333 (grey)
 - **Background:** #fff (White)
 This combination ensures clarity, accessibility, and a professional appearance, allowing for easy navigation throughout the site.
-->
### Font
<!--
- For the logo and headers, I will be using **Lora**.
- The rest of the body text and interactive elements will use **Catamaran** for its readability and clean look.
-->
## Project Planning

### Strategy Plane
<!--
The primary objective of HealMate is to bridge the gap between patients and healthcare providers. By offering an intuitive interface, users can easily search for medical professionals, book appointments, and receive necessary care without hassle.
-->
### Site Goals

- Community Engagement: Foster a sense of community among book lovers, this helps members connect, share their thoughts, and build relationships around their mutual love of books.

- User-Friendly Interface: Ensure the website is easy to navigate with a clean and intuitive design. This includes clear menus, and responsive design for various devices. A user-friendly interface makes it easier for members to find and engage with content.

- Allows Admins to manage the website.


### Agile Methodologies - Project Management

I used an agile approach to project management. 

### MoSCoW Prioritization

- **Must-[Haves]:** User registration and login, role-based dashboards.
- **Should-Haves:** Add/Edit a Book, Add/Edit  a review,  Add to wishlist
- **Could-Haves:** Profile pictures for users 
- **would like to have:** Book recomendatons, Top 10 books

## User Stories

- As a member, I want to log in securely so that I can access my dashboard and manage my activities.
- As a member I want to leave a review and rating for books I have read.
- As Admin I want to be able to add, edit and delete books and posts from the database so that I can manage the content on the platform.
- As a visitor, I want to sign up easily, so that I can join the Book Nook.
- As a member I can delete any reviews I have written.
- As a member I can remove books I've read or am no longer interested in.
- As a member I want o add books to my Wish List, so that i can save the book for future reading.
- As a member, I want to view all the books listed
- As a member, I would like to view the top ten rated books based on other members recommendations, in order to suggest my next read.
- As an admin, I want to see the profile images of members, so that I can verify their identity and ensure a professional presence on the platform.
- As a member I would like to be able t refer books to other users if I like them.
- As an admin, I want to be able to approve any books added to the website in order to validate their appropriateness for the website.
- As a member, I would like the ability to add books to the website so that they can be displayed and reviewed by others.

## Scope Plane

The BookNook platform will include the following MVP functionalities:
- User registration and role-based navigation.
- view a list of all books.
- view of list of books on users wishlist.
- view individual books.
- Add/update a member profile.
- Add/update a book review.
- (Admin only) view a list of books waiting to be approved for uploading onto the website.
- (Admin only) view a list of All books listed on the website and delete any if required.


## Structural Plane

The site is structured around an easy-to-use interface. The primary menu includes links to all features applicble to role (Member, Admin).

Members 

## Skeleton & Surface Planes

### Wireframes

Wireframes were created for the following key pages to ensure an intuitive user journey:

- **Home Page**
![Homepage & Navigation](booknook/docs/Wireframes/homepage_and_navigation.png)

- **Books**
![Books](booknook/docs/Wireframes/Books.png)

- **Book List**
![Book List](booknook/docs/Wireframes/BookList.png)

- **Book List**
![Add Book](booknook/docs/Wireframes/Add_book.png)

- **Member Profile**
![Member Profile](booknook/docs/Wireframes/member_profile.png)

- **Pending Approval**
![Pending Apprival ](booknook/docs/Wireframes/Pending_Approval.png)

- **Wishlist**

![Wishlist ](booknook/docs/Wireframes/wishlist.png)

- **Django Admin**

- Django Admin panel, accessable via URL/Admin with correct ccredentials

![Adnmin Logon](booknook/docs/screenviews/Admin.png)
![Admin List](booknook/docs/screenviews/admin_lists.png)


Wireframes were designed using [Balsamiq](https://balsamiq.com/), ensuring responsiveness across devices.





## Data Models

### Book Model:

- Each book in our club will have attributes such as title, author, description

### Review Model:

- The Review model will store reviews users leave for each book. It is linked both to the Book and the User models.

### WishList Model:

- The WishList Model will store information about the books that users have added to their "wishlist". It is linked both to the Book and the User models.

### User Model:

- The User model is provided by Django.

### Relationships:

#### User <-> Review:

- One-to-many relationship: One user can write multiple reviews, but each review belongs to only one user.

- Foreign Key: user_id in the Review table references the id in the User table.

#### Book <-> Review:

- One-to-many relationship: One book can have multiple reviews, but each review is linked to only one book.

- Foreign Key: book_id in the Review table references the id in the Book table.

 #### User <-> WishList:

- One-to-many relationship: One user can have many wish list entries.

- Foreign Key: user_id in the User table references the id in the WishList table.

#### Book <-> WishList:

- One-to-many relationship: Each book can appear in the "Want-to-read" list of multiple users.

- Foreign Key: book_id in the Book table references the id in the WishList table.

### Models

 **Book Model**
- title: The title of the book.
- author: The author of the book.
- synopsis: A brief summary of the book.
- slug: A URL-friendly version of the title.
- book_cover: The cover image of the book stored in Cloudinary.
- part_of_series: A boolean indicating if the book is part of a series.
- ISBN: The International Standard Book Number.
- featured: A boolean indicating if the book is featured.
- approved: A boolean indicating if the book is approved.
- uploadedby: A foreign key linking to the User who uploaded the book.
- uploadedOn: The date and time when the book was uploaded.
- category: The category of the book.

 **member Model**
- user: A one-to-one relationship with the User model.
- bio: A short biography of the member.
- location: The location of the member.
- birth_date: The birth date of the member.

 **Review Model**
- book: A foreign key linking to the Book model (many-to-one relationship). This indicates that multiple reviews can be written for a single book.
- author: A foreign key linking to the User model (many-to-one relationship). This indicates that multiple reviews can be authored by a single user.
- body: The content of the review.
- approved: A boolean indicating if the review is approved.
- created_on: The date and time when the review was created.
- rating: The rating given to the book, with a validator to ensure it's between 1 and the maximum allowed value.

 **Wishlist Model**
- user: A foreign key linking to the User model. This indicates that multiple wishlists can belong to a single user.
- book: A foreign key linking to the Book model. This indicates that multiple books can be added to a single user's wishlist.
- added_at: The date and time when the book was added to the wishlist.


### ER Diagram

The ERD for HealMate illustrates the relationships between the users, members, Books, Reviews and wishlist. This is essential to demonstrate the relationships between the different models in the PostgreSQL database.

![ERD Illustration](booknook/docs/Wireframes/Booknook_ERD.png)

## Security

All data is securely handled with Django’s security features, including:
- CSRF protection for form submissions.
- Data encryption for sensitive information like passwords using Django's built-in authentication.
- Role-based access control to restrict sensitive data to authorized users.

## Features

### HomePage (All)

![HomePage](booknook/docs/screenviews/Homepage.png)
 
- Hero Section: A welcoming banner with a catchy tagline introducing the Book Nook to potential users. 

- Navigation Bar: A clean navigation bar allowing users to access the Home, and Login/Register options. Responsive design ensures usability across devices.

![Login](booknook/docs/screenviews/login.png)
![Register](booknook/docs/screenviews/register.png)

- Featured Books: A selection of popular or recently added books to engage visitors.

![Feaatured Books](booknook/docs/screenviews/featured_books.png)

- If a user is logged in, clicking more will lead to more details of the book selected.

### Books (Loggin in User)

![Books](booknook/docs/screenviews/books.png)

- Paginated view of books for user to select
- More button leading to more book details

![Books](booknook/docs/screenviews/book.png)

### Add Book

- Add Biik Sectiion which enables members & Admin to upload Books onto the website
- Books wont show on theWebsite until approved by Admin.

![Books](booknook/docs/screenviews/add_book.png)

### Pending Approvals (Admin Only)

- Pending Approvals section listing all books that have been uploaded to the website for approval.
- Once approved the book will be added to the website for all to view and/or review

![Pending Approvals](booknook/docs/screenviews/pending_approval.png)

### Book List (Admin Only)

- Admin view of All Books
- Books can only be deleted by admin.  Deleting a book will also delete any associated reviews
- Unapproved Books will be highlighted in Yellow

![BookList](booknook/docs/screenviews/booklist.png)

### Profile
- view of members profile, By default will be blank, but is associated with user, so all users will ahve a profile
- button to update profile

![Profile](booknook/docs/screenviews/profile.png)
![Update Profile](booknook/docs/screenviews/call_to_action_Profile.png)

## Future Features

I plan to implement the following in future iterations:
- The ability to Update book information.
- The ability to reccomend a book to other users.

## Technologies & Languages Used

- HTML5 - Markup language for structuring the website
- CSS3 - Styling language for designing the layout and visual aesthetics
- JavaScript - For interactivity and DOM manipulation on the frontend
- Python (Django) - Backend web framework for server-side logic and management
- PostgreSQL - Database management system for storing data
- Cloudinary - Cloud-based image storage solution
- Whitenoise - For serving static files directly from Django
- SmartDraw - for ERD

## Libraries & Frameworks
- **Django** - Backend framework
- **Django Crispy Forms** - For elegant form rendering
- **Cloudinary** - Media storage
- **Whitenoise** - For serving static files

## Tools & Programs
- **GitHub Projects** - Project management and tracking
- **Heroku** - Deployment and hosting
- **Balsamiq** - Wireframes and design prototypes

## **Testing**

### **Validation Testing**

All Pages have been run through the Wave Evaluation Tool, and have no errors  ( 2 sample pages below)

![Wave Evaluation Homepage ](booknook/docs/testing/wave_evaluation_homepage.png)
![Wave Evaluation Books](booknook/docs/testing/wave_evaluation_books.png)

All code has been validated through:

- **HTML**: [W3C Markup Validator](https://validator.w3.org/).
- **CSS**: [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).
- **Python**: PEP8 validation to ensure code quality.

<!-- ![HTML validator test](docs/project-images/Screenshot%202024-10-04%20164347.png) -->

![CSS validator test](booknook/docs/testing/css_validation.png)


### **User Testing**

- **Browser Compatibility**: The website has been tested on Chrome, 
- **Responsiveness**: The platform has been tested on mobile, tablet, and desktop devices to ensure optimal performance.
- **Role-Based Dashboard Testing:** Each user type (nonuser, member, Admin) was tested to ensure they were directed to the correct dashboard after login.

<!--
### **Bugs**
- ### Bug Fix #1: `DISABLE_COLLECTSTATIC` Setting Causing Heroku Deployment Failure

**Issue:**  
During the deployment to Heroku, the following error occurred:

The error was caused by the absence of proper static file handling and a misconfiguration in the `INSTALLED_APPS` list in `settings.py`.

**Cause:**  
- The `DISABLE_COLLECTSTATIC=1` config variable was used in Heroku to prevent collectstatic from running during the initial setup.
- There was a duplicate entry for `django.contrib.staticfiles` in `INSTALLED_APPS`, which caused an error when trying to collect static files.

**Steps Taken to Fix:**
1. Fixed the duplicate `django.contrib.staticfiles` entry in `INSTALLED_APPS`.
2. Ensured the static and media handling was properly set up with Cloudinary and Whitenoise.
3. Deleted the `DISABLE_COLLECTSTATIC=1` from Heroku's Config Vars.
4. Deployed again, which successfully collected static files and completed the deployment.


### Bug Fix #2: Permission Issues with Dashboard Access

**Issue**

Users are unable to access the Admin, Patient, and Specialist dashboards even though they are assigned to the correct user groups in the Django admin panel. The application either throws a 403 Forbidden error or does not recognize the users' group memberships.

**Cause**

The issue seems to be related to incorrect handling of group membership checks in the views or misconfiguration of user group assignments within the Django admin panel.

### Steps Taken to Fix

1. **Investigate Group Check Functions**:
   - Reviewed the group-check functions (`is_admin`, `is_patient`, `is_specialist`) in `views.py` to ensure they correctly identify user groups.
   - Confirmed that the group names match those set in the Django admin.

2. **Validate Group Assignments**:
   - Ensured that users are properly assigned to the correct groups (Admin, Patient, Specialist) in the Django Admin panel.
   - Verified that the group names in the code match the group names set up in Django admin.

3. **Testing**:
   - Tested access with both existing and newly created users to ensure they can access their respective dashboards without issues.
   - Verified that group membership was properly recognized for all users.

4. **Revert Changes**:
   - Once the issue was resolved, reverted any temporary modifications to the views back to their original implementation.

5. **Verify Access Control**:
   - Tested edge cases, such as users without group assignments attempting to access dashboards, to ensure proper behavior.
   - Confirmed that custom `PermissionDenied` logic displayed the correct 403 error page for unauthorized access attempts.

**Outcome**

The problem was successfully resolved, allowing users to access their respective dashboards based on group membership without encountering 403 errors or redirection issues.

### Bug Fix #3: Form Not Visible on Homepage Due to Conflicting View Usage

### Issue
The form on the homepage not visible due to conflicting view usage. The homepage should display a form that allows users to search for specialists, but the form did not appear as expected.

### Cause
The conflict arises from the use of both a class-based `HomePage` view and a function-based `home` view. The class-based view does not properly pass the `specialties` context required to render the form on the homepage.

### Steps Taken to Fix

1. **Update URLs**:
   - Updated `core/urls.py` to replace the class-based `HomePage` view with the function-based `home` view to ensure the correct context is passed.

2. **Verify Context Passing**:
   - Verified that the `specialties` context was properly passed to `index.html` so that the form could display the list of specialties dynamically.

3. **Test Form Visibility and Functionality**:
   - Tested the homepage to ensure that the form was visible and correctly populated with the list of specialties from the database.

4. **Commit Changes**:
   - Added and committed the changes after confirming that the issue was resolved.

### Outcome
The form is now visible on the homepage and correctly displays the list of specialties, allowing users to search for specialists as intended. The conflict between the views was resolved by using the appropriate function-based view that properly passes the necessary context.


### Bug Fix #4: Signal Not Triggering on User Registration

### Issue
A Django signal intended to automatically assign new users to the "Patients" group and create a `PatientProfile` upon registration was not firing. This led to no profile being created and no group being assigned after user registration.

### Cause
The issue was caused by an incorrect configuration of the `AccountsConfig` class in `INSTALLED_APPS` in `settings.py` and missing signal imports in the `ready()` method of `accounts/apps.py`.

### Steps Taken to Fix

1. **Correct Configuration in INSTALLED_APPS**:
   - Updated `INSTALLED_APPS` in `settings.py` to reference `'accounts.apps.AccountsConfig'` instead of just `'accounts'`. This ensured that the custom AppConfig class was properly loaded.

2. **Add Signal Imports in `ready()` Method**:
   - Added a `ready()` method in `accounts/apps.py` to correctly import the signal handlers, ensuring they were registered when the app was loaded.

3. **Remove Debug Statements**:
   - Removed unnecessary print statements that were used for debugging to keep the code clean and efficient.

### Outcome
The signal is now correctly triggered upon user registration, resulting in the automatic assignment of new users to the "Patients" group and the creation of a `PatientProfile` as intended. The configuration in `INSTALLED_APPS` and signal registration were successfully fixed.


### Bug Fix #5: Specialist Availability Submission and Display Issues

### Issue
Specialists encountered multiple issues when trying to set their availability. Initially, a 405 Method Not Allowed error occurred upon form submission. After fixing that, the start time was not displayed on the specialist dashboard, while the end time appeared correctly.

### Cause
1. **405 Method Not Allowed**:
   - The `post` method was missing from the `SpecialistDashboardView` class in `dashboard/views.py`, resulting in the 405 error when attempting to submit availability.

2. **Missing Start Time**:
   - The `start_time` was not displayed on the specialist dashboard due to a missing template tag (`{{ availability.start_time }}`) in the "Your Availability" section.

### Steps Taken to Fix

1. **Handle POST Method in View**:
   - Added a `post` method to `SpecialistDashboardView` in `dashboard/views.py` to properly handle form submissions, resolving the 405 Method Not Allowed error.

2. **Fix Start Time Rendering in Template**:
   - Updated the specialist dashboard template to include the `{{ availability.start_time }}` tag, ensuring that both the `start_time` and `end_time` are displayed in the "Your Availability" section.

### Outcome
Specialists can now successfully submit their availability without encountering the 405 error. Both `start_time` and `end_time` are displayed correctly on the specialist dashboard, providing a complete view of their available times for appointments.


### Bug Fix #6: Incorrect Template Rendered for Specialist Search Results

### Issue
The incorrect template was being rendered for specialist search results on the HealMate platform. A secondary `search_results.html` template in a different directory was causing confusion, leading to a simplified search results page being displayed. Key features like specialist bio, profile image, and pagination were missing.

### Cause
An additional `search_results.html` template was located inside the global `/templates/specialists/` directory. This template had minimal content and was unintentionally overriding the correct `search_results.html` template in the `/specialists/templates/specialists/` directory.

### Steps Taken to Fix

1. **Isolate Problematic Template**:
   - Renamed the global `/templates/specialists/` directory to determine if it was the source of the issue.

2. **Confirm and Resolve Issue**:
   - After confirming the issue was caused by the additional template, deleted the `/templates/specialists/` directory and its contents.

3. **Verify Correct Template Rendering**:
   - Verified that the correct `search_results.html` template inside `/specialists/templates/specialists/` is now rendering, displaying all necessary features, including the specialist bio, profile image, and pagination.

### Outcome
The correct template for specialist search results is now rendering as intended. The page displays all relevant information, including specialist bio, profile images, and pagination, providing users with a complete view of search results.


-->
## Deployment

All code for this project was written in Gitpod as the integrated development environment. GitHub was used for version control, and the application was deployed to Heroku from GitHub.

### Pre-Deployment

To ensure a successful deployment to Heroku, the following practices are to be followed (Experience from previous Django projects):

- **Requirements File:** The `requirements.txt` file must be kept up to date to ensure all imported Python modules are configured correctly for Heroku.
- **Procfile:** A `Procfile` was added to configure the application as a Gunicorn web app on Heroku.
- **Allowed Hosts:** In `settings.py`, the `ALLOWED_HOSTS` list was configured to include the Heroku app name and `localhost`. Example format:
    ```python
    ALLOWED_HOSTS = ['your-app-name.herokuapp.com', 'localhost']
    ```
- **Environment Variables:** All sensitive data such as the `DATABASE_URL`, `CLOUDINARY_URL`, and `SECRET_KEY` were added to the `.env` file, which is ignored by Git using `.gitignore`. These variables are added to Heroku manually through the Config Vars section.

### Deploying with Heroku

The steps for deploying to Heroku are as follows (Experience from previous Django projects):

1. **Create New App:** Log in to your Heroku account and click on the "Create New App" button.
2. **App Name:** Choose a unique name for your app.
3. **Select Region:** Choose the appropriate region (Europe was selected for this project).
4. **Create App:** Click the "Create App" button to proceed.
5. **Deployment Method:** In the "Deploy" tab, select GitHub as the deployment method.
6. **Connect to GitHub:** Search for the repository name and click "Connect".
7. **Manual or Automatic Deployment:** Select either manual or automatic deployment. Ensure the main branch is selected for deployment.
8. **Config Vars:** In the "Settings" tab, click "Reveal Config Vars" and input the required environment variables.
9. **Buildpack:** Select Node.js and Python as the buildpacks for your project.
10. **Deploy:** Once the configuration is complete, click the "Deploy Branch" button. After successful deployment, a "View" button will appear to take you to the live site.

The live link for this project can be found here: <a href="https://booknook2025-4c3ce9e8c031.herokuapp.com/" target="_blank">BookNook</a>

### Fork this Repository

1. Go to the GitHub repository.
2. Click the "Fork" button in the upper right-hand corner.

### Clone this Repository

1. Go to the GitHub repository.
2. Click the "Code" button at the top of the page.
3. Choose between 'HTTPS', 'SSH', or 'GitHub CLI' depending on your preference.
4. Click the copy button to copy the URL.
5. Open Git Bash.
6. Change the working directory to where you want to clone the directory.
7. Type:
    ```bash
    git clone https://github.com/DebbieCoates/BookNook2025

    ```
8. Press Enter to create the local clone.

**Note:** The difference between a clone and a fork is that with a clone, you need permission to push changes to the original repository, whereas a fork creates an entirely new project under your GitHub account.

## Credits

### Code
- **Django Documentation**: The official docs were invaluable in setting up the project structure and solving specific issues.
- **Django Crispy Forms Documentation**: Used to streamline form rendering.
- **coPilot**: For  coding ideas
- **Favicon.io**: For Favicon generation.
- **Google Fonts**: For typography.
- **Bootstrap 5**: for layout.

### Media

- Icons and images sourced from **Creative Fabrica** and **favicon**.

### Additional tutorials/books/blogs

- Django 5 By Example, by Antonieo mele
- Codemy.com

## Acknowledgements

I would like to extend my heartfelt gratitude to the following individuals and organizations whose support, guidance, and inspiration have been invaluable in the development of this project.

### Mentors and Advisors

- **To all my amazing classmates**

I want to extend a heartfelt thank you to each and every one of you. We've had an environment where laughter, encouragement, and support have flourished. The camaraderie we've built has made this journey not only educational but genuinely enjoyable. The ability to have a laugh and joke has lightened the workload. When challenges arose, helping and encouraging each other made all the difference.

I'm grateful to be part of such an incredible group. Thank you for being such fantastic classmates!


- **Amy Richardson** 

I extend my deepest gratitude to Amy Richardson, my tutor and facilitator, for her unwavering support and expert guidance throughout this journey. Her mentorship provided the clarity and confidence I needed to overcome challenges, which significantly enhanced the quality of this project. Amy's dedication and encouragement have left a lasting impact on my progress and learning. Her departure is a great loss to both our class and the Code Institute, as her influence and expertise truly made a difference. Moreover, her positive attitude and steadfast support always uplifted the group – she was genuinely a ray of sunshine, always cheerful and encouraging, regardless of the circumstances. I am incredibly thankful for your commitment and for taking on the challenge of leading us with such dedication. Thank you for everything!

- **Vasilica Pavaloi**

A big thank you to Vasilica Pavaloi for stepping in when Amy left and guiding us through the final weeks of our project. You helped us stay focused and motivated, and got us to the finish line. Thank you for everything

- **Spencer Barriball, Roo MacArthur & John Reardon** 

A big thank you to Spencer, John, and Roo for all their support, helpful feedback, and constructive criticism throughout this project. Their knowledge and encouragement really pushed me to improve and kept me on track. The Coding Coach channel was an absolute lifeline. This project wouldn’t have been the same without their guidance.

### Supportive Friends and Family
- My friends and family, especially, for their encouragement and patience during this project. Your belief in me kept me motivated and focused.

### Academic Institutions
- **Code Institute** – Thank you for providing the learning environment and resources that made this project possible. I am especially grateful to the professors and staff at Code Institute for their valuable insights.

### Final Note
This project would not have been possible without the support, advice, and inspiration of each individual and organization mentioned. Thank you for being a part of this journey.

