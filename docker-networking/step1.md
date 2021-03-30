## default bridge network

- List all networks available in Docker.

`docker network ls`{{copy}}

- Run two `alpine` containers with interactive shell, in detached mode, name the container as `clarus1st` and `clarus2nd`, and add command to run alpine shell.

`docker run -dit --name clarus1st alpine ash
docker run -dit --name clarus2nd alpine ash`{{copy}}

- Show the list of running containers on Docker machine.

`docker ps`{{copy}}

- Show the details of bridge network, and explain properties (subnet, ips) and why containers are in the default network bridge.

`docker network inspect bridge | less`{{copy}}

- Get the IP of clarus2nd container.

`docker inspect clarus2nd |grep IPAddress`{{copy}}

- Connect to the clarus1st container.

`docker attach clarus1st`{{copy}}

- Ping google.com four times to check internet connection.

`ping -c 4 google.com`{{copy}}

- Ping `clarus2nd `container by its IP four times to show the connection.

`ping -c 4 <clarus2nd-ip>`{{copy}}


- Try to ping `clarus2nd `container by its name, should face with bad address. Because, containers on the default bridge network can only access each other by IP addresses. 

`ping -c 4 clarus2nd`{{copy}}

- Stop and delete the containers

`
docker stop clarus1st clarus2nd
docker rm clarus1st clarus2nd
`{{copy}}