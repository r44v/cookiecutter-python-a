FROM python:3.7-slim-buster

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
COPY requirements /code/requirements
RUN pip install --upgrade pip && pip install -r requirements.txt && rm -rf ~/.cache/pip/*

COPY {{cookiecutter.package_name}} /code/{{cookiecutter.package_name}}
COPY application.py /code/

ENTRYPOINT ["/bin/bash", "-c"]
CMD [ "python /code/application.py" ]