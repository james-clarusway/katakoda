## Endpoints

As Pods come-and-go (scaling up and down, failures, rolling updates etc.), the Service dynamically updates its list of Pods. It does this through a combination of the label selector and a construct called an Endpoint object.

Each Service that is created automatically gets an associated Endpoint object. This Endpoint object is a dynamic list of all of the Pods that match the Service’s label selector.

Kubernetes is constantly evaluating the Service’s label selector against the current list of Pods in the cluster. Any new Pods that match the selector get added to the Endpoint object, and any Pods that disappear get removed. This ensures the Service is kept up-to-date as Pods come and go.

- List the Endpoints.

`kubectl get ep -o wide`{{copy}}

- Scale the deployment up to ten replicas and list the `Endpoints`.

`kubectl scale deploy web-flask-deploy --replicas=10`{{copy}}

- List the `Endpoints` and see that the Service has an associated `Endpoint` object with an always-up-to-date list of Pods matching the label selector.

`kubectl get ep -o wide`{{copy}}