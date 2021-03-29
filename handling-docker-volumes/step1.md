
Volumes are created and managed by Docker. You can create a volume explicitly using the `docker volume create` command.

`docker volume create firstvolume`{{copy}}

When you create a volume, it is stored within a directory on the Docker host. When you mount the volume into a container, this directory is what is mounted into the container. Look at the Mountpoint.

`docker volume inspect firstvolume`{{copy}}

## Declaration of volumes

Volumes can be declared on the command-line, with the --volume or -v  flag for docker run. Let's create an alpine container.

`docker container run -it -v firstvolume:/sample alpine sh`{{copy}}

<div class="alert alert-block alert-info">
    <b>💡Tip: 
</b>
    <ul>-v or --volume: Consists of three fields, separated by colon characters (:). The fields must be in the correct order.
       <li>the first field is the name of the volume, and is unique on a given host machine. In this example volume name is firstvolume.</li>
       <li>The second field is the path where the file or directory are mounted in the container. In this example folder in container is /sample.</li>
       <li>The third field is optional, and is a comma-separated list of options, such as ro (read only).</li>
    </ul>
</div>

When we type ls command in alpine terminal, we can see the sample folder.

`docker container run -it -v firstvolume:/sample alpine sh`{{copy}} 


We create a file in the sample folder and exit.

`ls`{{copy}} 
`cd sample`{{copy}} 
`echo "this is added in first container" >> file1.txt`{{copy}} 
`exit`{{copy}} 

Let's remove the alpine container.

`docker container ls -a`{{copy}} 
`docker container rm <ContainerId>`{{copy}} 

Let's check the file1.txt.

`docker volume inspect firstvolume`{{copy}}
`cd /var/lib/docker/volumes/firstvolume/_data`{{copy}}
`cat file1.txt`{{copy}}

As we see above, file1.txt is still there even if we remove the container.