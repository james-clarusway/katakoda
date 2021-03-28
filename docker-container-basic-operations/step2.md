- Download and run `ubuntu` os with interactive shell open.

`docker run -i -t ubuntu`{{copy}}

- Display the os name on the container for the current user.

```bash
cat /etc/os-release
```

- Display the shell name on the container for the current user.

```bash
echo $0
```

- Update and upgrade os packages on `ubuntu` container.

```bash
apt-get update && apt-get upgrade -y
```

- Show that `ubuntu` container is like any other Ubuntu system but limited.

  - Go to the home folder and create a file named as `myfile.txt`

    ```bash
    cd ~ && touch myfile.txt && ls
    ```

  - Try to edit `myfile.txt` file with `vim` editor and show that there is no `vim` installed.

    ```bash
    vim myfile.txt
    ```

  - Install `vim` editor.

    ```bash
    apt-get install vim
    ```

  - Edit `myfile.txt` file with `vim` editor and type `Hello from the Ubuntu Container` to show that `vim` command can be run now.

    ```bash
    vim myfile.txt
    ```

- Exit the `ubuntu` container and return to ec2-user bash shell.

```bash
exit
```

- Show the list of all containers available on Docker machine and explain container properties.

```bash
docker ps -a
```

- Run the second `ubuntu` os with interactive shell open and name container as `clarus` and show that this `ubuntu` container is different from the previous one.

```bash
docker run -i -t --name clarus ubuntu
```

- Exit the `ubuntu` container and return to ec2-user bash shell.

```bash
exit
```

- Show the list of all containers again and explain the second `ubuntu` containers' properties and how the names of containers are given.

```bash
docker ps -a
```

- Restart the first container by its `ID`.

```bash
docker start 4e6
```

- Show only running containers and explain the status.

```bash
docker ps
```

- Stop the first container by its `ID` and show it is stopped.

```bash
docker stop 4e6 && docker ps -a
```

- Restart the `clarus` container by its name and list only running containers.

```bash
docker start clarus && docker ps
```

- Connect to the interactive shell of running `clarus` container and `exit` afterwards.

```bash
docker attach clarus
```

- Show that `clarus` container has stopped by listing all containers.

```bash
docker ps -a
```

- Restart the first container by its `ID` again and attach to it to show that the file we have created is still there under the home folder, and exit afterwards.

```bash
docker start 4e6 && docker attach 4e6
```

- Show that we can get more information about `clarus` container by using `docker inspect` command and explain the properties.

```bash
docker inspect clarus | less
```

- Delete the first container using its `ID`.

```bash
docker rm 4e6
```

- Delete the second container using its name.

```bash
docker rm clarus
```

- Show that both of containers are not listed anymore.

```bash
docker ps -a
```
