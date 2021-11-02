FROM python:3.9.5

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install psycopg2
RUN python3 -m pip install --upgrade pip

WORKDIR /home/owerpy/Recipes/
COPY ./requirements.txt /home/owerpy/Recipes/requirements.txt
RUN pip install -r /home/owerpy/Recipes/requirements.txt

COPY . /home/owerpy/Recipes/
