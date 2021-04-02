
- Create a `web-svc.yaml` file with following content.

```
cat << EOF > web-svc.yaml
apiVersion: v1
kind: Service   
metadata:
  name: web-flask-svc
  labels:
    app: web-flask
spec:
  type: ClusterIP  
  ports:
  - port: 3000  
    targetPort: 5000
  selector:
    app: web-flask 
EOF
```{{copy}}
  
`kubectl apply -f web-svc.yaml`{{copy}}

- List the services.

`kubectl get svc -o wide`{{copy}}

- Display information about the `web-flask-svc` Service.

`kubectl describe svc web-flask-svc`{{copy}}


- Create a `clarus-db.yaml` file to create a Pod that connects the web-flask page via curl command.

```
cat << EOF > clarus-db.yaml
apiVersion: v1
kind: Pod
metadata:
  name: clarus-db
spec:
  containers:
  - name: clarus-db
    image: clarusway/clarus-db
    imagePullPolicy: IfNotPresent
  restartPolicy: Always
EOF
```{{copy}}

- Create the `clarus-db` pod and log into the container. Connects the web-flask page via curl command and pay attention to load balancig.

`kubectl apply -f clarus-db.yaml`{{copy}}

`kubectl exec -it clarus-db -- sh`{{copy}}

`curl <cluster-ip>:3000`{{copy}}

- To connect web-flask page, we can use service name, in our case it is `web-flask-svc`, instead of cluster ip.

`kubectl exec -it clarus-db -- sh`{{copy}}
`curl web-flask-svc:3000`{{copy}}