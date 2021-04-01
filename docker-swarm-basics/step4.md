## Global mod

- Create service in `global mod`.

`docker service create --name glbserver --mode=global -p 80:80 nginx`{{copy}}

- Remove a container and pay attention that swarm creates a new task immediately.

`docker container ls`{{copy}}
`docker container rm -f <containerid>`{{copy}}
`docker service ps glbserver`{{copy}}

- Remove the `glbserver` service.

`docker service rm glbserver`{{copy}}