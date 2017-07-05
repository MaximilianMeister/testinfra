import pytest

@pytest.mark.worker
class TestKubernetesWorker(object):
    """docstring for TestBaseEnv"""
    @pytest.mark.parametrize("service", [
        "flanneld",
        "docker",
        "containerd",
        "container-feeder",
        "kubelet",
        "kube-proxy"
    ])
    def test_services_running(self, host, service):
        host_service = host.service(service)
        assert host_service.is_running
        assert host_service.is_enabled
