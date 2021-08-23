# Pod maintenance
## SSH
`kubectl exec --stdin --tty <POD NAME>  -n <NAMESPACE> -- /bin/sh`

## CP
`kubectl cp <LOCAL  PATH> <NAMESPACE>/<POD>:<PATH>`

## Port forward
`kubectl port-forward <POD> <PORT> -n <NAMESPACE>`


# Resource creation
## Get YAML for resource
`kubectl get <TYPE> <NAME> -n <NAMESPACE> -o yaml`
