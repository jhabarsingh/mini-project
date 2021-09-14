import json
import datetime
from kubernetes import client


def addUsernames(x):
    r = json.loads(x.to_json())
    r['_id'] = str(x.id)
    r['by'] = x.by.username
    r['created_on'] = x.id.generation_time
    return r

class Kube:
    @classmethod
    def create_deployment_object(cls,name,deployment_name,image,port,cpu,memory,cpuLimit,memLimit,replica):
        # Configureate Pod template container
        container = client.V1Container(
            name=name,
            image=image,
            ports=[client.V1ContainerPort(container_port=port)],
            resources=client.V1ResourceRequirements(
                requests={"cpu": cpu, "memory": memory},
                limits={"cpu": cpuLimit, "memory": memLimit},
            ),
        )
        # Create and configurate a spec section
        template = client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(labels={"app": name}),
            spec=client.V1PodSpec(containers=[container]),
        )

        # Create the specification of deployment
        spec = client.V1DeploymentSpec(
            replicas=replica, template=template, selector={
                "matchLabels":
                {"app": name}})

        # Instantiate the deployment object
        deployment = client.V1Deployment(
            api_version="apps/v1",
            kind="Deployment",
            metadata=client.V1ObjectMeta(name=deployment_name),
            spec=spec,
        )
        return deployment

    @classmethod
    def create_service_object(cls,service_name,name,port,target_port):
        body=client.V1Service()
        metadata = client.V1ObjectMeta(name=service_name)
        spec = client.V1ServiceSpec(type='NodePort')
        port = client.V1ServicePort(port=port,target_port=target_port)
        spec.ports = [ port ]
        spec.selector = {"app": name}
        body.spec = spec
        body.metadata=metadata
        return body

    @classmethod
    def create_service(cls,api_instance,body,namespace="default"):
        api_response = api_instance.create_namespaced_service(namespace=namespace, body=body)
        return api_response

    @classmethod
    def create_deployment(cls,api, deployment,namespace="default"):
        # Create deployement
        resp = api.create_namespaced_deployment(
            body=deployment, namespace=namespace
        )
        return resp

    @classmethod
    def delete_deployment(cls,api,deployment_name,namespace="default"):
        # Delete deployment
        resp = api.delete_namespaced_deployment(
            name=deployment_name,
            namespace=namespace,
        )
        return resp

    @classmethod
    def delete_service(cls,api,service_name,namespace="default"):
        # Delete service
        resp = api.delete_namespaced_service(
            name=service_name,
            namespace=namespace,
        )
        return resp
    
    @classmethod
    def deploy(cls,req,coreApi,appsApi,namespace="default"):
        deployObject = cls.create_deployment_object(str(req.appName),str(req.deploymentName),str(req.image),int(req.port),str(req.cpu),str(req.memory),str(req.cpuLimit),str(req.memLimit),int(req.maxReplicas))
        deployResponse = cls.create_deployment(appsApi,deployObject,namespace)
        serviceObject = cls.create_service_object(str(req.serviceName),str(req.appName),8082,int(req.port))
        serviceResponse = cls.create_service(coreApi,serviceObject,namespace)
        return serviceResponse.spec.ports[0].node_port

    @classmethod
    def delete(cls,req,coreApi,appsApi,namespace="default"):
        deployResponse = cls.delete_deployment(appsApi,str(req.deploymentName),namespace)
        serviceResponse = cls.delete_service(coreApi,str(req.serviceName),namespace)

