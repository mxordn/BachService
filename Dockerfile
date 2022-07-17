FROM python:3.10-slim

WORKDIR /usr/src

RUN set -ex \
    && buildDeps=' \
        gcc \
        libbz2-dev \
        libc6-dev \
        libgdbm-dev \
        liblzma-dev \
        libncurses-dev \
        libreadline-dev \
        libsqlite3-dev \
        libssl-dev \
        libpcre3-dev \
        make \
        tcl-dev \
        tk-dev \
        wget \
        xz-utils \
        zlib1g-dev \
    ' \
    && deps=' \
        libexpat1 \
    ' \
    && apt-get update && apt-get install -y $buildDeps $deps --no-install-recommends  && rm -rf /var/lib/apt/lists/* \
    && pip install uwsgi \
    && apt-get purge -y --auto-remove $buildDeps \
    && find /usr/local -depth \
    \( \
        \( -type d -a -name test -o -name tests \) \
        -o \
        \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
    \) -exec rm -rf '{}' +


COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./app ./app
COPY ./app/static/bwv.sqlite ./app/static/bwv.sqlite
COPY ./start_bwv_service.ini ./start_bwv_service.ini
COPY ./start_bwv_service.py ./start_bwv_service.py
EXPOSE 8005

CMD ["uwsgi", "start_bwv_service.ini"]