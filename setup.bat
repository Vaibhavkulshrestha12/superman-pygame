@echo off
echo Setting up Superman Game environment...
echo.

echo Creating virtual environment...
python -m venv .venv

echo.
echo Activating virtual environment...
call .venv\Scripts\activate

echo.
echo Installing requirements...
pip install -r requirements.txt

echo.
echo Setup complete! You can now run the game with:
echo   run_game.bat
echo.
echo Or manually with:
echo   .venv\Scripts\activate
echo   python run.py
pause