- Expose the nginx-server pod as a new Kubernetes service on master.

`kubectl expose pod nginx-server --port=80 --type=NodePort`{{copy}}

- Get the list of services and show the newly created service of `nginx-server`

`kubectl get service -o wide`{{copy}}

- You will get an output like this.

```bash
kubernetes     ClusterIP   10.96.0.1       <none>        443/TCP        13m    <none>
nginx-server   NodePort    10.110.144.60   <none>        80:32276/TCP   113s   run=nginx-server
```

- Select port to view on Host1 and select port [NodePort] (in this case it is 32276). Check that, nginx server is running.

- Clean the service and pod from the cluster.

`kubectl delete service nginx-server
kubectl delete pods nginx-server`{{copy}}

- Check there is no pod left.

`kubectl get pods`{{copy}}