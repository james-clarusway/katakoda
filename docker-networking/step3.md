
## Container Networking

- Run a `nginx` web server, name the container as `ng`, and bind the web server to host port 8080 command to run alpine shell. Explain `--rm` and `-p` flags and port binding.

`docker run --rm -d -p 8080:80 --name ng nginx`{{copy}}

- Select port to view on Host1 and select port:8080. Check that, nginx server is running.

- Stop container `ng`, must be removed automatically due to `--rm` flag.

`docker stop ng`{{copy}}
