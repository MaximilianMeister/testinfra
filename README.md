# testinfra tests for kubic nodes

This is a collection of testinfra tests that can be used to ensure that the bootstraping 
of a CaaSP install has been completed correctly

## Running

To run, you need to do a test run per node type right now in the following form:

`pytest --ssh-config=~/.ssh/config --sudo --hosts=admin-ip -m "admin or common" --junit-xml admin.xml -v`
`pytest --ssh-config=~/.ssh/config --sudo --hosts=master-ip -m "master or common" --junit-xml master.xml -v`
`pytest --ssh-config=~/.ssh/config --sudo --hosts=worker-1-ip,worker-2-ip -m "worker or common" --junit-xml workers.xml -v`

Where `~/.ssh/config` is an ssh config file that tells ssh what key to use for the connection

## File Structure

Right now, there is 4 test files.

`tests/test_common.py` - tests for services that are on all nodes, e.g. `etcd`, `salt-minion`
`tests/test_kubic_admin.py` - tests for services, files and configuration that are on just the admin node, e.g. salt roles
`tests/test_kubernetes_master.py` - tests for services, files and configuration that are on just the master node, and some tests of the kubernetes cluster itself
`tests/test_kubernetes_worker.py` - tests for services, files and configuration that are on just the worker nodes

## Related Links:

- testinfra http://testinfra.readthedocs.io/en/latest/index.html
- pytest https://docs.pytest.org/en/latest/contents.html
