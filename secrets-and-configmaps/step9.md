## Configure all key-value pairs in a ConfigMap as container environment variables in POSIX format

- In case if you are using envFrom  instead of env  to create environmental variables in the container, the environmental names will be created from the ConfigMap's keys. If a ConfigMap  key has invalid environment variable name, it will be skipped but the pod will be allowed to start. 

- POSIX variables consist solely of uppercase letters, digits, and the '_' (underscore) from the characters defined in Portable Character Set and do not begin with a digit.

Modify configmap.yaml file:

```
cat << EOF > configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: demo-config
data:
  GREETING: Merhaba
EOF
```{{copy}}

The environmental variables are directly filled in `configmap.yaml`. They are in capital letters.

- `deployment.yaml` file:

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
          image: clarusways/demo:hello-config-env
          ports:
            - containerPort: 8888
          envFrom:
          - configMapRef:
              name: demo-config
EOF
```{{copy}}

Note the change as follows:

```bash
...
          envFrom:
          - configMapRef:
              name: demo-config
```

- You can compare with the previos `deployment.yaml` file.

`kubectl apply -f .`{{copy}}

`kubectl get svc`{{copy}}

`curl localhost:<nodePort>`{{copy}}

The output:

```
Merhaba, Clarusway!
```

Everything works fine!

`kubectl delete -f .`{{copy}}