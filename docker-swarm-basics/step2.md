## Managing Docker Swarm Services

- Start a `nginx service` with 5 replicas.

`docker service create --name webserver --replicas=5 -p 80:80 -d nginx`{{copy}}

- List services.

`docker service ls`{{copy}}

- Select port to view on Host1 and select port:80. Check that, the `Nginx Web Server` is running.

- Display detailed information on service.

`docker service inspect --pretty webserver`{{copy}}

- List the tasks of service.

`docker service ps webserver`{{copy}}

- Fetch the logs of the service or a task.

```bash
docker service logs webserver
```