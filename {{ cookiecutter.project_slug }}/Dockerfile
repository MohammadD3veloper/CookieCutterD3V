FROM python:3.10

ENV PYTHONUNBUFFERED 1

ENV PYTHONDONTWRITEBYTECODE 1

ENV Environment=/app/{{ cookiecutter.project_slug }}

RUN mkdir -p ${Environment}

WORKDIR ${Environment}

COPY . ${Environment}

RUN  pip install --upgrade pip

RUN pip install -r requirements/local.txt

CMD python manage.py runserver 0.0.0.0:8000
