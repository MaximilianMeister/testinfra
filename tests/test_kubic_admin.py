import pytest
import json

@pytest.mark.admin
class TestKubicAdmin(object):
    """docstring for TestBaseEnv"""

    @pytest.mark.parametrize("service", [
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
        "docker",
        "container-feeder",
        "kubelet",
        "kube-proxy"
    ])
    def test_services_enabled(self, host, service):
        host_service = host.service(service)
        assert host_service.is_enabled

    def test_salt_role(self, host):
        assert 'admin' in host.salt("grains.get", "roles")