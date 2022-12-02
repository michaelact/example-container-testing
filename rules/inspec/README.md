# [InSpec](https://github.com/inspec/inspec)

## Persiapan
1. Install [Docker](https://docs.docker.com/engine/install/)
2. `cd /path/to/example-container-testing/container`
3. Build bad image: `docker build -f Dockerfile.bad -t bad-case:latest .`
4. Build good image: `docker build -f Dockerfile.good -t good-case:latest .`

## Percobaan
1. Install [InSpec](https://docs.chef.io/inspec/install/)
2. `cd /path/to/example-container-testing/rules/inspec`
3. Test bad case:
   - Simpan container ID: `docker run -it --rm --entrypoint sleep bad-case:latest 9999`
   - Taruh container ID: `inspec exec test_exec_container.rb -t docker://CONTAINER_ID`
4. Test good case:
   - Simpan container ID: `docker run -it --rm --entrypoint sleep good-case:latest 9999`
   - Taruh container ID: `inspec exec test_exec_container.rb -t docker://CONTAINER_ID`

## Belum diketahui
- Memeriksa label dari container image
