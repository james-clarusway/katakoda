- Check the readiness of nodes at the cluster on master node.

`kubectl cluster-info
kubectl get nodes`{{copy}}

## Kubernetes Volume Persistence

-On node01, create a `pv-data` directory under home folder, also create an `index.html` file with `Welcome to Kubernetes persistence volume lesson` text and note down path of the `pv-data` folder.

`mkdir pv-data && cd pv-data`{{copy}}
`echo "Welcome to Kubernetes persistence volume lesson" > index.html`{{copy}}

- On controlplane, create a `clarus-pv.yaml` file using the following content with the volume type of `hostPath` to build a `PersistentVolume`.

```
cat << EOF > clarus-pv.yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: clarus-pv-vol
  labels:
    type: local
spec:
  storageClassName: manual
  capacity:
    storage: 5Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/home/ubuntu/pv-data"
EOF
```{{copy}}

- Create the PersistentVolume `clarus-pv-vol`.

`kubectl apply -f clarus-pv.yaml`{{copy}}

- View information about the `PersistentVolume` and notice that the `PersistentVolume` has a `STATUS` of available which means it has not been bound yet to a `PersistentVolumeClaim`.

`kubectl get pv clarus-pv-vol`{{copy}}

- Create a `clarus-pv-claim.yaml` file using the following content to create a `PersistentVolumeClaim`.

```
cat << EOF > clarus-pv-claim.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: clarus-pv-claim
spec:
  storageClassName: manual
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
EOF
```{{copy}}

- Create the PersistentVolumeClaim `clarus-pv-claim`.

`kubectl apply -f clarus-pv-claim.yaml`{{copy}}

> After we create the PersistentVolumeClaim, the Kubernetes control plane looks for a PersistentVolume that satisfies the claim's requirements. If the control plane finds a suitable `PersistentVolume` with the same `StorageClass`, it binds the claim to the volume. Look for details at [Persistent Volumes and Claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#introduction)

- View information about the `PersistentVolumeClaim` and note that the `PersistentVolumeClaim` is bound to your PersistentVolume `clarus-pv-vol`.

`kubectl get pvc clarus-pv-claim`{{copy}}

- View information about the `PersistentVolume` and pay attention that the PersistentVolume `STATUS` changed from Available to `Bound`.

`kubectl get pv clarus-pv-vol`{{copy}}