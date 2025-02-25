FROM python:3.12-slim

ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV PYTHONIOENCODING=UTF-8
ENV APP_HOME=/app

WORKDIR $APP_HOME
COPY . .

RUN pip install -r requirements.txt

RUN chmod +x entrypoint.sh
CMD  [ "/bin/sh", "entrypoint.sh"]