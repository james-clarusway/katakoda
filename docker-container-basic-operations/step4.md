- Show only running containers and explain the status.

`docker ps`{{copy}}

- Connect to the interactive shell of running `clarus` container and `exit` afterwards.

`docker attach clarus`{{copy}}

- Show that `clarus` container has stopped by listing all containers.

`docker ps -a`{{copy}}

- Restart the first container by its `ID` again and attach to it to show that the file we have created is still there under the home folder, and exit afterwards.

`docker start <ID> && docker attach <ID>`{{copy}}