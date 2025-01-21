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
<!--
My inspiration for HealMate came from a personal experience during a routine visit to my GP. I thought about how many medical consultations, especially those that don’t require physical examinations, could easily be handled online. This thought extended to pregnant women, who often need guidance and reassurance from their midwives or doctors but don’t necessarily need an in-person visit. The convenience of a digital platform for such consultations became clear. The name HealMate reflects the idea of a supportive, reliable partner in managing one's health—much like popular health apps such as ClueMate, where ‘Mate’ signifies companionship and guidance in managing health.
-->
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
<!--
- Provide patients with a user-friendly platform to book appointments with various specialists.
- Allow doctors to manage their appointments and patient information.
- Offer an intuitive interface with role-based dashboards for admins, specialists, and patients.
-->

### Agile Methodologies - Project Management
<!--
I used an agile approach to project management. The HealMate development process was broken into sprints, and tasks were added to the GitHub project board to be tracked and managed through issues.
-->
### MoSCoW Prioritization
<!--
- **Must-Haves:** User registration and login, specialist search, appointment booking, role-based dashboards.
- **Should-Haves:** Feedback system, health tools, advanced filtering options.
- **Could-Haves:** Profile pictures for users and specialists, messaging system.
- **Won’t-Haves:** Full payment integration, doctor-patient messaging for now.
-->
### Sprints
<!--
- **Sprint 1:** Initial Setup - Project, repository, environment setup.
- **Sprint 2:** User Authentication & Role-Based Dashboards.
- **Sprint 3:** Specialist Search & Appointment Booking System.
- **Sprint 4:** Static Pages & UI/UX Improvements.
- **Sprint 5:** Deployment & Testing.
-->

## User Stories
<!--
- As a user (patient/specialist/admin), I want to register and log in securely so that I can access my dashboard and manage my activities.
- As a user, I want a personalized dashboard based on my role (patient, doctor, admin) so that I can access the features relevant to me.
- As a visitor, I want to see a well-designed home page that introduces HealMate so that I understand the platform's purpose and value.
- As a patient, I want to search for specialists by category (e.g., Dermatologist, Psychologist) so that I can find a doctor that meets my needs.
- As a patient, I want to view available time slots for a specialist and book an appointment, so that I can get medical advice and treatment.
- As a patient, I want to message my doctor before or after a consultation so that I can ask follow-up questions or clarify doubts.
- As a specialist, I want to manage my schedule and view patient appointments so that I can efficiently conduct consultations.
-->

## Scope Plane
<!--
The HealMate platform will include the following MVP functionalities:
- User registration and role-based dashboards.
- Search and filtering system for specialists.
- Appointment scheduling with available specialists.
- Specialist profiles showcasing specialty, experience, and availability.
-->

## Structural Plane

The site is structured around an easy-to-use interface. The primary menu includes links to specialist searches, appointment bookings, and user profile management.

## Skeleton & Surface Planes

### Wireframes

Wireframes were created for the following key pages to ensure an intuitive user journey:
- **Home Page**

![Homepage & Navigation](docs/wireframe/Homepage%20%26%20navigation.png)

![Home Wireframe](Homepage & navigation.png "Home Page & navigation")


- **Specialist Search Results**

<!-- ![Homepage Wireframe](docs/wireframe/search-result-large-screen.png) -->

<!-- ![Homepage Wireframe](docs/wireframe/search-result-mobile.png) -->

- **Member Profile**

![Homepage Wireframe](docs/wireframe/member profile.png)

- **User Dashboards** (Patient and Specialist)
- **Admin Panel**

Wireframes were designed using [Balsamiq](https://balsamiq.com/), ensuring responsiveness across devices.

<!-- ## Database Schema - Entity Relationship Diagram
The ERD for HealMate illustrates the relationships between the users, specialists, appointments, and more. This is essential to demonstrate the relationships between the different models in the PostgreSQL database.

The ERD also demonstrates the platform's role-based structure. Each user is assigned to a specific group (patient, specialist, or admin) that determines their access level. PatientProfile and SpecialistProfile models are linked to the User model, and each profile type has specific fields relevant to their role. Admins have broader access to manage both specialist vetting and platform data.

![ERD Illustration](docs/erd/erd-healmate.png)

The above ERD was generated using Python Extension - pygraphviz and pydotplus. Documentation at https://django-extensions.readthedocs.io/en/latest/graph_models.html. -->

## Security
<!--
All data is securely handled with Django’s security features, including:
- CSRF protection for form submissions.
- Data encryption for sensitive information like passwords using Django's built-in authentication.
- Role-based access control to restrict sensitive data to authorized users.

Role-based access control (RBAC) is implemented using Django's Group and Permission systems. Patients, specialists, and admins are grouped based on their role, and their access to features and sensitive information is restricted accordingly. Patients can only access their own medical data and booking history, while specialists can only view data related to their consultations. Admins have the broadest access for system management.
-->
## Features

### User View - Registered/Unregistered
<!--
HealMate offers distinct user views. Unregistered users can search for specialists, but registered users have full access to the appointment system and dashboard functionalities.

### User Registration Process
- **Patients:** When a new user registers, they are automatically assigned to the "Patient" group. This ensures that all users begin with patient privileges and access, allowing them to book appointments and view specialist profiles. During the registration process, essential patient profile information is captured (e.g., contact number, address, date of birth, gender). After the registration is complete, a corresponding PatientProfile is automatically created and associated with the user.

- **Specialists:** During the registration process, essential patient profile information is captured (e.g., contact number, address, date of birth, gender). After the registration is complete, a corresponding PatientProfile is automatically created and associated with the user.

- **Admins:** Admin accounts are created manually by other existing admins or superusers within the Django administration area. This ensures that the creation of administrative-level accounts is strictly controlled and follows the platform's internal policies.

This registration flow was chosen to ensure role-based control and security. Patients are the primary users of the platform, and allowing them to register freely makes the service accessible. However, specialists and admins require a higher level of trust and validation, so they undergo a manual vetting process. This ensures that only qualified professionals and authorized admins can manage sensitive tasks such as consultations and platform settings, which helps maintain the integrity and security of the system.

### Role-Based Dashboard Features

**HealMate includes role-based dashboards for different types of users:**
- **Patient Dashboard:** Allows patients to view their profile, manage appointments, and access medical records.

- **Specialist Dashboard:** Specialists can manage their availability, view and approve appointments, and review patient profiles.

- **Admin Dashboard:** Admins can manage users (patients, specialists) and vet specialist applications. They also have access to system-wide settings.

### Role-Based Navigation
(Not the same as Role-Based Dashboard Features)

The navigation bar in HealMate adapts dynamically based on the user's role. This feature ensures that users see only the relevant options for their role, improving usability and reducing clutter in the interface.

- **Specialists**: When logged in, specialists will only see links to their dashboard, profile, password change, and logout options. General site navigation like "Home," "About," or "Join Us" will be hidden.
- **Patients**: Logged-in patients have access to their dashboard, profile, password change, and logout options, while still seeing general navigation links like "Home" and "About."
- **Admins**: Admins will see their dedicated dashboard link and other relevant options.
- **Non-Authenticated Users**: Users who are not logged in will only see options to log in or register on the platform.

This role-based navigation provides a tailored experience for every user type, streamlining access to the most relevant pages.


### Soft Delete/Archiving for Patient Accounts
HealMate includes a soft delete mechanism to ensure data integrity and prevent accidental loss of important user information. Instead of permanently deleting accounts, users can request a soft deletion, which deactivates their account while retaining their data in the system.

**How It Works:**
- **Patient Account Deactivation:** Patients can request to have their account deactivated through a user-friendly option on their dashboard.
- **Data Preservation:** When a patient requests account deletion, their profile is marked as inactive rather than removed from the database. This means the patient’s information, appointments, and records remain available for future use or audit purposes.
- **Admin Reactivation:** Admins have the ability to reactivate patient accounts from the Django admin panel. This ensures that patients can return to the platform with all their previous data intact, avoiding any data loss or system disruptions.

**Benefits:**
- **System Integrity:** Prevents errors that could arise from full account deletions, such as broken relationships with other models (e.g., appointments, messages, feedback).
- **User Flexibility:** Patients can choose to deactivate their account temporarily and return at a later date without losing their medical history or profile information.
- **Security:** Only admins have the power to fully manage account reactivations, ensuring oversight and control over patient data.


### Appointment Booking System
HealMate allows patients to book appointments with specialists directly through the platform. The system includes:
- **Specialist Search**: Patients can search for specialists based on name, specialty, or location.
- **Book Appointment**: Patients can book an appointment directly from the specialist's profile page.
- **Appointment Management**: Specialists and patients can view and manage upcoming appointments through their respective dashboards.
- **Appointment Cancellation**: Patients and specialists have the ability to cancel appointments with a confirmation prompt.


### Messaging System
HealMate provides a secure messaging system for communication between patients and specialists:
- **Inbox**: Users can view received messages and reply to messages directly from their inbox.
- **Send Message**: Patients can send messages to specialists they have appointments with, and vice versa.
- **Message History**: All sent and received messages are stored and displayed in the user's message history.
- **Real-Time Messaging**: The system is designed to support real-time messaging between users.


### Profile Management
Each user can manage their profile through the dashboard:
- **Patient Profile**: Patients can view and update personal details such as contact information, medical history, and emergency contacts.
- **Specialist Profile**: Specialists can view and update their bio, specialty, location, and upload profile images.
- **Profile Images**: Specialists can upload and update their profile image, which appears on the search results and specialist details page.

### Confirmation Messages
- **User Feedback**: Confirmation messages are shown to users when important actions are performed, such as logging in, booking an appointment, or sending a message. These messages help ensure a smooth user experience by providing feedback on successful actions.

### CRUD Functionality

The following **CRUD** functionalities are implemented within HealMate:

- **Create**: Patients are automatically assigned a profile upon registration. This profile includes key fields such as contact information, address, and medical history.
  
- **Read**: Patients can view their profile and associated information, including medical history and emergency contact details, from their dashboard.

- **Update**: Patients have the ability to update their profile information, including personal data (e.g., contact number, address, and medical history), via a dedicated "Edit Profile" page.

- **Delete (Soft Delete)**: Patients can request to deactivate their account through a **soft delete** mechanism. This deactivation preserves the patient’s data within the system while preventing further access until reactivation by an admin. The admin can reactivate the account from the Django admin panel at any time, restoring full access for the patient.

This CRUD cycle is central to the **PatientProfile** model, ensuring that users can fully manage their personal information while providing system integrity with the soft delete functionality.

-->
## Future Features
<!--
I plan to implement the following in future iterations:
- Push notifications for upcoming appointments.
- Integrate payment system for paid consultations.
-->
## Technologies & Languages Used
- HTML5 - Markup language for structuring the website
- CSS3 - Styling language for designing the layout and visual aesthetics
- JavaScript - For interactivity and DOM manipulation on the frontend
- Python (Django) - Backend web framework for server-side logic and management
- PostgreSQL - Database management system for storing data
- Cloudinary - Cloud-based image storage solution
- Whitenoise - For serving static files directly from Django

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
<!--
### **Validation Testing**

All code has been validated through:
- **HTML**: [W3C Markup Validator](https://validator.w3.org/).
- **CSS**: [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).
- **Python**: PEP8 validation to ensure code quality.

![HTML validator test](docs/project-images/Screenshot%202024-10-04%20164347.png)

![CSS validator test](docs/project-images/Screenshot%202024-10-04%20164642.png)

### **User Testing**

- **Browser Compatibility**: The website has been tested on Chrome, Firefox, Safari, and Edge.
- **Responsiveness**: The platform has been tested on mobile, tablet, and desktop devices to ensure optimal performance.
- **Role-Based Dashboard Testing:** Each user type (patient, specialist, admin) was tested to ensure they were directed to the correct dashboard after login. Patients were assigned to the correct group during registration, and specialists were manually added by admins. The redirection logic was thoroughly tested by registering new users and ensuring role-based access was properly applied.
- **Automatic Assignment Testing:** Tests were conducted to verify that newly registered users are automatically assigned to the "Patient" group and that their PatientProfile was successfully created. This was confirmed through both the user interface and the Django admin panel.

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
<!--
All code for this project was written in Visual Studio/Gitpod as the integrated development environment. GitHub was used for version control, and the application was deployed to Heroku from GitHub.

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

The live link for this project can be found here: <a href="https://healmate-378e458234ec.herokuapp.com/" target="_blank">HealMate</a>

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
    git clone https://github.com/easybulb/healmate
    ```
8. Press Enter to create the local clone.

**Note:** The difference between a clone and a fork is that with a clone, you need permission to push changes to the original repository, whereas a fork creates an entirely new project under your GitHub account.

## Privacy Policy

As part of my **HealMate** project, I am dedicated to ensuring that users’ personal data is handled responsibly. The following privacy practices outline how information is collected, used, and stored within this academic project.

- **Data Collection**: HealMate, as a project, collects personal data during user registration and profile setup. This includes:
  - First and Last Name
  - Contact Information (Phone Number, Email)
  - Date of Birth
  - Gender
  - Medical History
  - Emergency Contact Information

- **Data Usage**: The information gathered is used solely for educational purposes, including:
  - Managing user profiles.
  - Facilitating appointment bookings between patients and specialists.
  - Sending notifications related to appointments or system updates.

- **Data Sharing**: As this is a student project, personal data will not be shared with any third parties. It will only be used for demonstrating the functionality of the project. All information remains confidential and will not be distributed beyond the scope of the HealMate project.

- **Security**: While this project is intended for educational use, I strive to implement best practices for data security using the Django framework’s built-in tools. Personal information is securely stored in the database and protected against unauthorized access.

- **User Rights**: Users of this platform, as part of this project, have the right to request modifications or deletion of their data. For any requests or concerns about personal data usage in this project, please contact the project owner at the provided email address.

Since this is an educational project, the privacy and data handling policies may evolve over time as more features are added and refined.

-->
## Credits
<!--
### Code
- **Django Documentation**: The official docs were invaluable in setting up the project structure and solving specific issues.
- **Django Crispy Forms Documentation**: Used to streamline form rendering.
- **Chatgpt AI**: For images and some coding ideas
- **Favicon.io**: For Favicon generation.
- **Google Fonts**: For typography.
- **Mark Brisco** - Code Institute: For general guidance.
- **Amy Richardson** - Code Institute: General guidance.

### Media
- Icons and images sourced from **Canva** and **ChatGPT**.
- ERD illustration was generated from **pygraphiz** - A django extension.

### Additional reading/tutorials/books/blogs
- **Django for Beginners** by William S. Vincent.
-->
## Acknowledgements
<!--
I would like to extend my heartfelt gratitude to the following individuals and organizations whose support, guidance, and inspiration have been invaluable in the development of this project.

### Mentors and Advisors
- **Amy Richardson** – Sincere gratitude to Amy, our tutor and facilitator, whose unwavering guidance and expertise were pivotal throughout this journey. Her mentorship provided the clarity and support needed to navigate challenges, ultimately elevating the quality of this project. Her dedication and encouragement made a profound impact on my progress and learning.

- **Mark Briscoe** – A heartfelt thank you to Mark, our dedicated tutor, whose unwavering support, insightful feedback, and constructive criticism were instrumental in guiding this project to completion. His depth of knowledge and encouragement not only enhanced my understanding but also inspired me to consistently improve my work. This project would not have been the same without his invaluable mentorship.


### Supportive Friends and Family
- My friends and family, especially, for their encouragement and patience during this project. Your belief in me kept me motivated and focused.

### Academic Institutions
- **Code Institute** – Thank you for providing the learning environment and resources that made this project possible. I am especially grateful to the professors and staff at Code Institute for their valuable insights.

### Final Note
This project would not have been possible without the support, advice, and inspiration of each individual and organization mentioned. Thank you for being a part of this journey.
-->
