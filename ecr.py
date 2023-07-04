apiVersion: v1
kind: Pod
metadata:
   name: cloud-native-monitoring-
     image: my-flask-app:latest
     ports:
     - containerPort: 5000
