FROM python:3.9 as build-python

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

FROM python:3.9-slim

RUN groupadd -r core && useradd -r -g core core

RUN apt-get update \
  && apt-get install -y \
  postgresql-client \
  postgresql-client-common \
  libcairo2 \
  libgdk-pixbuf2.0-0 \
  liblcms2-2 \
  libopenjp2-7 \
  libpango-1.0-0 \
  libpangocairo-1.0-0 \
  libssl1.1 \
  libtiff5 \
  libwebp6 \
  libxml2 \
  libpq5 \
  shared-mime-info \
  mime-support \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /app/media/media  \
  && chown -R core:core /app/  

COPY --from=build-python /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/
COPY --from=build-python /usr/local/bin/ /usr/local/bin/
COPY . /app
WORKDIR /app

RUN SECRET_KEY=6w9z$C@FaJ@McQfTjWnZr4u7x@A%D*G-6w9z$C@FaJ@McQfTjWnZr4u7x@A%D*G-6w9z$C@FaJ@McQfTjWnZr4u7x@A%D*G- STATIC_URL= ${STATIC_URL} python3 manage.py collectstatic --no-input

EXPOSE 8000
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ARG COMMIT_ID
ARG PROJECT_VERSION
ENV PROJECT_VERSION="${PROJECT_VERSION}"

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "--worker-class", "gevent", "--worker-connections", "500" "core.wsgi:application"]
