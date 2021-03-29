## Use a read-only volume

For some development applications, the container needs to write into the bind mount so that changes are propagated back to the Docker host. At other times, the container only needs read access to the data. Remember that multiple containers can mount the same volume, and it can be mounted read-write for some of them and read-only for others, at the same time.

`docker container run -it -v firstvolume:/try3:ro centos sh`{{copy}}

`ls`{{copy}}

`cd try3`{{copy}}

`ls`{{copy}}  

Let's try to add a file to the volume.

`touch file3`{{copy}}

As we see above, We can not create a file.