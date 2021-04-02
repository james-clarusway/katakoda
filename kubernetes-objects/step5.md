## Namespaces in Kubernetes

- List the current namespaces in a cluster using and explain them. *Kubernetes supports multiple virtual clusters backed by the same physical cluster. These virtual clusters are called `namespaces`.

`kubectl get namespace`{{copy}}

>### default
>The default namespace for objects with no other namespace

>### kube-system
>The namespace for objects created by the Kubernetes system

>### kube-public
>This namespace is created automatically and is readable by all users (including those not authenticated). This >namespace is mostly reserved for cluster usage, in case that some resources should be visible and readable >publicly throughout the whole cluster. The public aspect of this namespace is only a convention, not a >requirement.

>### kube-node-lease
>This namespace for the lease objects associated with each node which improves the performance of the node  heartbeats as the cluster scales.

- Create a new YAML file called `my-namespace.yaml` with the following content.

`cat << EOF > my-namespace.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: clarus-namespace
EOF`{{copy}}

- Create a namespace using the `my-namespace.yaml` file.

`kubectl apply -f ./my-namespace.yaml`{{copy}}

- Alternatively, you can create namespace using below command:

`kubectl create namespace <namespace-name>`{{copy}}

- Create pods in each namespace.

`kubectl create deployment default-ns --image=nginx`{{copy}}

`kubectl create deployment clarus-ns --image=nginx  -n=clarus-namespace`{{copy}}

- List the deployments in `default` namespace.

`kubectl get deployment`{{copy}}

- List the deployments in `clarus-namespace`.

`kubectl get deployment -n clarus-namespace`{{copy}}

- List the all deployments.

`kubectl get deployment -o wide --all-namespaces`{{copy}}

- Delete the namespace.

`kubectl delete namespaces clarus-namespace`{{copy}}