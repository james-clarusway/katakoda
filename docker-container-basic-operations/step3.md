- Run the second `ubuntu` os with interactive shell open and name container as `clarus` and show that this `ubuntu` container is different from the previous one.

`docker run -i -t --name clarus ubuntu`{{copy}}

- Exit the `ubuntu` container and return to ec2-user bash shell.

`exit`{{copy}}

- Show the list of all containers again and explain the second `ubuntu` containers' properties and how the names of containers are given.

`docker ps -a`{{copy}}

- Restart the first container by its `ID`.

`docker start <ID>`{{copy}}

- Show only running containers and explain the status.

`docker ps`{{copy}}

- Stop the first container by its `ID` and show it is stopped.

`docker stop <ID> && docker ps -a`{{copy}}

- Restart the `clarus` container by its name and list only running containers.

`docker start clarus && docker ps`{{copy}}