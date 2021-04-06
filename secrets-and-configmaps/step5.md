We have modified the application to take the greeting message as a parameter (environmental variable). So we will expose configuration data into the container’s environmental variables.

Now, we will create `ConfigMap` and use the `greeting` key-value pair as in the `deployment.yaml` file.

The modified `deployment.yaml` file.

```
cat << EOF > deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: demo
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
        - name:  demo
          image: clarusway/demo:hello-config-args
          imagePullPolicy: Always
          args:
            - '-greeting'
            - '$(GREETING)'
          ports:
            - containerPort: 8888
          env:
            - name: GREETING
              valueFrom:
                configMapKeyRef:
                  name: demo-config
                  key: greeting
EOF
```{{copy}}
Note the application run parameter (`args`) and `ConfigMap` reference in container section.

## Create and use ConfigMaps with kubectl create configmap command

There are three ways to create ConfigMaps using the `kubectl create configmap` command. Here are the options.

1. Use the contents of an entire directory with `kubectl create configmap my-config --from-file=./my/dir/path/`
   
2. Use the contents of a file or specific set of files with `kubectl create configmap my-config --from-file=./my/file.txt`
   
3. Use literal key-value pairs defined on the command line with `kubectl create configmap my-config --from-literal=key1=value1 --from-literal=key2=value2`

### Literal key-value pairs

We will start with the third option. We have just one parameter. Greet with "Halo" in Spanish.

`kubectl create configmap demo-config --from-literal=greeting=Halo`{{copy}}

- Let's see the `ConfigMap` file contents.

`kubectl get configmap/demo-config -o yaml`{{copy}}

- Apply `kubectl` to these files.

`kubectl apply -f deployment.yaml`{{copy}}  

`kubectl apply -f  service.yaml`{{copy}}

- List the services.

`kubectl get svc -o wide`{{copy}}

- See the message.

`curl localhost:<nodePort>`{{copy}}

- The output is like below.

`Halo, Clarusway!`{{copy}}

- Reset what we have created.

`kubectl get cm`

`kubectl delete cm demo-config`{{copy}}

`kubectl delete -f service.yaml`{{copy}}

`kubectl delete -f deployment.yaml`{{copy}}