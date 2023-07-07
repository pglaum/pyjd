FROM python:3-alpine

RUN mkdir /pyjd
WORKDIR /pyjd

COPY .docker/pytest-entrypoint.sh /usr/local/bin/docker-entrypoint
RUN chmod +x /usr/local/bin/docker-entrypoint

ENTRYPOINT [ "docker-entrypoint" ]
CMD pytest
