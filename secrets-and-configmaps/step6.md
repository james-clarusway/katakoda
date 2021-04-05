### From a config file

- We will write the greeting key-value pair in a file in Norvegian and create the ConfigMap from this file.

`echo "greeting: Hei" > config`{{copy}}

Note that, the comman notation used in key-value pairs is to use `key= value` notation, but this is not an obligatory. The notation actualy depends on the application implementation that will parse and use these files.

- Let's create our configmap from `config` file.

`kubectl create configmap demo-config --from-file=./config`{{copy}}

- Check the content of the `configmap/demo-config`.

`kubectl get  configmap/demo-config -o json`{{copy}}

We have modifed our application to read parameters from the file. So the `deployment` file changed as follows:

```bash
$ cat deployment.yaml 
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
```
Volume and volume mounting are comman ways to place config files inside a container. We are selecting `config` key from `demo-config` ConfigMap and put it inside the container at path `/config/` with the name `demo.yaml`.

Apply and run all the configurations as follow:

```bash
$ kubectl apply -f deployment.yaml 
deployment.apps/demo created
$ kubectl get po
NAME                   READY   STATUS    RESTARTS   AGE
demo-77496d887-rhkww   1/1     Running   0          4s
$ kubectl apply -f service.yaml 
service/demo-service created
$ kubectl get svc -o wide
NAME           TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE   SELECTOR
demo-service   LoadBalancer   10.108.171.92   <pending>     80:32337/TCP   16s   app=demo
kubernetes     ClusterIP      10.96.0.1       <none>        443/TCP        46d   <none>
$ curl < worker-ip >:32337
Hei, Clarusway!
```

- Reset what we have created.

```bash
$ kubectl get cm
NAME          DATA   AGE
demo-config   1      15m
$ kubectl delete cm demo-config 
configmap "demo-config" deleted
$ kubectl delete -f service.yaml
service "demo-service" deleted
$ kubectl delete -f deployment.yaml
deployment.apps "demo" deleted
```

## From a ConfigMap YAML file

This has the same steps and configuration with the `From a config file`

The ConfigMap YAML file
```bash
$ cat configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: demo-config
data:
  config: |
    greeting: Buongiorno
```

Note the greeting message is changed.

```bash
$ cat deployment.yaml
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
```
`Service` is the same.

```bash
$ kubectl apply -f configmap.yaml
configmap/demo-config created
$ kubectl apply -f deployment.yaml 
deployment.apps/demo created
$ kubectl apply -f service.yaml 
service/demo-service created
$ kubectl get po
NAME                   READY   STATUS    RESTARTS   AGE
demo-77496d887-bljb8   1/1     Running   0          12s
$ kubectl get svc -o wide
NAME           TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE   SELECTOR
demo-service   LoadBalancer   10.107.176.127   <pending>     80:30811/TCP   16s   app=demo
kubernetes     ClusterIP      10.96.0.1        <none>        443/TCP        46d   <none>
$ curl < worker-ip >:30811
Buongiorno, Clarusway!
```

- Reset what we have created.
```bash
$ kubectl delete cm demo-config 
configmap "demo-config" deleted
$ kubectl delete -f service.yaml
service "demo-service" deleted
$ kubectl delete -f deployment.yaml
deployment.apps "demo" deleted
```

## Configure all key-value pairs in a ConfigMap as container environment variables

We will update the `configmap.yaml` as follows:

```text
apiVersion: v1
kind: ConfigMap
metadata:
  name: demo-config
data:
  greeting: Hola
```

We will update the `deployment.yaml` as follows:

```text
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
          env:
            - name: GREETING
              valueFrom:
                configMapKeyRef:
                  name: demo-config
                  key: greeting
```

Note that this time, we are not placing the `GREETING` as run arguments. This time we will inject this variable as `environment variable`.

```bash
$ kubectl apply -f k8s
configmap/demo-config created
deployment.apps/demo created
service/demo-service created

$ kubectl get svc
NAME           TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
demo-service   LoadBalancer   10.104.115.11   <pending>     80:31577/TCP   42s
kubernetes     ClusterIP      10.96.0.1       <none>        443/TCP        46d

$ curl < worker-ip >:31577
Hola, Clarusway!
```

- Reset what we have created.

```bash
$ kubectl delete -f k8s
configmap "demo-config" deleted
deployment.apps "demo" deleted
service "demo-service" deleted
```

## Configure all key-value pairs in a ConfigMap as container environment variables in POSIX format

- In case if you are using envFrom  instead of env  to create environmental variables in the container, the environmental names will be created from the ConfigMap's keys. If a ConfigMap  key has invalid environment variable name, it will be skipped but the pod will be allowed to start. 

- POSIX variables consist solely of uppercase letters, digits, and the '_' (underscore) from the characters defined in Portable Character Set and do not begin with a digit.

Modify configmap.yaml file:

```text
apiVersion: v1
kind: ConfigMap
metadata:
  name: demo-config
data:
  GREETING: Merhaba
```

The environmental variables are directly filled in `configmap.yaml`. They are in capital letters.

- `deployment.yaml` file:

```text
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
```

Note the change as follows:

```text
...
          envFrom:
          - configMapRef:
              name: demo-config
```

- You can compare with the previos `deployment.yaml` file.

```bash
$ kubectl apply -f k8s
configmap/demo-config created
deployment.apps/demo created
service/demo-service created
```

```bash
$ kubectl get svc
NAME           TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
demo-service   LoadBalancer   10.110.195.109   <pending>     80:32711/TCP   17s
kubernetes     ClusterIP      10.96.0.1        <none>        443/TCP        46d

$ curl < worker-ip >:32711
Merhaba, Clarusway!
```

Everything works fine!

```bash
$ kubectl delete -f k8s
configmap "demo-config" deleted
deployment.apps "demo" deleted
service "demo-service" deleted
```