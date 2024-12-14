# django_blog

- Configuration
    - create .env file in app folder
    - Copy and paste the contents of the .env.example file into the .env file 
- Start without docker
    - python manage.py migrate
    - python manage.py createsuperuser
    - python manage.py runserver
- Start with docker
    - docker-compose build
    - docker-compose run --rm web python3 manage.py migrate
    - docker-compose run --rm web python3 manage.py createsuperuser
    - docker-compose up
