FROM python:3.6

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src

COPY ./Pipfile  ./
COPY ./Pipfile.lock ./

RUN pip install pipenv \
 && pipenv install --system --dev

RUN eval "$(pipenv --completion)"

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root"]
