# Python docker template

![Test](https://github.com/PiroHiroPiro/docker_template_python/workflows/Test/badge.svg)
![Code Style](https://github.com/PiroHiroPiro/docker_template_python/workflows/Code%20Style/badge.svg)

This is a template that provides an python environment.

## Requirement

- [Docker](https://www.docker.com/)

## Usage

Run Jupyter notebook:

```shell
$ docker compose up
```

Go to `http://localhost:8888` and you'll see the notebooks.

## Install

Clone repository:

```shell
$ git clone https://github.com/PiroHiroPiro/docker_template_python.git
$ cd docker_template_python
```

Build image:

```shell
$ cp .env.example .env
$ docker compose build
```

Change the configuration file `source/pyproject.toml`.

## Author

[Hiroyuki Nishizawa](https://github.com/PiroHiroPiro)
