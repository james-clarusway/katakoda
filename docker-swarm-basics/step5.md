## Updating and Rolling Back in Docker Swarm

- Create a new service of `clarusway/container-info:1.0` with 10 replicas.

`docker service create --name clarusweb -p 80:80 --replicas=10 clarusway/container-info:1.0`{{copy}}

- Select port to view on Host1 and select port:80. Check that, the `clarusweb` is running. Pay attention to version of Container Info is 1.0.

- Update `clarusway/container-info:1.0` image with `clarusway/container-info:2.0` image.

`docker service update --detach --update-delay 5s --update-parallelism 2 --image clarusway/container-info:2.0 clarusweb`{{copy}}
`watch docker service ps clarusweb`{{copy}}

- Select port to view on Host1 and select port:80. Check that, the `clarusweb` is running. Pay attention to version of Container Info is 2.0 now.

- Revert back to the earlier state of `clarusweb` service and monitor the changes.

`docker service rollback --detach clarusweb`{{copy}}
`watch docker service ps clarusweb`{{copy}}

- Select port to view on Host1 and select port:80 again. Check that, the `clarusweb` is running. Pay attention to version of Container Info is 1.0 now.

 - Remove the service.

`docker service rm clarusweb`{{copy}}