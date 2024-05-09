# Pod maintenance
## SSH
`kubectl exec --stdin --tty <POD NAME>  -n <NAMESPACE> -- /bin/sh`

## CP
`kubectl cp <LOCAL  PATH> <NAMESPACE>/<POD>:<PATH>`

## Port forward
`kubectl port-forward <POD> <PORT> -n <NAMESPACE>`

## Delete resources by pattern
`kubectl get <TYPE> -o custom-columns=:.metadata.name --no-headers | grep <PATTERN> | xargs echo kubectl delete <TYPE>`

## Clear finalizers
`kubectl patch <TYPE> <NAME> -p '{"metadata":{"finalizers":null}}' --type=merge`

## Print secret
`kubectl get secret <NAME> --template={{.data.<KEY>}} | base64 -D`


# Resource creation
## Get YAML for resource
`kubectl get <TYPE> <NAME> -n <NAMESPACE> -o yaml`

## Deploy a resource
`kubectl create -f <FILE.YML>` Create if not present  
`kubectl apply -f <FILE.YML>` Create if not present, overwrite if present (and it was created with `--apply`)

## Annotate a resource
`kubectl annotate <TYPE> <NAME> <ANNOTATION KEY>=<ANNOTATION VALUE>`

# Setup

Set default namespace: `kubectl config set-context --current --namespace=<NAMESPACE>`