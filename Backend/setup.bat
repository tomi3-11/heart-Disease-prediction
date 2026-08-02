@echo off

python -m venv .venv

call .venv\Scripts\activate

python -m pip install --upgrade pip

pip install -r requirements.txt

echo.
echo Setup complete.
echo.
echo Activate the environment:
echo .venv\Scripts\activate
echo.
echo Then run:
echo uvicorn app.main:app --reload
