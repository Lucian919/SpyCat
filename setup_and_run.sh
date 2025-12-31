#!/bin/bash
# filepath: django-project/setup_and_run.sh

# Exit immediately if a command exits with a non-zero status
set -e

echo "Setting up the Django project..."

# Step 1: Create a virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
else
    echo "Virtual environment already exists."
fi

# Step 2: Activate the virtual environment
echo "Activating virtual environment..."

if [[ "$OSTYPE" == "msys"* || "$OSTYPE" == "cygwin"* ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi
# Step 3: Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Step 4: Apply database migrations
echo "Applying database migrations..."
python manage.py makemigrations
python manage.py migrate

# Step 5: Start the Django development server
echo "Starting the Django development server..."
python manage.py runserver