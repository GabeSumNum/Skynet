# Snowflake SQLAlchemy builds numpy and doesn't work on Alpine
FROM python:3.10-bullseye AS fastapi

# used with live-reload so .pyc isn't stored on host
ENV PYTHONPYCACHEPREFIX=/tmp

#
RUN useradd -m -U fastapi
ENV PATH="/home/fastapi/.local/bin:$PATH"

WORKDIR /app
EXPOSE 5000
COPY . .

RUN chown -R fastapi:fastapi /app
RUN chmod 755 /app
USER fastapi

RUN pip install -r requirements.txt
ENTRYPOINT ["/bin/bash", "-c", "/app/start_api.sh"]
