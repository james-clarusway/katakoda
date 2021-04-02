- Check the readiness of nodes at the cluster on master node.

`kubectl cluster-info
kubectl get nodes`{{copy}}

## Kubernetes Services

An abstract way to expose an application running on a set of Pods as a network service.
With Kubernetes you don't need to modify your application to use an unfamiliar service discovery mechanism. Kubernetes gives Pods their own IP addresses and a single DNS name for a set of Pods, and can load-balance across them.

- Let's define a setup to observe the behaviour of `services` in Kubernetes and how they work in practice.

- Create `yaml` file named `web-flask.yaml`.

```
cat << EOF > web-flask.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-flask-deploy
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web-flask
  template:
    metadata:
      labels:
        app: web-flask
    spec:
      containers:
      - name: web-flask-pod
        image: clarusways/cw_web_flask1
        ports:
        - containerPort: 5000
EOF
```{{copy}}

- Create the web-flask Deployment.
  
`kubectl apply -f web-flask.yaml`{{copy}}

- Show the Pods detailed information and learn their IP addresses:

`kubectl get pods -o wide`{{copy}}

- We get an output like below.

```text
NAME                                READY   STATUS    RESTARTS   AGE   IP               NODE
web-flask-7cbb5f5967-24smj          1/1     Running   0          15m   172.16.166.175   node1
web-flask-7cbb5f5967-94g6f          1/1     Running   0          15m   172.16.166.177   node1
web-flask-7cbb5f5967-gjtkx          1/1     Running   0          15m   172.16.166.176   node1
```

In the output above, for each Pod the IPs are internal and specific to each instance. If we were to redeploy the application, then each time a new IP will be allocated.

We now check we can ping a Pod inside the cluster.

- Create a `forping.yaml` file to create a Pod that pings a Pod inside the cluster.

```
cat << EOF > forping.yaml
apiVersion: v1
kind: Pod
metadata:
  name: for-ping
spec:
  containers:
  - name: forping
    image: clarusway/forping
    imagePullPolicy: IfNotPresent
  restartPolicy: Always
```{{copy}}

- Create the `forping` pod and log into the container.

`kubectl apply -f forping.yaml
kubectl exec -it forping -- sh
/ # ping <IP of any pod>
`{{copy}}

- Show the Pods detailed information and learn their IP addresses again.

`kubectl get pods -o wide`{{copy}}

- Scale the deployment down to zero.

`kubectl scale deploy web-flask-deploy --replicas=0`{{copy}}

- List the pods again and note that there is no pod in web-flask-deploy.

`kubectl get pods -o wide`{{copy}}

- Scale the deployment up to three replicas.

`kubectl scale deploy web-flask-deploy --replicas=3`{{copy}}

- List the pods again and note that the pods are changed.

`kubectl get pods -o wide`{{copy}}