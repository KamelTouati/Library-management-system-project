# Library-management-system-project

# Description
The Library Management System is a website application designed to manage the operations and activities of a library. This system provides a convenient way to organize and track books.
## Features
Book Management: Add, update, and delete books from the library. Keep track of book details such as title, author, publication date, and availability status.

Reservation System: Allow members to reserve books that are currently unavailable. Automatically notify members when the reserved books become available.

Search and Filtering: Provide a search functionality to find books by title. Implement filtering options to narrow down the search results based on various criteria.

## Screenshots

![website interface0](screenshots/screencapture-127-0-0-1-8000-2023-06-14-19_18_49.png)
![website interface0](screenshots/screencapture-127-0-0-1-8000-2023-06-14-19_19_37.png)
![website interface0](screenshots/screencapture-127-0-0-1-8000-books-2023-06-14-19_20_20.png)
![website interface0](screenshots/screencapture-127-0-0-1-8000-delete-44-2023-06-14-19_20_47.png)
![website interface0](screenshots/screencapture-127-0-0-1-8000-update-44-2023-06-14-19_20_36.png)


### Installation

1. Clone the repository: `git clone https://github.com/KamelTouati/Library-management-system-project`
2. Navigate to the project directory: `cd LibManagSysEnv`
3. Create and activate a virtual environment (optional but recommended):
   - For Windows (using Command Prompt):
     ```
     python -m venv venv
     venv\Scripts\activate
     ```
   - For macOS/Linux:
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```
4. Install the required packages: `pip install django`
5. Perform database migrations:
    ```
    python manage.py migrate
    ```
6. Create a superuser:
    ```
    python manage.py createsuperuser
    ```
7. Start the development server:
    ```
    python manage.py runserver
    ```
8. Open your web browser and visit `http://localhost:8000` to access the application.



## Technologies Used
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"><img class="ml-4 w-8 h-8 sm:w-10 sm:h-10" src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40">

## Contributions

Contributions are welcome! If you have any ideas or suggestions, feel free to open an issue or submit a pull request.

## Contact Information

For any questions or feedback, please contact [kamel touati](mailto:kameltouati19.work@gmail.com).