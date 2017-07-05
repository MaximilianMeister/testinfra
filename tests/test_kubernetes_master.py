import pytest
import json

@pytest.mark.master
class TestKubernetesMaster(object):
    """docstring for TestBaseEnv"""

    @pytest.mark.parametrize("service", [
        "kube-apiserver",
        "kube-controller-manager",
        "kube-scheduler"
    ])
    def test_services_running(self, host, service):
        host_service = host.service(service)
        assert host_service.is_running
        assert host_service.is_enabled

    def test_kubernetes_cluster(self, host):
        host.run(
            "kubectl cluster-info dump --output-directory=/tmp/cluster_info"
        )

        nodes = json.loads(
            host.file("/tmp/cluster_info/nodes.json").content_string
        )
        # Check the number of nodes
        # TODO(graham): Load this from env
        assert (len(nodes["items"]) == 2)

        # Check all nodes are marked as "Ready" in k8s
        for node in nodes["items"]:
            for item in node["status"]["conditions"]:
                if item["type"] is "Ready":
                    assert bool(item["status"])