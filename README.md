# Fitness Tracker Platform

A Django-based web application that allows users to track their fitness activities, monitor progress, and achieve their health goals. The platform includes features for logging workouts, tracking nutrition, and visualizing progress over time.

## Features

- **User Authentication**: Users can register, log in, and log out.
- **Workout Logging**: Users can log their workouts, including exercises, sets, and reps.
- **Nutrition Tracking**: Users can track their daily food intake and nutrition.
- **Progress Visualization**: Users can view their progress over time with charts and graphs.
- **Goal Setting**: Users can set and track fitness goals.
- **Social Sharing**: Users can share their achievements with friends and followers.

## Technology Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: PostgreSQL
- **Other**: Bootstrap (Frontend Framework)

## Getting Started

### Prerequisites

- Python 3.8+
- pip
- virtualenv (optional but recommended)


## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/Alirezz2020/Fitness-Tracker.git
   cd Fitness-Tracker
2. **Set Up a Virtual Environment:**
    ```sh
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
3. **Install Dependencies:**
   ```sh
    pip install -r requirements.txt

4. **Apply Migrations:**
    ```sh
    python manage.py migrate
5. **Create a Superuser:**
    ```sh
   python manage.py createsuperuser
6. **Run the Development Server:**
    ```sh
   python manage.py runserver
7. **Access the Application:**

    Visit http://127.0.0.1:8000/ in your browser to start exploring the platform.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. Make sure to include tests and follow the project’s coding standards.

## License
This project is licensed under the MIT License.

