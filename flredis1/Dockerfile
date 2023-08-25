# syntax=docker/dockerfile:1.4
FROM python:alpine 
# AS builder

WORKDIR /code

COPY requirements.txt /code
RUN  pip3 install -r requirements.txt

# --mount=type=cache,target=/root/.cache/pip \
#   pip3 install -r requirements.txt

COPY . /code

ENTRYPOINT ["python3"]
CMD ["app.py"]

# FROM builder as dev-envs

# RUN apk update && \
#     apk add git bash

# RUN addgroup -S docker \
#     adduser -S --shell /bin/bash --ingroup docker vscode

# # install Docker tools (cli, buildx, compose)
# COPY --from=gloursdocker/docker / /
