import pytest

@pytest.mark.common
class TestCommon(object):
    """docstring for TestBaseEnv"""
    @pytest.mark.parametrize("service", [
        "etcd",
        "salt-minion"
    ])
    def test_services_running(self, host, service):
        host_service = host.service(service)
        assert host_service.is_running
        assert host_service.is_enabled

    def test_bootstrap_grain(self, host):
        grains = host.salt("grains.get")
        print(grains)
        assert 0
