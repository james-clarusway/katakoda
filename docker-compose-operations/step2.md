
## docker-compose operation

- Create a file called `docker-compose.yml`.

```text
This Compose file defines two services: web and redis.

### Web service
The web service uses an image that’s built from the Dockerfile in the current directory. It then binds the container and the host machine to the exposed port, 5000. This example service uses the default port for the Flask web server, 5000.

### Redis service
The redis service uses a public Redis image pulled from the Docker Hub registry.
```

`cat << EOF > docker-compose.yml
version: "3"
services:
  web:
    build: .
    ports:
      - "5000:5000"
  redis:
    image: "redis:alpine"
EOF`{{copy}}

- Build and run your app with `Docker Compose`.

```text
Docker compose pulls a Redis image, builds an image for our the app code,
and starts the services defined. In this case, the code is statically copied into the image at build time.
```

`docker-compose up`{{copy}}

- Select port to view on Host1 and select port:5000. Check that, app is running..


- Press `Ctrl+C` to stop containers, and run `docker ps -a` to see containers created by Docker Compose.

`docker ps -a`{{copy}}

- Remove the containers with `Docker Compose`.

`docker-compose down`{{copy}}