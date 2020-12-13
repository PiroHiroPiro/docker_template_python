# Python docker template

This is a template that provides an python environment.

## Requirement

- [Docker](https://www.docker.com/)
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
$ git clone https://github.com/PiroHiroPiro/docker_template_python.git
$ cd docker_template_python
```

Build image:

```console
$ cp .env.example .env
$ docker-compose build
```

## Licence

This software is released under the MIT License, see [LICENSE](https://github.com/PiroHiroPiro/docker_template_python/blob/master/LICENSE).

## Author

[Hiroyuki Nishizawa](https://github.com/PiroHiroPiro)
