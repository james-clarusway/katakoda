## Updating and Rolling Back in Docker Swarm

- Create a new service of `clarusway/container-info:1.0` with 10 replicas.

`docker service create --name clarusweb -p 80:80 --replicas=10 clarusway/container-info:1.0`{{copy}}

- Inspect the `docker service update` command.

`docker service update --help`{{copy}}

- Update `clarusway/container-info:1.0` image with `clarusway/container-info:2.0` image.

`docker service update --detach --update-delay 5s --update-parallelism 2 --image clarusway/container-info:2.0 clarusweb`{{copy}}
`watch docker service ps clarusweb`{{copy}}

- Revert back to the earlier state of `clarusweb` service and monitor the changes.

`docker service rollback --detach clarusweb`{{copy}}
`watch docker service ps clarusweb`{{copy}}

 - Remove the service.

`docker service rm clarusweb`{{copy}}