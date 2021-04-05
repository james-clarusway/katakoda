## Creating a Secret manually 

- You can also create a Secret in a file first, in JSON or YAML format, and then create that object. The name of a Secret object must be a valid DNS subdomain name. 

- The Secret contains two maps: data and stringData. 

- The **data** field is used to store arbitrary data, encoded using base64. 

- The **stringData** field is provided for convenience, and allows you to provide secret data as unencoded strings.

For example, to store two strings in a Secret using the data field, convert the strings to base64 as follows:

`echo -n 'admin' | base64`{{copy}}

The output is similar to:
```text
YWRtaW4=
```

`echo -n '1f2d1e2e67df' | base64`{{copy}}

The output is similar to:
```text
MWYyZDFlMmU2N2Rm
```

Write a Secret that looks like this named secret.yaml:

```
cat << EOF > secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
type: Opaque
data:
  username: YWRtaW4=
  password: MWYyZDFlMmU2N2Rm
EOF
```{{copy}}

Now create the Secret using `kubectl apply`:

`kubectl apply -f ./secret.yaml`{{copy}}

### Decoding a Secret

Secrets can be retrieved by running kubectl get secret. For example, you can view the Secret created in the previous section by running the following command:

`kubectl get secret mysecret -o yaml`{{copy}}

The output is similar to:
```text
apiVersion: v1
data:
  password: MWYyZDFlMmU2N2Rm
  username: YWRtaW4=
kind: Secret
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"v1","data":{"password":"MWYyZDFlMmU2N2Rm","username":"YWRtaW4="},"kind":"Secret","metadata":{"annotations":{},"name":"mysecret","namespace":"default"},"type":"Opaque"}
  creationTimestamp: "2020-09-06T17:39:17Z"
  managedFields:
  - apiVersion: v1
    fieldsType: FieldsV1
    fieldsV1:
      f:data:
        .: {}
        f:password: {}
        f:username: {}
      f:metadata:
        f:annotations:
          .: {}
          f:kubectl.kubernetes.io/last-applied-configuration: {}
      f:type: {}
    manager: kubectl-client-side-apply
    operation: Update
    time: "2020-09-06T17:39:17Z"
  name: mysecret
  namespace: default
  resourceVersion: "98708"
  selfLink: /api/v1/namespaces/default/secrets/mysecret
  uid: c9589ee5-37f8-4ec8-9233-67c110b9f928
type: Opaque
```

Decode the password field:
`echo 'MWYyZDFlMmU2N2Rm' | base64 --decode`{{copy}}

The output is similar to:
```text
1f2d1e2e67df
```