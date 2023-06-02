FROM python:3.10-alpine
# used with live-reload so .pyc isn't stored on host
ENV PYTHONPYCACHEPREFIX=/tmp
#
RUN adduser -D testapi
USER testapi
ENV PATH="/home/testapi/.local/bin:$PATH"
WORKDIR /test
COPY . .

RUN pip install -r requirements.txt
ENTRYPOINT ["pytest"]
