# [Goss](https://github.com/goss-org/goss)

## Persiapan
1. Install [Docker](https://docs.docker.com/engine/install/)
2. `cd /path/to/example-container-testing/container`
3. Build bad image: `docker build -f Dockerfile.bad -t bad-case:latest .`
4. Build good image: `docker build -f Dockerfile.good -t good-case:latest .`

## Percobaan

1. Install [goss](https://github.com/goss-org/goss#installation)
2. `cd /path/to/example-container-testing/rules/goss`
3. `dgoss run -it --rm --entrypoint sh bad-case:latest`
4. `dgoss run -it --rm --entrypoint sh good-case:latest`
