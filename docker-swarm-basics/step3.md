
## Scale up and down services

- Scale up services.

`docker service scale webserver=10`{{copy}}

- Scale down services.

`docker service scale webserver=3`{{copy}}

- Remove service.

`docker service rm webserver`{{copy}}

## Global mod

- Create service in `global mod`.

```bash
docker service create --name glbserver --mode=global -p 80:80 nginx
```

- Remove a container and pay attention that swarm creates a new task immediately.

`docker container ls`{{copy}}
`docker container rm -f <containerid>`{{copy}}
`docker service ps glbserver`{{copy}}

- Remove the `glbserver` service.

`docker service rm glbserver`{{copy}}