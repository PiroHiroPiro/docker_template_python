# Python docker template

![Test](https://github.com/PiroHiroPiro/docker_template_python/workflows/Test/badge.svg)
![Code Style](https://github.com/PiroHiroPiro/docker_template_python/workflows/Code%20Style/badge.svg)

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

Change the configuration file `source/pyproject.toml`.

## Licence

This software is released under the MIT License, see [LICENSE](https://github.com/PiroHiroPiro/docker_template_python/blob/master/LICENSE).

## Author

[Hiroyuki Nishizawa](https://github.com/PiroHiroPiro)
