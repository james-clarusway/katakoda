## Building Docker Images

- Create a Dockerfile.

`vim Dockerfile`{{copy}}
  
  
### Dockerfile:
`FROM ubuntu
LABEL maintainer="clarusway@example.com"
RUN apt-get update && apt-get install -y nginx
EXPOSE 80`{{copy}}

- Build Docker image.

`docker build -t="clarusway" .`{{copy}}
`docker image ls`{{copy}}