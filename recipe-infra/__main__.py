"""A Kubernetes Python Pulumi program"""

import pulumi
from pulumi_kubernetes.apps.v1 import Deployment
from pulumi_kubernetes.core.v1 import Service

app_labels = { "app": "recipe-app" }

# Deployment
deployment = Deployment(
    "recipe-app-deployment",
    metadata = {
        "name": "recipe-app-deployment",
        "labels": app_labels,
    },
    spec={
        "selector": { "match_labels": app_labels },
        "replicas": 1,
        "template": {
            "metadata": { "labels": app_labels },
            "spec": { "containers": [{
                "name": "recipe-app",
                "image": "priestjimbo/recipe-site:latest",
                "imagePullPolicy": "Always",
                "ports": [{"containerPort": 80}] }] }
        },
    })

# Service
service = Service(
    "recipe-app-service",
    metadata = {
        "name": "recipe-app-service",
        "labels": app_labels,
    },
    spec={
        "type": "NodePort",
        "selector": app_labels,
        "ports": [{
            "port":80,
            "targetPort": 80,
            "protocol": "TCP",
            "node_port": 30080
        }]
    }
)

pulumi.export("service_name", service.metadata["name"])
pulumi.export("node_port", service.spec["ports"][0]["node_port"])
