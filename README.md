# Python + Pipenv + Docker + CircleCI Template
## on local
### set up
```
$ cp .env.example .env
$ vim .env
$ pip install pipenv
$ pipenv install --dev
```

### run
```
$ cp .env.example .env
$ vim .env
$ pipenv shell
$ python APP.PY
```

## on docker container
### set up
```
$ docker-compose build
```

### run jupyter notebook
```
$ docker-compose up
```

### run bash
after `run jupyter notebook`, start up at another terminal
```
$ docker ps
$ docker exec -it [CONTAINER ID] /bin/bash
```

## lint
```
$ pipenv run pylint
$ pipenv run flake
```
