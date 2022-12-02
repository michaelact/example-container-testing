# [TestInfra](https://github.com/pytest-dev/pytest-testinfra)

## Persiapan
1. Install [Docker](https://docs.docker.com/engine/install/)
2. `cd /path/to/example-container-testing/container`
3. Build bad image: `docker build -f Dockerfile.bad -t bad-case:latest .`
4. Build good image: `docker build -f Dockerfile.good -t good-case:latest .`
5. Install [Python](https://www.python.org/downloads/) (Python 3.8.5)

## Percobaan
1. `cd /path/to/example-container-testing/rules/testinfra`
2. Install _PyTest_ dan _Dependencies_ lainnya: `pip3 install -r requirements.txt`
3. Test bad case:
   - `export CONTAINER_IMAGE_URL=bad-case:latest`
   - `pytest`
4. Test good case:
   - `export CONTAINER_IMAGE_URL=good-case:latest`
   - `pytest`
