- Show that we can get more information about `clarus` container by using `docker inspect` command and explain the properties.

`docker inspect clarus | less`{{copy}}

- Delete the first container using its `ID`.

`docker rm <ID>`{{copy}}

- Delete the second container using its name.

`docker rm clarus`{{copy}}

- Show that both of containers are not listed anymore.