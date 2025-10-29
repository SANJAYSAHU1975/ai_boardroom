#!/bin/bash
# AI Boardroom Startup Script

echo "🎯 Starting AI Boardroom..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "⚠️  Please edit .env file with your configuration"
fi

# Initialize database
echo "Initializing database..."
python -c "from app import app, db; app.app_context().push(); db.create_all(); print('Database initialized!')"

# Run tests only if TEST_ON_STARTUP is set
if [ "$TEST_ON_STARTUP" = "true" ]; then
    echo "Running tests..."
    python -m unittest test_app.py
fi

# Start the application
echo "🚀 Starting Flask application..."
echo "Access the application at http://localhost:5000"
python app.py
