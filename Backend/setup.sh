#!/usr/bin/env bash

set -e

echo "Creating virtual environment..."
python3 -m venv .venv

echo "Activating virtual environment..."
source .venv/bin/activate

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing dependencies..."
pip install -r requirements.txt

echo
echo "Setup complete."
echo
echo "Next steps:"
echo "1. Copy .env.example to .env"
echo "2. Configure DATABASE_URL"
echo "3. Start PostgreSQL"
echo "4. Run:"
echo "   source .venv/bin/activate"
echo "   uvicorn app.main:app --reload"
