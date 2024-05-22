# Gestion de alumnos escuela magica - Black Clover

## Presentacion

Cabe mencionar que este proyecto se ha realizado con el boilerplate - [![Christian](https://github.com/Jebux01/boilerplate-fastapi)]
El boilerplate es de mi auditoria y es de uso libre

### Technology
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)  
[![Build Status](https://img.shields.io/badge/build-develop-pass.svg)](https://shields.io/)
[![Coverage](https://img.shields.io/badge/coverage-process-blue.svg)](https://shields.io/)
[![Testing](https://img.shields.io/badge/testing-process-blue.svg)](https://shields.io/)


install dependencies
```
pyenv virtualenv template
pyenv activate template
pip3 install -r requirements.txt
pip3 install pre-commit
pre-commit install
```

Run pre-commit checks
```
pre-commit run --all-files
```

Run unit tests
```
pytest --cov -v
coverage html   (genera reporte html)
```

Run checks
```
flake8 .
black .    (formatea código)
```

---


## Uso Docker

### Iniciar proyecto
```sh
docker-compose up --build
```

### Terminar proyecto
```sh
docker-compose down
```

## Acceso a los servicios

### Backend
#### Documentacion
```sh
http://localhost:8000/docs
```

#### App React Ts
```sh
http://localhost:3000
```