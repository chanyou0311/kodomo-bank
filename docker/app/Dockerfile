FROM python:3.6.9

RUN mkdir /code/
ADD ./ /code/
WORKDIR /code

RUN pip install --upgrade pip && \
  pip install pipenv && \
  pipenv --python /usr/local/bin/python
RUN pipenv install --dev && \
  apt-get update && \
  apt-get install -y mariadb-client
