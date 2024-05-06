echo -n 'secret_text' | base64
kubectl get secrets
kubectl describe secret secret_name
kubectl get secrets secret secret_name -o yaml
echo -n 'encode_text' | base64 --decode
