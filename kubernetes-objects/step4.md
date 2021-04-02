## Deployment Rolling Update and Rollback in Kubernetes

- Create a new folder name it deployment-lesson.

`mkdir deployment-lesson
cd deployment-lesson`{{copy}}

- Create a clarus-deploy.yaml and input text below. Pay attention that image version is 1.0.

```
cat << EOF > clarus-deploy.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: clarus-deploy
  labels:
    app: container-info
  annotations:
    kubernetes.io/change-cause: deploy/clarus-deploy is set as container-info=clarusway/container-info:1.0
spec:
  replicas: 3
  selector:
    matchLabels:
      app: container-info
  template:
    metadata:
      labels:
        app: container-info
    spec:
      containers:
      - name: container-info
        image: clarusway/container-info:1.0
        ports:
        - containerPort: 80
EOF
```{{copy}}

- Create the deployment with `kubectl apply` command.

`kubectl apply -f clarus-deploy.yaml`{{copy}}

- List the `Deployment`, `ReplicaSet` and `Pods` of `clarus-deploy` deployment using a label and note the name of ReplicaSet.

`kubectl get deploy,rs,po -l app=container-info`{{copy}}

- Describe deployment and note the image of the deployment. In our case, it is clarusway/container-info:2.0.

`kubectl describe deploy clarus-deploy`{{copy}}

- View previous rollout revisions.

`kubectl rollout history deploy clarus-deploy`{{copy}}

- Display details with revision number, in our case, is 1. And note name of image.

`kubectl rollout history deploy clarus-deploy --revision=1`{{copy}}

- Upgrade image.

`kubectl set image deploy clarus-deploy container-info=clarusway/container-info:2.0 --record=true`{{copy}}

- Show the rollout history.

`kubectl rollout history deploy clarus-deploy`{{copy}}

- Display details about the revisions.

`kubectl rollout history deploy clarus-deploy --revision=1
kubectl rollout history deploy clarus-deploy --revision=2`{{copy}}

- List the `Deployment`, `ReplicaSet` and `Pods` of `clarus-deploy` deployment using a label and pay attention to ReplicaSets. There are two replicaSets. The number of one is zero and the other one is three.

`kubectl get deploy,rs,po -l app=container-info`{{copy}}

- Upgrade image with kubectl edit commands.

`kubectl edit deploy/clarus-deploy`{{copy}}

- We will see an output like below.

```yaml
# Please edit the object below. Lines beginning with a '#' will be ignored,
# and an empty file will abort the edit. If an error occurs while saving this file will be
# reopened with the relevant failures.
#
apiVersion: apps/v1
kind: Deployment
metadata:
  annotations:
    deployment.kubernetes.io/revision: "2"
    kubectl.kubernetes.io/last-applied-configuration: |
    ...
```

- Change the `metadata.annotations.kubernetes.io/change-cause` and `spec.template.spec.containers.image` fields as below.

```yaml
...
...
    kubernetes.io/change-cause: kubectl set image deploy clarus-deploy container-info=clarusway/container-info:3.0
...
...
    spec:
      containers:
      - image: clarusway/container-info:3.0
...
...
```

- Show the rollout history.

`kubectl rollout history deploy clarus-deploy`{{copy}}

- Display details about the revisions.

`kubectl rollout history deploy clarus-deploy --revision=1
kubectl rollout history deploy clarus-deploy --revision=2
kubectl rollout history deploy clarus-deploy --revision=3`{{copy}}

- List the `Deployment`, `ReplicaSet` and `Pods` of `clarus-deploy` deployment using a label.

`kubectl get deploy,rs,po -l app=container-info`{{copy}}

- Rollback to `revision 1`.

`kubectl rollout undo deploy clarus-deploy --to-revision=1`{{copy}}

- Display the rollout history and note that we have revision 2, 3 and 4. Pay attention that original revision, which is `revision 1`, becomes `revision 4`.

`kubectl rollout history deploy clarus-deploy
kubectl rollout history deploy clarus-deploy --revision=2
kubectl rollout history deploy clarus-deploy --revision=2
kubectl rollout history deploy clarus-deploy --revision=4`{{copy}}

- Try to pull up the `revision 1`, that is no longer available.

`kubectl rollout history deploy clarus-deploy --revision=1`{{copy}}

- List the `Deployment`, `ReplicaSet` and `Pods` of `mynginx` deployment using a label, and see that the original ReplicaSet has been scaled up back to three and second ReplicaSet has been scaled down to zero.

`kubectl get deploy,rs,po -l app=container-info`{{copy}}

- Delete the deployment.

`kubectl delete deploy -l app=container-info`{{copy}}