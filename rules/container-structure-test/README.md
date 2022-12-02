# [Container Structure Test](https://github.com/GoogleContainerTools/container-structure-test)

## Persiapan
1. Install [Docker](https://docs.docker.com/engine/install/)
2. `cd /path/to/example-container-testing/container`
3. Build bad image: `docker build -f Dockerfile.bad -t bad-case:latest .`
4. Build good image: `docker build -f Dockerfile.good -t good-case:latest .`

## Percobaan

1. Install [container-structure-test](https://github.com/GoogleContainerTools/container-structure-test#installation)
2. `cd /path/to/example-container-testing/rules/container-structure-test`
3. `container-structure-test test --image bad-case:latest --config tests.yaml`
4. `container-structure-test test --image good-case:latest --config tests.yaml`

## Belum diketahui
- Memeriksa label dari container image
