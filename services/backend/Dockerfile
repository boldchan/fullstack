FROM python:3.10-slim

WORKDIR /code

ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt ./
RUN set -eux
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt
RUN rm -rf /root/.cache/pip

# for migrations
COPY migrations .
COPY pyproject.toml .

COPY ./src ./src