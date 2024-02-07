   2        0.147 kubectl get pods -o wide
   3        0.166 docker ps
   4        0.156 kubectl get pods -o wide
   5        0.149 kubectl get replicaset
   6        0.135 kubectl get replicaset
   7        0.170 kubectl get pods -o wide
   8        1.050 kubectl delete pod nginx
   9        0.023 cd .\kubernetes\fundamentals\
  10        0.446 kubectl create -f .\replicasets\replicaset.yaml
  11        0.432 kubectl create -f .\replicasets\replicaset.yaml
  12        0.339 kubectl create -f .\replicasets\replicaset.yaml
  13        0.426 kubectl create -f .\replicasets\replicaset.yaml
  14        0.367 kubectl get .\replicasets\
  15        0.151 kubectl get replicaset
  16        0.180 kubectl get pods
  17        0.169 kubectl deelte pod myapp-replicaset-mpn5p
  18        1.589 kubectl delete pod myapp-replicaset-mpn5p
  19        0.150 kubectl get pods
  20        0.162 kubectl describe replicaset my-app-replicaset
  21        0.215 kubectl get replicaset
  22        0.206 kubectl describe replicaset myapp-replicaset
  23       13.510 kubectl edit replicaset myapp-replicaset
  24        0.133 kubectl get pods
  25        0.179 kubectl scale replicaset myapp-replicaset --replicas=2
  26        0.130 kubectl get pods
  27        0.265 kubectl get all
  28        0.150 kubectl get services
  29        0.263 kubectl create -f .\deployments\deployment.yaml
  30        0.295 kubectl create -f .\deployments\deployment.yaml
  31        0.324 kubectl get deployments
  32        0.279 kubelctl get pods
  33        0.211 kubectl get pods
  34        0.144 kubectl get pods -o wide
  35        0.139 kubectl get pods -o wide
  36        0.154 kubectl get pods
  37        0.142 kubectl get pods -o wide
  38        0.140 kubectl get deployments
  39        0.133 kubectl get replicaset
  40        0.143 kubectl get deployments
  41        0.164 kubectl get pods -o wide
  42        0.164 kubectl describe deployment nginx-deployment
  43        0.128 kubectl get deployments
  44        0.100 kubelctl delete deployment nginx-deployment
  45        0.147 kubectl delete deployment nginx-deployment
  46        0.164 kubectl get pods
  47        0.132 kubectl get replicaset
  48        0.145 kubectl delete replicaset myapp-replicaset
  49        0.165 kubectl get replicaset
  50        0.122 kubectl get pods
  51        0.040 clear
  52        0.098 kubelctl create -f .\deployments\deployment.yaml
  53        0.253 kubectl create -f .\deployments\deployment.yaml
  54        0.387 kubectl get pods
  55        0.143 kubectl get pods
  56        0.163 kubectl rollout status deployment.apps/nginx-deployment
  57        0.107 kubectl rollout history
  58        0.142 kubectl rollout history deployment.apps/nginx-deployment
  59        0.192 kubectl delete deployment nginx-deployment
  60        0.151 kubectl get pods
  61        0.125 kubectl get pods
  62        0.315 kubectl create -f .\deployments\deployment.yaml --record
  63        0.287 kubectl get pods
  64        0.167 kubectl rollout status deployment.apps/nginx-deployment
  65        0.144 kubectl rollout history deployment.apps/nginx-deployment
  66        0.122 kubelctl edit deployment nginx-deployment --record
  67        0.097 kube#ctl edit deployment nginx-deployment --record
  68       56.799 kubectl edit deployment nginx-deployment --record
  69        0.257 kubectl rollout history
  70        0.314 kubectl rollout history deployment.apps/nginx-deployment
  71        0.161 kubectl get pods
  72        0.257 kubectl get pods -o wide
  73        0.160 kubectl rollout undo deployment/nginx-deployment
  74        0.262 kubectl rollout history deployment.apps/nginx-deployment
  75        0.163 kubectl get pods -o wide
  76        0.089 kubelctl edit deployment nginx-deployment --record
  77     1:30.694 kubectl edit deployment nginx-deployment --record
  78        0.145 kubectl rollout history deployment.apps/nginx-deployment
  79        0.090 history
  80        3.767 kubectl edit deployment nginx-deployment --record
  81        0.132 kubectl rollout history deployment.apps/nginx-deployment
  82        0.141 kubectl rollout history deployment/nginx-deployment --revision=2
  83       11.066 kubectl edit deployment nginx-deployment
  84        0.137 kubectl rollout history deployment/nginx-deployment --revision=2
  85        0.157 kubectl rollout history deployment/nginx-deployment
  86        0.150 kubectl rollout undo deployment/nginx-deployment