# Docker, Docker Compose and Tensorflow Boilerplate

This is a minimal working example for running Tensorflow on Docker. It can be run as-is or can be forked and add you own tensorflow scripts.
There are two different docker images, where one is used for running Tensorflow in a GPU-accelerated device and another for running it in a CPU-only device.

The GPU docker image includes the installed Nvidia drivers. The GPU image can still run on a CPU-only machines, but best practise is to use CPU docker images
for CPU machines since the docker image size is smaller.

To start an interactive bash shell in a CPU-only Docker container:

```shell
docker compose run --rm tensorflow_cpu
```

To start an interactive bash shell in a GPU-supported Docker container:

```shell
docker compose run --rm tensorflow_gpu
```

To run CPU test:

```shell
docker compose run --rm tensorflow_cpu_test
```

To run GPU test:

```shell
docker compose run --rm tensorflow_gpu_test
```