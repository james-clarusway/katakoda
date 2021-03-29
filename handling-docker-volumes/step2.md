Let's run an alpine image and this time we will create try1 folder instead of sample folder.

`docker container run -it -v firstvolume:/try1 alpine sh`{{copy}}

`ls`{{copy}}

`try1`{{copy}}

`ls`{{copy}}

`cat file1.txt`{{copy}}

As we see, we can reach file1.txt via a new container.

We can add a new file to the try1 folder.

`touch file2.txt`{{copy}}

`echo "this is added in second container" >> file2.txt`{{copy}}

`cat file2.txt`{{copy}}

Let's create an ubuntu image.

`docker container run -it -v firstvolume:/try2 ubuntu sh`{{copy}}

`ls`{{copy}}

`cd try2`{{copy}}

`ls`{{copy}}

As we see above, We can use the same volumes with different containers.