## Labels and loose coupling

- Pods and Services are loosely coupled via labels and label selectors. For a Service to match a set of Pods, and therefore provide stable networking and load-balance, it only needs to match some of the Pods labels. However, for a Pod to match a Service, the Pod must match all of the values in the Service’s label selector.

- Add `version: v1` to `web-svc.yaml --> spec.selector`. So that you end up with:

```
cat << EOF > web-svc.yaml
apiVersion: v1
kind: Service
metadata:
  name: web-flask-svc
  labels:
    app: web-flask
spec:
  type: NodePort
  ports:
  - port: 3000
    nodePort: 30036
    targetPort: 5000
  selector:
    app: web-flask
    version: v1
EOF
```{{copy}}

- Use kubectl apply to push your configuration changes to the cluster.

`kubectl apply -f web-svc.yaml`{{copy}}

- Reload the page, and see that we can not see the page because of that the Service is selecting on two labels, but the Pods only have one of them. The logic behind this is a Boolean `AND` operation.

- Add `version: v1` to `web-flask.yaml --> spec.template.metadata.labels`. So that you end up with:

```
cat << EOF > web-svc.yaml
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
        version: v1
    spec:
      containers:
      - name: web-flask-pod
        image: clarusway/cw_web_flask1
        ports:
        - containerPort: 5000
EOF
```{{copy}}

- Use kubectl apply to push your configuration changes to the cluster.

`kubectl apply -f web-flask.yaml`{{copy}}

- Reload the page again, and now we can see the page because the `Service` is selecting on two labels and the Pods have all of them.

- Add `test: coupling` to `web-flask.yaml --> spec.template.metadata.labels`. So that you end up with:

```
cat << EOF > web-svc.yaml
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
        version: v1
        test: coupling
    spec:
      containers:
      - name: web-flask-pod
        image: clarusway/cw_web_flask1
        ports:
        - containerPort: 5000
EOF
```{{copy}}

- Push your configuration changes to the cluster.

`kubectl apply -f web-flask-development.yaml`{{copy}}

- Reload the page again, and we see the page although the `Pods` have additional labels that the `Service` is not selecting on.