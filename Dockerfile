FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install Pillow
RUN pip install django-tempus-dominus
RUN pip install django-widget-tweaks
COPY . /app

CMD python manage.py runserver 0.0.0.0:8000