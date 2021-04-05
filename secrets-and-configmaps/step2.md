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

Decode the password field:
`echo 'MWYyZDFlMmU2N2Rm' | base64 --decode`{{copy}}

The output is similar to:

```
1f2d1e2e67df
```