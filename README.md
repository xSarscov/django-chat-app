# Django Chat App

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

This is a real-time chat application built using Django and Channels, allowing users to join rooms and chat with others instantly. The project focuses on practicing websockets in Django and does not handle user authentication; instead, it stores rooms and messages.

## Dependencies
- ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
- ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) Channels
- Daphne
- Channels
- ![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

## Installation and Setup
1. Clone this repository to your local machine:
   ```
   git clone https://github.com/xSarscov/django-chat-app.git
   ```
2. Change your current directory to the cloned repository:
   ```
   cd django-chat-app
   ```
3. Activate your virtual environment using Pipenv:
   ```
   pipenv shell
   ```
4. Install the required dependencies:
   ```
   pipenv install
   ```
5. Apply database migrations:
   ```
   python manage.py migrate
   ```
6. Run the Django development server:
   ```
   python manage.py runserver
   ```
7. Open your web browser and visit http://localhost:8000 to use the chat application.

---

![preview](https://github.com/xSarscov/django-chat-app/assets/110932159/084c8f82-3e09-4b46-b102-ffdb4b75dbb2)

---

## Usage
- Upon visiting the application, users can create a new room by providing their username and the room name, or they can choose to join an existing room.
- The application does not validate user existence but ensures that room names are unique when creating a new room.
- Once in the chat page, users can see all existing rooms and join them to chat with other users in real-time.

## Project Structure
- `core/`: Contains Django app files for managing rooms and messages.
- `templates/`: Contains HTML templates for the user interface.
- `static/`: Contains static files such as CSS and JavaScript for frontend functionality.
- `Pipfile` and `Pipfile.lock`: Manage project dependencies using Pipenv.
- `requirements.txt`: Alternative file for managing dependencies, useful for other virtual environments.

## Development Notes
- Websockets are implemented using Django Channels for real-time communication.
- The application does not handle user authentication; it focuses solely on the chat functionality.
- Ensure that the required dependencies are installed and the virtual environment is activated before running the application.
