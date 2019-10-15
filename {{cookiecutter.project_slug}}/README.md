# {{cookiecutter.project_name}}

## Run

```
python application.py
```

## Docker

**build**

```
docker build -t {{cookiecutter.project_slug}}:0.0.1 . 
```

**run**

```
docker run --rm -it {{cookiecutter.project_slug}}:0.0.1 application.py
```

## Testing

```
pytest --doctest-modules --rootdir=tests --cov-config=tests/.coveragerc --cov={{cookiecutter.project_slug}} tests/
```
