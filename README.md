# SpyCat Django Project

This project is a Django-based API for managing missions, cats, and targets. Follow the instructions below to set up the project, run the server, and test the API.

## Prerequisites
Before running the project, ensure you have the following installed:

Python 3.8 or higher
- pip (Python package manager)
- Virtual environment tools (venv)
- Bash shell (for running the setup script)
- Initial Setup and Running the Server

To simplify the setup process, a shell script (**setup_and_run.sh**) is provided. Follow these steps:

## Navigate to the Project Directory:
Open a terminal and navigate to the django-project directory:

## Run the Setup Script:
Execute the **setup_and_run.sh** script to set up the project and start the development server:

This script will:

- Create and activate a virtual environment.
- Install all required dependencies from requirements.txt.
- Apply database migrations.
- Start the Django development server.
- Access the Development Server:
- Once the server is running, you can access the API at:

## Testing the API
To test the API, you can use the provided Postman collection. Follow these steps:

## Import the Postman Collection:
Use the following link to import the Postman collection into your Postman workspace:
[SpyCat Postman Collection](https://www.postman.com/joint-operations-candidate-67313575/workspace/catspy/collection/36510858-84d09cc4-2f6c-4667-b3e4-1789e7a5bdc3?action=share&creator=36510858)

## Run API Requests:

## Open Postman and navigate to the imported collection.
Use the available endpoints to interact with the API.
To easily configure request use Postman Collection variables (cat_id, mission_id, targe_id)

Notes
Ensure the virtual environment is activated before running any Django commands manually:
If you encounter any issues, check the terminal output for error messages.
To stop the server, press Ctrl+C in the terminal where the server is running.