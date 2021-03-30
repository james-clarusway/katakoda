
## User-defined Network Bridge in Docker

- Create a bridge network `clarusnet`.

`docker network create --driver bridge clarusnet`{{copy}}

- List all networks available in Docker, and show the user-defined `clarusnet`.

`docker network ls`{{copy}}

- Show the details of `clarusnet`, and show that there is no container yet.

`docker network inspect clarusnet`{{copy}}

- Run four `alpine` containers with interactive shell, in detached mode, name the containers as `clarus1st`, `clarus2nd`, `clarus3rd` and `clarus4th`, and add command to run alpine shell. Here, 1st and 2nd containers should be in `clarusnet`, 3rd container should be in default network bridge, 4th container should be in both `clarusnet` and default network bridge.

`docker run -dit --network clarusnet --name clarus1st alpine ash
docker run -dit --network clarusnet --name clarus2nd alpine ash
docker run -dit --name clarus3rd alpine ash
docker run -dit --name clarus4th alpine ash
docker network connect clarusnet clarus4th`{{copy}}

- List all running containers and show there up and running.

`docker container ls`{{copy}}

- Show the details of `clarusnet`, and explain newly added containers. (1st, 2nd, and 4th containers should be in the list)

`docker network inspect clarusnet`{{copy}}

- Show the details of  default network bridge, and pay attention to newly added containers. (3rd and 4th containers should be in the list)

`docker network inspect bridge`{{copy}}

- Connect to the `clarus1st` container.

`docker attach clarus1st`{{copy}}

- Ping `clarus2nd` and `clarus4th` container by its name to show that in user-defined network, container names can be used in networking.

`ping -c 4 clarus2nd
ping -c 4 clarus4th`{{copy}}

- Try to ping `clarus3rd` container by its name and IP, should face with bad address because 3rd container is in different network.

`ping -c 4 clarus3rd`{{copy}}
`ping -c 4 172.17.0.2`{{copy}}

- Ping google.com to check internet connection.

```bash
ping -c 4 google.com
```

- Exit the `clarus1st` container without stopping. (CTRL + p + q)

- Connect to the `clarus4th` container, since it is in both network should connect all containers.

`docker attach clarus4th`{{copy}}

- Ping `clarus2nd` and `clarus4th` container by its name, ping `clarus3rd` container with its IP.

`ping -c 4 clarus1st
ping -c 4 clarus2nd
ping -c 4 172.17.0.2`{{copy}}

- Stop and remove all containers

`
docker stop clarus1st clarus2nd clarus3rd clarus4th
docker rm clarus1st clarus2nd clarus3rd clarus4th
`{{copy}}

- Delete clarusnet network

`docker network rm clarusnet`{{copy}}