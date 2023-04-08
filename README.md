# CookieCutterD3V

FullFeatuered CookieCutter template
Supporting most of useful technologies

## Which technologies we used?
### Prometheus
This template uses prometheus for monitoring requests, models, etc.

### Multiple api frameworks
This template uses multiple api frameworks like:
1. Django rest framework
2. Django grpc framework
3. Graphene django
And if the none of above choosed, it will use the basic html features

### Project documentions with sphinx
This template uses sphinx for project documention. eg: development, production, about, todos and etc.

### Api documentions with drf_spectacular
This template uses drf-spectacular for documenting apis

### more technologies
This template support more technologies like:
1. Celery
2. Django Channels
3. Django debug toolbar
4. Pytest
5. Persian django configuration
6. Docker
7. Jwt
8. And more...

## How to use it ?

### Installing cookiecutter

At first, you should install cookiecutter on your operation system

As the cookiecutter docs explained you can install cookiecutter by using pip with the command below:

```python3 -m pip install --user cookiecutter```

### Get template by cookiecutter

Then you should pass my template to cookiecutter:

```cookiecutter https://github.com/MohammadD3veloper/CookieCutterD3V```

### Answering cookiecutter questions

Now answer cookiecutter questions as desired
After answering questions, your project will be ready

### declaring Environment variable for Django debug:
Cause of usage of the debug variable before env initialization, template needs the debug variable from environment and you can set it in linux os with the command below:

```export DJANGO_DEBUG=true```

The value of this variable can be true/false

### Running tests

This template has a sample test, for ensure it is working as well, you can run command below in the root of project:

```pytest```

### Running makemigrations & migrate

```python manage.py makemigrations```

```python manage.py migrate```

### Creating Superuser

```python manage.py createsuperuser```

It will ask you a username & password like the default django UserManager
After fill the creation form, it will create the superuser and you can access the admin panel url or documentation url


## thanks !
Thank you of using this template
If you like it. Just give a star

## License
This template is under GPL3 License
Designed with ❤️ by MohammadD3veloper
