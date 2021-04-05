- Check the readiness of nodes at the cluster on master node.

`kubectl cluster-info
kubectl get nodes`{{copy}}

## Kubernetes Secrets

A Secret is an object that contains a small amount of sensitive data such as a password, a token, or a key. Storing confidential information in a Secret is more secure and flexible than putting it verbatim in a Pod definition or in a container image.

### Creating your own Secrets 

#### Creating a Secret Using kubectl

Secrets can contain user credentials required by Pods to access a database. For example, a database connection string consists of a username and password. You can store the username in a file ./username.txt and the password in a file ./password.txt on your local machine.

`# Create files needed for the rest of the example.`

```
echo -n 'admin' > ./username.txt
echo -n '1f2d1e2e67df' > ./password.txt
```{{copy}}

The kubectl create secret command packages these files into a Secret and creates the object on the API server. The name of a Secret object must be a valid DNS subdomain name.

`kubectl create secret generic db-user-pass --from-file=./username.txt --from-file=./password.txt`{{copy}}

Default key name is the filename. You may optionally set the key name using `[--from-file=[key=]source]`.

```
kubectl create secret generic db-user-pass --from-file=username=./username.txt --from-file=password=./password.txt
```

>Note:
>Special characters such as `$`, `\`, `*`, `=`, and `!` will be interpreted by your shell and require escaping. In most shells, the easiest way to escape the password is to surround it with single quotes (`'`). For example, if your actual password is S!B\*d$zDsb=, you should execute the command this way:
>
>```
>kubectl create secret generic dev-db-secret --from-literal=username=devuser --from-literal=password='S!B\*d$zDsb='
>```
>You do not need to escape special characters in passwords from files (--from-file).

You can check that the secret was created:

`kubectl get secrets`{{copy}}

You can view a description of the secret:

`kubectl describe secrets/db-user-pass`{{copy}}

Note: The commands kubectl get and kubectl describe avoid showing the contents of a secret by default. This is to protect the secret from being exposed accidentally to an onlooker, or from being stored in a terminal log.