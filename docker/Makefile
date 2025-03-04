UBUNTU_VERSION=16.04
DOCKER_IMAGE=ubuntu:$(UBUNTU_VERSION)-sniper-$(USER)
DOCKER_FILE=Dockerfile-ubuntu-$(UBUNTU_VERSION)

all: $(DOCKER_FILE)
	docker build -f $(DOCKER_FILE) -t $(DOCKER_IMAGE) ../
	
run:
	docker run --privileged --rm -it -v "/home/bwoah/open-source-projects/HotSniper:/home/bwoah/open-source-projects/HotSniper" --user $(shell id -u):$(shell id -g) -w "${PWD}" $(DOCKER_IMAGE)

.PHONY: all
