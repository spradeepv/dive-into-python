Introduction
------------

This chart bootstraps a daemonset which contains 2 containers **keepalived-config-manager** and **service-firewall-driver**, on a kubernetes cluster using the Helm package manager.

Prerequisites
-------------
- Kubernetes 1.5+ with Beta APIs enabled
- Configmap 'hostname-to-vrid-map', which contains the details of the VR ids to be used by the keepalived process on each worker node.

Helm RBAC setup for K8s v1.6+
-----------------------------

    $ kubectl -n kube-system create sa tiller
    $ kubectl create clusterrolebinding tiller --clusterrole cluster-admin \
        --serviceaccount=kube-system:tiller 
    $ helm init --service-account tiller
    
Packagaing the Chart
--------------------
To package the chart, execut the below command:

    $ helm package keepalived-config-manager

Installing the Chart
--------------------
To install the chart with the release name _kcm-svc-fw_:

    $ helm install --name kcm-svc-fw keepalived-config-manager.tar.gz

Uninstalling the Chart
----------------------
To uninstall/delete the _kcm-svc-fw_ deployment:
    
     $ helm delete kcm-svc-fw

The command removes all the kubernetes components associated with the chart and deletes the release.

Configuration
-------------
The following tables lists the configurable parameters of this chart and their default values specified in the [values.yaml](values.yaml).

Parameter | Description | Default |
--- | --- | --- | 
namespace | Namespace in kubernets to deploy this chart | kube-system |
imageRegistry | Registry from where to pull image from | hub.docker.hpecorp.net/ncs-lbaas/ |
kcmTag | Tag of the keepalived-config-manager image to use | v0.12.2 |
svcFwTag | Tag of the service-firewall-driver image to use | v0.10.2 |
imagePullPolicy | Image pull policy | IfNotPresent |
