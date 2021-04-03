## Using pvc in pod

- Create a `clarus-pod.yaml` file that uses your PersistentVolumeClaim as a volume using the following content.

```
cat << EOF > clarus-pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: clarus-pod
  labels:
    app: clarus-web 
spec:
  volumes:
    - name: clarus-pv-storage
      persistentVolumeClaim:
        claimName: clarus-pv-claim
  containers:
    - name: clarus-pv-container
      image: nginx
      ports:
        - containerPort: 80
          name: "http-server"
      volumeMounts:
        - mountPath: "/usr/share/nginx/html"
          name: clarus-pv-storage
EOF
```{{copy}}

- Create the Pod `clarus-pod`.

`kubectl apply -f clarus-pod.yaml`{{copy}}

- Verify that the Pod is running.

`kubectl get pod clarus-pod`{{copy}}

- Open a shell to the container running in your Pod.

`kubectl exec -it clarus-pod -- /bin/bash`{{copy}}

- Verify that `nginx` is serving the `index.html` file from the `hostPath` volume.

`curl http://localhost/`{{copy}}

- On node01 change the `index.html`.

`cd pv-data`{{copy}}

`echo "Kubernetes Rocks!!!!" > index.html`{{copy}}

- On controlplane, check if the change is in effect.

`kubectl exec -it clarus-pod -- /bin/bash`{{copy}}

`curl http://localhost/`{{copy}}

- Expose the clarus-pod pod as a new Kubernetes service on master.

`kubectl expose pod clarus-pod --port=80 --type=NodePort`{{copy}}

- List the services.

- Select port to view on Host1 and select port:`<node-port>`. Check that, clarus-pod is running.

`kubectl get svc`{{copy}}

- Delete the `Pod`, the `PersistentVolumeClaim` and the `PersistentVolume`.

```
kubectl delete pod clarus-pod
kubectl delete pvc clarus-pv-claim
kubectl delete pv clarus-pv-vol
```{{copy}}