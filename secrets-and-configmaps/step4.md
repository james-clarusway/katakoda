## ConfigMaps in Kubernetes

A ConfigMap is a dictionary of configuration settings. This dictionary consists of key-value pairs of strings. Kubernetes provides these values to your containers. Like with other dictionaries (maps, hashes, ...) the key lets you get and set the configuration value.

- A ConfigMap stores configuration settings for your code. Store connection strings, public credentials, hostnames, environment variables, container command line arguments and URLs in your ConfigMap.

- ConfigMaps bind configuration files, command-line arguments, environment variables, port numbers, and other configuration artifacts to your Pods' containers and system components at runtime.

- ConfigMaps allow you to separate your configurations from your Pods and components. 

- ConfigMap helps to makes configurations easier to change and manage, and prevents hardcoding configuration data to Pod specifications.

- ConfigMaps are useful for storing and sharing non-sensitive, unencrypted configuration information.

For the show case we will select a simple application that displays a message like this.

```text
Hello, Clarusway!
```

We will parametrized the "Hello" portion in some languages.

```
cat << EOF > deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: demo
  labels:
    app: demo
spec:
  replicas: 1
  selector:
    matchLabels:
      app: demo
  template:
    metadata:
      labels:
        app: demo
    spec:
      containers:
        - name: demo
          image: clarusway/demo:hello
          ports:
          - containerPort: 8888
EOF
```{{copy}}

- service.yaml

```
cat << EOF > service.yaml
apiVersion: v1
kind: Service
metadata:
  name: demo-service
  labels:
    app: demo
spec:
  type: LoadBalancer
  ports:
  - port: 80
    targetPort: 8888
  selector:
    app: demo
EOF
```{{copy}}

- See the files and go upper folder.

`ls
cd ..`{{copy}}

- Now apply `kubectl` to these files.

`kubectl apply -f .`{{copy}}

Let's see the message.

`kubectl get svc demo-service -o wide`{{copy}}

`curl localhost:<nodePort>`{{copy}}

The output is like below.

`Hello, Clarusway!`


This is the default container behaviour.

Now delete what we have created.

`kubectl delete -f .`{{copy}}