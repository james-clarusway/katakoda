### From a config file

- We will write the greeting key-value pair in a file in Norvegian and create the ConfigMap from this file.

`echo "greeting: Hei" > config`{{copy}}

Note that, the comman notation used in key-value pairs is to use `key= value` notation, but this is not an obligatory. The notation actualy depends on the application implementation that will parse and use these files.

- Let's create our configmap from `config` file.

`kubectl create configmap demo-config --from-file=./config`{{copy}}

- Check the content of the `configmap/demo-config`.

`kubectl get  configmap/demo-config -o json`{{copy}}

We have modifed our application to read parameters from the file. So the `deployment` file changed as follows:

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
          image: clarusway/demo:hello-config-file
          ports:
            - containerPort: 8888
          volumeMounts:
          - mountPath: /config/
            name: demo-config-volume
            readOnly: true
      volumes:
      - name: demo-config-volume
        configMap:
          name: demo-config
          items:
          - key: config
            path: demo.yaml
EOF
```{{copy}}

Volume and volume mounting are comman ways to place config files inside a container. We are selecting `config` key from `demo-config` ConfigMap and put it inside the container at path `/config/` with the name `demo.yaml`.

Apply and run all the configurations as follow:

`kubectl apply -f deployment.yaml`{{copy}}

`kubectl get po`{{copy}}

`kubectl apply -f service.yaml`{{copy}}

`kubectl get svc -o wide`{{copy}}

`curl localhost:<nodePort>`{{copy}}

The output:

```
Hei, Clarusway!
```

- Reset what we have created.

`kubectl get cm`{{copy}}

`kubectl delete cm demo-config`{{copy}}

`kubectl delete -f service.yaml`{{copy}}

`kubectl delete -f deployment.yaml`{{copy}}