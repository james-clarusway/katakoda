## Deployments

- Create yaml file named `mydeployment.yaml`.

```
cat << EOF > mydeployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    environment: dev
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.19
        ports:
        - containerPort: 80
EOF
```{{copy}}

- Create the deployment with `kubectl apply` command.
  
`kubectl apply -f mydeployment.yaml`{{copy}}

- List the deployments.

`kubectl get deployments`{{copy}}

- List pods with more information.
  
`kubectl get pods -o wide`{{copy}}

- Show details of deployments.

`kubectl describe deploy/nginx-deployment`{{copy}}

- Print the logs for a container in a pod.

`kubectl logs <pod-name>`{{copy}}

- If there is a multi-container pod, we can print logs of one container.

```bash
kubectl logs <pod-name> -c <container-name>
```

- Execute a command in a container.

`kubectl exec <pod-name> -- date`{{copy}}

`kubectl exec <pod-name> -- cat /usr/share/nginx/html/index.html`{{copy}}

- Open a bash shell in a container.

`kubectl exec -it <pod-name> -- bash`{{copy}}

- List the ReplicaSets.

`kubectl get rs`{{copy}}

- Show details of ReplicaSets.

`kubectl describe rs <rs-name>`{{copy}}

- Scale the deployment up to five replicas.

`kubectl scale deploy nginx-deployment --replicas=5`{{copy}}

- Delete a pod and pay attention that new pod is immediately created.

`kubectl delete pod <pod-name>`{{copy}}

`kubectl get pods`{{copy}}

- Delete deployments

`kubectl delete deploy <deployment-name>`{{copy}}