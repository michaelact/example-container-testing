import pytest
import subprocess
import os
import testinfra
import docker

DOCKER_IMAGE_NAME = os.environ['CONTAINER_IMAGE_URL']

# scope='session' uses the same container for all the tests;
# scope='function' uses a new container per test function.
@pytest.fixture(scope='function')
def host(request):
    docker_id = subprocess.check_output(
        ['docker', 'run', '--entrypoint', 'sleep', '-d', DOCKER_IMAGE_NAME, '9999']).decode().strip()
    host = testinfra.get_host("docker://" + docker_id)
    yield host
    subprocess.check_call(['docker', 'rm', '-f', docker_id])

def test_upgrade_packages(host):
    """
    Ensure `apt-get upgrade -y` is already executed
    """
    assert host.check_output('apt-get -qq update; apt-get -qqs upgrade') == ""

def test_operating_system(host):
    """
    Ensure Non-Alpine based image
    """
    assert b"Alpine" not in host.file("/etc/os-release").content

docker_client = docker.from_env()
def test_container_labels():
    """
    Ensure Container Image has `maintainer` label
    """
    labels = docker_client.images.get(DOCKER_IMAGE_NAME).labels
    assert labels['maintainer'] == 'Michael Act < michael.4ct@gmail.com >'
