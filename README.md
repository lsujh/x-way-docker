# Описание проекта
### Стек технологий
- Python, Django, DjangoRestFramework.
- PostgreSQL, RabbitMQ, Celery.

---------
# Cloning & Run:
- sudo apt-get update
- sudo apt-get upgrade 
- PACKAGES=“python3.8 python3-pip python3-venv rabbitmq-server gettext”
- sudo apt-get -y –force-yes install $PACKAGES 

### Get the code
- git clone https://github.com/lsujh/x-way-docker.git
- cd x-way-docker/x-way

### Install geckodriver for Firefox
- wget https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-linux64.tar.gz
- tar -xvzf geckodriver-v0.29.1-linux64.tar.gz
- sudo mv geckodriver /usr/local/bin/geckodriver
- sudo chown root:root /usr/local/bin/geckodriver
- sudo chmod +x /usr/local/bin/geckodriver

### Virtualenv modules installation (Unix based systems)
- python -m venv venv
- source venv/bin/activate

### Install modules
- pip install -r requirements.txt
- Edit file .env with settings database

### Create tables
- python3 manage.py migrate

### Start the application (development mode)
- python manage.py runserver # default port 8000

### Start the app - custom port
- python manage.py runserver 0.0.0.0:<your_port>

### Access the web app in browser: http://127.0.0.1:8000/

###Start management script
- python manage.py parser_placeholder

### Start Celery
- celery -A core worker -B -l INFO
