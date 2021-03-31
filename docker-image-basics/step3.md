- Run the newly built image as container in detached mode.

`docker run -d -p 80 --name mycontainer clarusway nginx -g "daemon off;"`{{copy}}
`docker ps`{{copy}}

- Stop and remove the container `mycontainer`.

`docker stop mycontainer
docker rm mycontainer`{{copy}}

- Delete image with `image id` locally.

`docker image rm <imageId>`{{copy}}
