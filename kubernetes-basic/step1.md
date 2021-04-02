- Check the readiness of nodes at the cluster on master node.

`kubectl get nodes`{{copy}}

- Show the list of existing pods. Since we haven't created any pods, list should be empty.

`kubectl get pods`{{copy}}

- Create and run a simple `Nginx` Server image in a pod on master.

`kubectl run nginx-server --image=nginx  --port=80`{{copy}}

- Get the list of pods on master and check the status and readiness of `nginx-server`

`kubectl get pods -o wide`{{copy}}