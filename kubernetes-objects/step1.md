## pods

- Create yaml file named `mypod.yaml`.

```
echo '
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  labels:
    app: nginx
spec:
  containers:
  - name: mynginx
    image: nginx:1.19
    ports:
    - containerPort: 80
'> mypod.yaml
```{{copy}}

- Create a pod with `kubectl create` command.

`kubectl create -f mypod.yaml`{{copy}}

- List the pods.

`kubectl get pods`{{copy}}

- List pods in `ps output format` with more information (such as node name).
  
`kubectl get pods -o wide`{{copy}}

- Show details of pod.

`kubectl describe pods/nginx-pod`{{copy}}

- Show details of pod in `yaml format`.
  
`kubectl get pods/nginx-pod -o yaml`{{copy}}

- Delete the pod.

`kubectl delete -f mypod.yaml`{{copy}}

# or

`kubectl delete pod nginx-pod`{{copy}}