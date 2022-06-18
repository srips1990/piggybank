call "%cd%\.venv\Scripts\activate.bat"
python manage.py collectstatic
python manage.py runserver
pause