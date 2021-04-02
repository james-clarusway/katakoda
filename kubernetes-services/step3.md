## NodePort

- Change the service type of web-flask-svc service to NodePort to use the Node IP and a static port to expose the service outside the cluster. So we get the yaml file below.

```
cat << EOF > web-svc.yaml
apiVersion: v1
kind: Service   
metadata:
  name: web-flask-svc
  labels:
    app: web-flask
spec:
  type: NodePort  # We change here
  ports:
  - port: 3000  
    targetPort: 5000
  selector:
    app: web-flask
EOF
```{{copy}}

- Configure the web-flask-svc service via apply command.

`kubectl apply -f web-svc.yaml`{{copy}}

- List the services again. Note that kubernetes exposes the service in a random port within the range 30000-32767 using the Node’s primary IP address.

`kubectl get svc -o wide`{{copy}}

- Select port to view on Host1 and select port:`<node-port>`. Refresh the page and pay attention to load balancing.

- We can also define NodePort via adding nodePort number to service yaml file. Check the below. 

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
    nodePort: 30036       # We add here
    targetPort: 5000
  selector:
    app: web-flask 
EOF
```{{copy}}

- Configure the web-flask-svc service again via apply command.

`kubectl apply -f web-svc.yaml`{{copy}}

- List the services and notice that nodeport numer is 30036.

`kubectl get svc -o wide`{{copy}}