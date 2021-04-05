## From a ConfigMap YAML file

This has the same steps and configuration with the `From a config file`

The ConfigMap YAML file

```
cat << EOF > configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: demo-config
data:
  config: |
    greeting: Buongiorno
EOF
```{{copy}}

Note the greeting message is changed.

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
          image: clarusways/demo:hello-config-file
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

`Service` is the same.

`kubectl apply -f configmap.yaml`{{copy}}

`kubectl apply -f deployment.yaml`{{copy}}

`kubectl apply -f service.yaml`{{copy}}

`kubectl get po`{{copy}}

`kubectl get svc -o wide`{{copy}}

`curl localhost:<nodePort>`{{copy}}

The output:
```
Buongiorno, Clarusway!
```

- Reset what we have created.

`kubectl delete cm demo-config`{{copy}}

`kubectl delete -f service.yaml`{{copy}}

`kubectl delete -f deployment.yaml`{{copy}}