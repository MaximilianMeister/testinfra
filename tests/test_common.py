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

    @pytest.mark.parametrize("service", [
        "etcd",
        "salt-minion"
    ])
    def test_services_enabled(self, host, service):
        host_service = host.service(service)
        assert host_service.is_enabled

    def test_bootstrap_grain(self, host):
        assert host.salt("grains.get", "bootstrap_complete")

    def test_etcd_aliveness(self, host):
        machine_id = host.file('/etc/machine-id').content_string.rstrip()
        cmd = "etcdctl --ca-file /etc/pki/trust/anchors/SUSE_CaaSP_CA.crt "\
              "--key-file /etc/pki/minion.key "\
              "--cert-file /etc/pki/minion.crt "\
              "--endpoints='https://%s.infra.caasp.local:2379' "\
              "cluster-health" % machine_id
        health = host.run_expect([0], cmd)
        assert "cluster is healthy" in health.stdout