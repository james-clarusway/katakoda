## Using Secrets 

- Let's assume that, we have a redis pod and we want to store some sensitive data such as a password in this pod. For this, we define sensitive variables with secrets.

- Firstly describe the mysecret.

`kubectl describe secret mysecret`{{copy}}

- Create a mysecret-pod.yaml file, and define this secrets in mysecret-pod.yaml as below.

```
cat << EOF > mysecret-pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: secret-env-pod
spec:
  containers:
  - name: mycontainer
    image: redis
    env:
      - name: SECRET_USERNAME
        valueFrom:
          secretKeyRef:
            name: mysecret   # This is name of secret
            key: username    # This is name of data
      - name: SECRET_PASSWORD
        valueFrom:
          secretKeyRef:
            name: mysecret   # This is name of secret
            key: password    # This is name of data
  restartPolicy: Never
EOF
```{{copy}}

- Create the pod.

`kubectl apply -f mysecret-pod.yaml`{{copy}}

## Consuming Secret Values from environment variables

Inside a container that consumes a secret in an environment variables, the secret keys appear as normal environment variables containing the base64 decoded values of the secret data. This is the result of commands executed inside the container from the example above:

- Enter into pod and type following command.

`kubectl exec -it secret-env-pod -- bash`{{copy}}

`echo $SECRET_USERNAME`{{copy}}

`echo $SECRET_PASSWORD`{{copy}}