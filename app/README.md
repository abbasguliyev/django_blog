# django_blog

- Configuration
    1. create .env file in app and main folders
    2. Copy and paste the contents of the env file into the .env file 
- Start without docker
    2. python manage.py migrate
    3. python manage.py createsuperuser
    4. python manage.py runserver
- Start with docker
    2. docker-compose build
    3. docker-compose run --rm web python3 manage.py migrate
    4. docker-compose run --rm web python3 manage.py createsuperuser
    5. docker-compose up
