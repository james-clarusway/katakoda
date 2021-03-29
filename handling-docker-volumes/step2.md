Let's run an alpine image and this time we will create try1 folder instead of sample folder.

`docker container run -it -v firstvolume:/try1 alpine sh`
`ls`
`try1`
`ls`
`cat file1.txt`{{copy}}

As we see, we can reach file1.txt via a new container.

We can add a new file to the try1 folder.

`touch file2.txt`
`echo "this is added in second container" >> file2.txt`
`cat file2.txt`{{copy}}

Let's create an ubuntu image.

`docker container run -it -v firstvolume:/try2 ubuntu sh`
`ls`
`cd try2`
`ls`{{copy}}

As we see above, We can use the same volumes with different containers.