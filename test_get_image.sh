#!bin/bash
#
# avatar server의 /packed_character_look으로의 테스트 콜

curl -X POST -H "Content-Type: application/json" http://demo-api-server.default.svc.cluster.local:8383/v1/character-info -d '{"user_name": "오지환"}'



aws ecr create-repository \
--repository-name avatar-server \
--image-scanning-configuration scanOnPush=true \
--region ${AWS_REGION}
apiVersion: v1
kind: Service
metadata:
  name: avatar-server
  annotations:
    alb.ingress.kubernetes.io/healthcheck-path: "/healthcheck"
spec:
  selector:
    app: avatar-server
  type: ClusterIP
  ports:
    - port: 8080
      targetPort: 8080
      protocol: TCP
---
apiVersion: apps/v1
kind: Deployment
metadata:
name: wzcomparerr2server
namespace: default
spec:
replicas: 1
selector:
matchLabels:
app: wzcomparerr2server
template:
metadata:
labels:
app: wzcomparerr2server
spec:
containers:
- name: wzcomparerr2server
image: 540566440182.dkr.ecr.ap-northeast-2.amazonaws.com/wzcomparerr2server:latest
imagePullPolicy: Always
env:
- name: ASPNETCORE_ENVIRONMENT
value: Development
ports:
- containerPort: 7209
volumeMounts:
- name: data-volume
mountPath: /app/Data
- name: ubuntu
image: ubuntu
command: ["/bin/bash"]
stdin: true
tty: true
volumeMounts:
- name: data-volume
mountPath: /app/Data
volumes:
- name: data-volume
persistentVolumeClaim:
claimName: wz-pvc

---
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
name: wz-pvc
spec:
accessModes:
- ReadWriteOnce
resources:
requests:
storage: 22Gi
storageClassName: gp2

aws ecr create-repository \
--repository-name inference-server \
--image-scanning-configuration scanOnPush=true \
--region ${AWS_REGION}