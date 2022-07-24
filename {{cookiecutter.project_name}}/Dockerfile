FROM python:{{cookiecutter.min_python_version}}

USER root:root

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -qqy git build-essential unixodbc-dev ssh wget &&\
    apt-get clean

RUN groupadd -g 1000 {{cookiecutter.user_name}} && \
    useradd -g 1000 -u 1000 --system --create-home {{cookiecutter.user_name}}

RUN pip install poetry \
    && poetry config virtualenvs.in-project true

USER {{cookiecutter.user_name}}

RUN poetry config virtualenvs.in-project true

WORKDIR /code
