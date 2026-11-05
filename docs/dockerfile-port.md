# Dockerfile 및 포트 매핑 검증

[← README로 돌아가기](../README.md)

## Dockerfile

#### 선정한 베이스 이미지

- **이미지**는 **Ubuntu**를 사용

#### 커스텀 이미지 구성 및 목적

- 빌드할때 **nginx** 프로그램이 설치되도록 하였다. 
- **Ubuntu**에는 **다운로드 기능**이 존재하므로 다른 프로그램이 설치되는지 확인해보려고 하였다.

#### 작성한 Dockerfile

- 프로젝트 루트의 [Dockerfile](../Dockerfile)을 사용한다.

```dockerfile
FROM ubuntu:24.04

RUN apt-get update -y && apt-get install nginx -y

ENV codyssey=minseong

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl -f http://localhost:80/ || exit 1

COPY ./index.html /var/www/html/index.html

CMD ["/bin/bash"]
```

#### 이미지 빌드 및 컨테이너 실행 결과

```bash
# Dockerfile에 기록한 것을 통해 nginx-install-ubuntu:1.4 이미지를 생성 (현재 경로를 기준으로 필요한 데이터를 사용함)
$ sudo docker build -t nginx-install-ubuntu:1.4 .
[+] Building 0.2s (8/8) FINISHED                                                                                                                                 docker:default
 => [internal] load build definition from Dockerfile                                                                                                                       0.0s
 => => transferring dockerfile: 298B                                                                                                                                       0.0s
 => [internal] load metadata for docker.io/library/ubuntu:24.04                                                                                                            0.0s
 => [internal] load .dockerignore                                                                                                                                          0.0s
 => => transferring context: 2B                                                                                                                                            0.0s
 => [1/3] FROM docker.io/library/ubuntu:24.04@sha256:534baea6a22c03a63003dbc8dbe78fe34bc0d7e595d9a9dc9834884ff530eb55                                                      0.0s
 => => resolve docker.io/library/ubuntu:24.04@sha256:534baea6a22c03a63003dbc8dbe78fe34bc0d7e595d9a9dc9834884ff530eb55                                                      0.0s
 => [internal] load build context                                                                                                                                          0.0s
 => => transferring context: 256B                                                                                                                                          0.0s
 => CACHED [2/3] RUN apt-get update -y && apt-get install nginx -y                                                                                                         0.0s
 => [3/3] COPY ./index.html /var/www/html/index.html                                                                                                                       0.0s
 => exporting to image                                                                                                                                                     0.1s
 => => exporting layers                                                                                                                                                    0.0s
 => => exporting manifest sha256:77f4fe073901b979fb6a2155eae387d477c7cdcc5a4cacd377af2cc6a46d7b7b                                                                          0.0s
 => => exporting config sha256:bd84ab9eb95545375ef651a179d4063553b30068f93c1609be3bef516a82f074                                                                            0.0s
 => => exporting attestation manifest sha256:39adeef4b331885110094e2298a785af08b708601c54b95e8494ead1a5b7ca0e                                                              0.0s
 => => exporting manifest list sha256:c9fa61ecbfc8e7d0c69f2aa20a6a75c687659841f34c18ebb403dad6fc29be98                                                                     0.0s
 => => naming to docker.io/library/nginx-install-ubuntu:1.4                                                                                                                0.0s
 => => unpacking to docker.io/library/nginx-install-ubuntu:1.4                                                                                                             0.0s                                                                                                          0.0s

# 만들어진 이미지를 통해 컨테이너 생성
$ sudo docker run -dit -p 8080:80 --name my-ubuntu nginx-install-ubuntu:1.4
622774c781d25a12ee608abf8f94f79b3ddebbf4e7754b820de8bc6aaa56c695
```

## 포트 매핑

#### 포트 설정

| 구분 | 포트 |
| --- | --- |
| 호스트 포트 | 8080 |
| 컨테이너 포트 | 80 |

#### 실행 명령어 및 결과

```bash
# 실행중인 컨테이너 확인 (포트 매핑 확인용)
$ sudo docker ps
CONTAINER ID   IMAGE                      COMMAND       CREATED          STATUS                             PORTS                                     NAMES
622774c781d2   nginx-install-ubuntu:1.4   "/bin/bash"   26 seconds ago   Up 25 seconds (health: starting)   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   my-ubuntu
```

#### 접속 결과

- 접속 주소: [http://localhost:8080]