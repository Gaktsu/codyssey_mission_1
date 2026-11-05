# Docker 설치 및 운영 검증

[← README로 돌아가기](../README.md)

## Docker 환경

#### 설치 및 데몬 확인

```bash
# docker의 버전 확인
$ docker --version
Docker version 29.9.0, build f415da8

$ docker info
Client: Docker Engine - Community
 Version:    29.9.0
 Context:    default
 Debug Mode: false
 Plugins:
  buildx: Docker Buildx (Docker Inc.)
    Version:  v0.38.0
    Path:     /usr/libexec/docker/cli-plugins/docker-buildx
  compose: Docker Compose (Docker Inc.)
    Version:  v5.6.0
    Path:     /usr/libexec/docker/cli-plugins/docker-compose

# 설치된 docker의 정보
$ sudo docker info
[sudo] password for minsung: 
Client: Docker Engine - Community
 Version:    29.9.0
 Context:    default
 Debug Mode: false
 Plugins:
  buildx: Docker Buildx (Docker Inc.)
    Version:  v0.38.0
    Path:     /usr/libexec/docker/cli-plugins/docker-buildx
  compose: Docker Compose (Docker Inc.)
    Version:  v5.6.0
    Path:     /usr/libexec/docker/cli-plugins/docker-compose

Server:
 Containers: 0
  Running: 0
  Paused: 0
  Stopped: 0
 Images: 8
 Server Version: 29.9.0
 Storage Driver: overlayfs
  driver-type: io.containerd.snapshotter.v1
 Logging Driver: json-file
 Cgroup Driver: systemd
 Cgroup Version: 2
 Plugins:
  Volume: local
  Network: bridge host ipvlan macvlan null overlay
  Log: awslogs fluentd gcplogs gelf journald json-file local splunk syslog
 CDI spec directories:
  /etc/cdi
  /var/run/cdi
 Swarm: inactive
 Runtimes: io.containerd.runc.v2 runc
 Default Runtime: runc
 Init Binary: docker-init
 containerd version: f2551031d7276a770f65f98c9b52e57e7dad07e8
 runc version: v1.5.2-0-g29dd3dc2
 init version: de40ad0
 Security Options:
  apparmor
   Profile: default
  seccomp
   Profile: builtin
  cgroupns
 Kernel Version: 7.0.0-38-generic
 Operating System: Ubuntu 24.04.4 LTS
 OSType: linux
 Architecture: x86_64
 CPUs: 8
 Total Memory: 15.3GiB
 Name: minsung-ThinkPad-E15
 ID: bce2c2bd-43d1-42b8-98e7-59ed299978fe
 Docker Root Dir: /var/lib/docker
 Debug Mode: false
 Experimental: false
 Insecure Registries:
  127.0.0.0/8
  ::1/128
 Live Restore Enabled: false
 Firewall Backend: iptables
  EnableUserlandProxy: true
  UserlandProxyPath: /usr/bin/docker-proxy
```

#### 이미지 다운로드 및 목록 확인

```bash
# 로컬에 저장되어 있는 이미지들을 확인
$ sudo docker images
                                                                                                                                                                           i Info →   U  In Use
IMAGE                   ID             DISK USAGE   CONTENT SIZE   EXTRA
alpine:3                294b683cb724         13MB         3.94MB        
alpine:3.20             d9e853e87e55       12.2MB         3.71MB        
docker-practice:v1      c4b6417a2c54        117MB         29.8MB        
mysql:8.0               7dcddc01f13b        1.1GB          249MB        
python:3.12-alpine      1b668429b351       83.6MB         21.3MB        
qdrant/qdrant:v1.19.1   12364fe851b9        288MB         79.1MB        
quality-system:v1       e43627a2b105        709MB          239MB        
ubuntu:24.04            534baea6a22c        119MB         31.7MB 

# dockerhub 사이트에 있는 nginx:trixie-perl 이미지를 설치
$ sudo docker pull nginx:trixie-perl
trixie-perl: Pulling from library/nginx
95f771989cac: Downloading [======================================>            ]  9.437MB/12.16MB
6e2ab1f3ef4e: Download complete 
a670537bed70: Download complete 
c139fe92686d: Download complete 
a071113ac575: Pulling fs layer 
6fc242d221a6: Downloading [========>                                          ]  5.243MB/29.86MB
9f604dae09b2: Download complete 
d322f1bf41d8: Download complete 
7829d19bb7a0: Download complete 
adc573221049: Download complete 

# nginx:trixie-perl 이 추가된 것을 확인
$ sudo docker images
                                                                                                                                                                           i Info →   U  In Use
IMAGE                   ID             DISK USAGE   CONTENT SIZE   EXTRA
alpine:3                294b683cb724         13MB         3.94MB        
alpine:3.20             d9e853e87e55       12.2MB         3.71MB        
docker-practice:v1      c4b6417a2c54        117MB         29.8MB        
mysql:8.0               7dcddc01f13b        1.1GB          249MB        
nginx:trixie-perl       3921681524c5        314MB         80.4MB        
python:3.12-alpine      1b668429b351       83.6MB         21.3MB        
qdrant/qdrant:v1.19.1   12364fe851b9        288MB         79.1MB        
quality-system:v1       e43627a2b105        709MB          239MB        
ubuntu:24.04            534baea6a22c        119MB         31.7MB     
```

#### 컨테이너 실행 및 관리

```bash
# nginx:trixie-perl 이미지를 기반으로 컨테이너 생성 후 실행
$ sudo docker run nginx:trixie-perl
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2026/11/04 05:55:58 [notice] 1#1: using the "epoll" event method
2026/11/04 05:55:58 [notice] 1#1: nginx/1.31.8
2026/11/04 05:55:58 [notice] 1#1: built by gcc 14.2.0 (Debian 14.2.0-19) 
2026/11/04 05:55:58 [notice] 1#1: OS: Linux 7.0.0-38-generic
2026/11/04 05:55:58 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1024:524288
2026/11/04 05:55:58 [notice] 1#1: start worker processes
2026/11/04 05:55:58 [notice] 1#1: start worker process 29
2026/11/04 05:55:58 [notice] 1#1: start worker process 30
2026/11/04 05:55:58 [notice] 1#1: start worker process 31
2026/11/04 05:55:58 [notice] 1#1: start worker process 32
2026/11/04 05:55:58 [notice] 1#1: start worker process 33
2026/11/04 05:55:58 [notice] 1#1: start worker process 34
2026/11/04 05:55:58 [notice] 1#1: start worker process 35
2026/11/04 05:55:58 [notice] 1#1: start worker process 36

# 실행되고 있는 컨테이너들을 확인
$ sudo docker ps
CONTAINER ID   IMAGE               COMMAND                  CREATED          STATUS          PORTS     NAMES
55d3089892fd   nginx:trixie-perl   "/docker-entrypoint.…"   50 seconds ago   Up 49 seconds   80/tcp    trusting_newton

# 실행되지 않는 컨테이너들을 포함한 모든 컨테이너들을 확인
$ sudo docker ps -a
CONTAINER ID   IMAGE               COMMAND                  CREATED              STATUS              PORTS     NAMES
55d3089892fd   nginx:trixie-perl   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    trusting_newton

# nginx:trixie-perl 이름의 컨테이너를 종료 시도하였지만 실패
# nginx:trixie-perl은 컨테이너가 아닌 이미지 이름이라서 실패함
$ sudo docker stop nginx:trixie-perl
Error response from daemon: No such container: nginx:trixie-perl

# 컨테이너의 ID를 입력하여 종료
$ sudo docker stop 55d3089892fd
55d3089892fd

# 컨테이너의 ID를 입력하여 제거
$ sudo docker rm 55d3089892fd
55d3089892fd

# 제거되었는지 확인
$ sudo docker ps -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

#### 로그 및 리소스 확인

```bash
# nginx:trixie-perl 이미지를 기반으로 한 nginx 이름의 컨테이너를 생성하고 실행함
$ sudo docker run --name nginx nginx:trixie-perl
[sudo] password for minsung: 
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2026/11/05 06:55:02 [notice] 1#1: using the "epoll" event method
2026/11/05 06:55:02 [notice] 1#1: nginx/1.31.8
2026/11/05 06:55:02 [notice] 1#1: built by gcc 14.2.0 (Debian 14.2.0-19) 
2026/11/05 06:55:02 [notice] 1#1: OS: Linux 7.0.0-38-generic
2026/11/05 06:55:02 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1024:524288
2026/11/05 06:55:02 [notice] 1#1: start worker processes
2026/11/05 06:55:02 [notice] 1#1: start worker process 29
2026/11/05 06:55:02 [notice] 1#1: start worker process 30
2026/11/05 06:55:02 [notice] 1#1: start worker process 31
2026/11/05 06:55:02 [notice] 1#1: start worker process 32
2026/11/05 06:55:02 [notice] 1#1: start worker process 33
2026/11/05 06:55:02 [notice] 1#1: start worker process 34
2026/11/05 06:55:02 [notice] 1#1: start worker process 35
2026/11/05 06:55:02 [notice] 1#1: start worker process 36

# nginx의 로그를 확인
$ sudo docker logs nginx
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2026/11/04 06:02:13 [notice] 1#1: using the "epoll" event method
2026/11/04 06:02:13 [notice] 1#1: nginx/1.31.8
2026/11/04 06:02:13 [notice] 1#1: built by gcc 14.2.0 (Debian 14.2.0-19) 
2026/11/04 06:02:13 [notice] 1#1: OS: Linux 7.0.0-38-generic
2026/11/04 06:02:13 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1024:524288
2026/11/04 06:02:13 [notice] 1#1: start worker processes
2026/11/04 06:02:13 [notice] 1#1: start worker process 29
2026/11/04 06:02:13 [notice] 1#1: start worker process 30
2026/11/04 06:02:13 [notice] 1#1: start worker process 31
2026/11/04 06:02:13 [notice] 1#1: start worker process 32
2026/11/04 06:02:13 [notice] 1#1: start worker process 33
2026/11/04 06:02:13 [notice] 1#1: start worker process 34
2026/11/04 06:02:13 [notice] 1#1: start worker process 35
2026/11/04 06:02:13 [notice] 1#1: start worker process 36
2026/11/04 06:02:54 [notice] 1#1: signal 3 (SIGQUIT) received, shutting down
2026/11/04 06:02:54 [notice] 32#32: gracefully shutting down
2026/11/04 06:02:54 [notice] 29#29: gracefully shutting down
2026/11/04 06:02:54 [notice] 31#31: gracefully shutting down
2026/11/04 06:02:54 [notice] 30#30: gracefully shutting down
2026/11/04 06:02:54 [notice] 29#29: exiting
2026/11/04 06:02:54 [notice] 31#31: exiting
2026/11/04 06:02:54 [notice] 30#30: exiting
2026/11/04 06:02:54 [notice] 33#33: gracefully shutting down
2026/11/04 06:02:54 [notice] 34#34: gracefully shutting down
2026/11/04 06:02:54 [notice] 29#29: exit
2026/11/04 06:02:54 [notice] 34#34: exiting
2026/11/04 06:02:54 [notice] 33#33: exiting
2026/11/04 06:02:54 [notice] 31#31: exit
2026/11/04 06:02:54 [notice] 30#30: exit
2026/11/04 06:02:54 [notice] 35#35: gracefully shutting down
2026/11/04 06:02:54 [notice] 34#34: exit
2026/11/04 06:02:54 [notice] 33#33: exit
2026/11/04 06:02:54 [notice] 35#35: exiting
2026/11/04 06:02:54 [notice] 36#36: gracefully shutting down
2026/11/04 06:02:54 [notice] 36#36: exiting
2026/11/04 06:02:54 [notice] 35#35: exit
2026/11/04 06:02:54 [notice] 36#36: exit
2026/11/04 06:02:54 [notice] 32#32: exiting
2026/11/04 06:02:54 [notice] 32#32: exit
2026/11/04 06:02:54 [notice] 1#1: signal 17 (SIGCHLD) received from 34
2026/11/04 06:02:54 [notice] 1#1: worker process 34 exited with code 0
2026/11/04 06:02:54 [notice] 1#1: worker process 29 exited with code 0
2026/11/04 06:02:54 [notice] 1#1: signal 29 (SIGIO) received
2026/11/04 06:02:54 [notice] 1#1: signal 17 (SIGCHLD) received from 29
2026/11/04 06:02:54 [notice] 1#1: signal 17 (SIGCHLD) received from 33
2026/11/04 06:02:54 [notice] 1#1: worker process 33 exited with code 0
2026/11/04 06:02:54 [notice] 1#1: signal 29 (SIGIO) received
2026/11/04 06:02:54 [notice] 1#1: signal 17 (SIGCHLD) received from 32
2026/11/04 06:02:54 [notice] 1#1: worker process 32 exited with code 0
2026/11/04 06:02:54 [notice] 1#1: worker process 35 exited with code 0
2026/11/04 06:02:54 [notice] 1#1: signal 29 (SIGIO) received
2026/11/04 06:02:54 [notice] 1#1: signal 17 (SIGCHLD) received from 30
2026/11/04 06:02:54 [notice] 1#1: worker process 30 exited with code 0
2026/11/04 06:02:54 [notice] 1#1: worker process 31 exited with code 0
2026/11/04 06:02:54 [notice] 1#1: signal 29 (SIGIO) received
2026/11/04 06:02:54 [notice] 1#1: signal 17 (SIGCHLD) received from 36
2026/11/04 06:02:54 [notice] 1#1: worker process 36 exited with code 0
2026/11/04 06:02:54 [notice] 1#1: exit

# nginx 컨테이너가 사용하고 있는 하드웨어 자원을 얼마나 사용하는지 확인
$ sudo docker stats nginx
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT    MEM %     NET I/O         BLOCK I/O   PIDS
b1a6fa47e38b   nginx     0.00%     7.492MiB / 15.3GiB   0.05%     2.79kB / 126B   0B / 0B     9
```

#### hello-world 및 Ubuntu 컨테이너

```bash
# hello-world 이미지를 기반으로 컨테이너 생성 후 실행 시도
# 로컬에 hello-world 이미지가 존재하지 않기에 docker hub에서 다운받아서 작업하는것을 확인 
$ sudo docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
4f55086f7dd0: Pull complete 
d5e71e642bf5: Download complete 
Digest: sha256:c567b231f65614688711a75f31518a064258a51d442117a3e771a3a8fdba78ef
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

# Ubuntu 컨테이너 실행 및 접속
$ sudo docker run -dit -p 8080:80 --name ubuntu ubuntu:24.04
82e00a5070e6203e94f372e33e16ea6ebd39d5bbfdd8909813d1e38d143244af

# ubuntu 컨테이너의 첫번째 프로세스를 호스트 터미널에 연결
$ sudo docker attach ubuntu
root@82e00a5070e6:/# 

# ubuntu 컨테이너의 bash 프로그램을 실행하여 호스트 터미널에 연결
$ sudo docker exec -it ubuntu bash
root@82e00a5070e6:/# 

# nginx 컨테이너 내부에서 bash 프로그램을 실행하여 호스트 터미널에 연결
# 실행한 bash 프로세스에서 ls 명령어 실행
# 실행한 bash 프로세스에서 Hello Codyssey! 출력
$ sudo docker exec -it nginx bash
root@b1a6fa47e38b:/# ls
bin  boot  dev  docker-entrypoint.d  docker-entrypoint.sh  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@b1a6fa47e38b:/# echo "Hello Codyssey!"
Hello Codyssey!
```

