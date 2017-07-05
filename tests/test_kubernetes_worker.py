import pytest
import testinfra

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

    @pytest.mark.parametrize("service", [
        "flanneld",
        "docker",
        "container-feeder",
        "kubelet",
        "kube-proxy"
    ])
    def test_services_enabled(self, host, service):
        host_service = host.service(service)
        assert host_service.is_enabled

    def test_salt_role(self, host):
        assert 'kube-minion' in host.salt("grains.get", "roles")

    def test_salt_id(self, host):
        machine_id = host.file('/etc/machine-id').content_string.rstrip()
        assert machine_id in host.salt("grains.get", "id")