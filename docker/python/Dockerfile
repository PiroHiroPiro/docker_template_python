FROM python:3.6

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src

COPY ./Pipfile  ./
COPY ./Pipfile.lock ./

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system --dev

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root"]
