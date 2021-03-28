- Download and run `ubuntu` os with interactive shell open.

`docker run -i -t ubuntu`{{copy}}

- Display the os name on the container for the current user.

`cat /etc/os-release`{{copy}}

- Display the shell name on the container for the current user.

`echo $0`{{copy}}

- Update and upgrade os packages on `ubuntu` container.

`apt-get update && apt-get upgrade -y`{{copy}}

- Show that `ubuntu` container is like any other Ubuntu system but limited.

  - Go to the home folder and create a file named as `myfile.txt`

    `cd ~ && touch myfile.txt && ls`{{copy}}

  - Try to edit `myfile.txt` file with `vim` editor and show that there is no `vim` installed.

    `vim myfile.txt`{{copy}}

  - Install `vim` editor.

    `apt-get install vim`{{copy}}

  - Edit `myfile.txt` file with `vim` editor and type `Hello from the Ubuntu Container` to show that `vim` command can be run now.

    `vim myfile.txt`{{copy}}

- Exit the `ubuntu` container and return to ec2-user bash shell.

`exit`{{copy}}

- Show the list of all containers available on Docker machine and explain container properties.

`docker ps -a`{{copy}}