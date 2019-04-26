# Python + Pipenv + CircleCI Docker template

This is a Docker template that provides an environment with Python, Pipenv and CircleCI.

## Requirement

- [docker](https://www.docker.com/)
  - docker-compose

## Usage

Run Jupyter notebook:

```console
$ docker-compose up
```

Go to `http://localhost:8888` and you'll see the notebooks.

## Install

Clone repository:

```console
$ git clone https://github.com/PiroHiroPiro/docker_template_python_pipenv_circleci.git
$ cd docker_template_python_pipenv_circleci
```

Build image:

```console
$ cp .env.example .env
$ docker-compose build
```

## Licence

This software is released under the MIT License, see [LICENSE](https://github.com/PiroHiroPiro/docker_template_python_pipenv_circleci/blob/master/LICENSE).

## Author

[Hiroyuki Nishizawa](https://github.com/PiroHiroPiro)
