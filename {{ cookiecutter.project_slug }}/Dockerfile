FROM python:3.10

ENV Environment={{ cookiecutter.project_slug }}

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN mkdir ${Environment}

COPY . ${Environment}

WORKDIR ${Environment}

RUN pip install --upgrade pip

RUN pip install -r requirements/local.txt

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000
