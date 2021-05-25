FROM python:3.8-alpine as builder

WORKDIR /usr/src/x-way

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN wget https://bootstrap.pypa.io/get-pip.py
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN apk --no-cache add \
    # Pillow dependencies
    freetype-dev fribidi-dev harfbuzz-dev jpeg-dev lcms2-dev openjpeg-dev \
    tcl-dev tiff-dev tk-dev zlib-dev jpeg libjpeg-turbo-dev libjpeg

# install geckodriver and firefox
RUN apk add firefox
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-linux64.tar.gz && \
     tar -xvzf geckodriver-v0.29.1-linux64.tar.gz && \
     mv geckodriver /usr/local/bin/geckodriver && \
     chown root:root /usr/local/bin/geckodriver && \
     chmod +x /usr/local/bin/geckodriver && \
     rm geckodriver-v0.29.1-linux64.tar.gz

RUN pip install --upgrade pip setuptools wheel

COPY . .

COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/x-way/wheels -r requirements.txt

# FINAL #
FROM python:3.8-alpine
RUN mkdir -p /home/x-way
RUN addgroup -S ihor && adduser -S ihor -G ihor

ENV HOME=/home/x-way
ENV APP_HOME=/home/x-way/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
RUN mkdir $APP_HOME/media
RUN mkdir $APP_HOME/media/photos
WORKDIR $APP_HOME

RUN apk update && apk add libpq
COPY --from=builder /usr/src/x-way/wheels /wheels
COPY --from=builder /usr/src/x-way/requirements.txt .
RUN pip install --upgrade pip --no-cache /wheels/*

COPY . $APP_HOME

RUN chown -R ihor:ihor $APP_HOME

USER ihor
