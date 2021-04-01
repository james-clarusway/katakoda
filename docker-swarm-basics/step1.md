## Set up a Swarm Cluster with Manager and Worker Node

- Firstly we create a Docker swarm cluster that is composed of one manager node and one worker node. 

- Initialize `docker swarm` on host-1.

`docker swarm init`{{copy}}

- You get an output as below.

```bash
Swarm initialized: current node (6gpbx6r9vxwp37hjcdi41bhuc) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-4yfmqmk2xvly7mczdi21cuuhmem34v4ytrnvvkhzfajlptp4rk-dkfxxv4bq48rxomjjsjoxo5f1 172.31.9.149:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.
```

- Copy the `docker swarm join --token` command and paste on host-2.

- Check if the `docker swarm` is active on host-1. Note that swarm part of `docker info` is active.

`docker info` {{copy}}

- List the connected nodes in `Swarm`.

`docker node ls`{{copy}}