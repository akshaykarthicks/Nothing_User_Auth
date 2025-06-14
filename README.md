# Django User Authentication System

A  Nothing  os style robust user authentication system built with Django, featuring user registration, login, and secure session management. 
# User Registration 
![image](https://github.com/user-attachments/assets/0accb687-46ca-4b41-8718-f8a360e8a4fb)

# Login page
![image](https://github.com/user-attachments/assets/f3195c70-55de-4f52-a7a6-1fa41c38466e)

## Features

- User Registration
- User Login/Logout
- Secure Password Management
- Session Management
- User Profile Management

## Prerequisites

- Python 3.x
- Django 4.x
- SQLite (included with Django)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Django_USER_AUTH
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

```
Django_USER_AUTH/
├── Login/                  # Main project directory
│   ├── Login/             # Project configuration
│   ├── Register/          # User registration app
│   ├── templates/         # HTML templates
│   └── manage.py          # Django management script
└── README.md
```

## Running the Project

1. Make migrations:
```bash
python manage.py makemigrations
```

2. Apply migrations:
```bash
python manage.py migrate
```

3. Run the development server:
```bash
python manage.py runserver
```

4. Access the application at `http://127.0.0.1:8000/`

## Usage

1. Register a new account at `/register/`
2. Login with your credentials at `/login/`
3. Access your profile and manage your account

## Security Features

- Password hashing
- CSRF protection
- Session management
- Secure form handling

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the repository or contact the maintainers. 
