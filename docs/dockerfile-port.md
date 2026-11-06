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

RUN apt-get update -y && apt-get install nginx -y && apt-get install curl -y

ENV codyssey=minseong

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl -f http://localhost:80/ || exit 1

COPY ./index.html /var/www/html/index.html

CMD ["nginx", "-g", "daemon off;"]
```

#### 이미지 빌드 및 컨테이너 실행 결과

```bash
# Dockerfile에 기록한 것을 통해 nginx-install-ubuntu:1.4 이미지를 생성 (현재 경로를 기준으로 필요한 데이터를 사용함)
 sudo docker build -t nginx-install-ubuntu:1.5 .
[+] Building 0.1s (8/8) FINISHED                                                                                                                           docker:default
 => [internal] load build definition from Dockerfile                                                                                                                 0.0s
 => => transferring dockerfile: 342B                                                                                                                                 0.0s
 => [internal] load metadata for docker.io/library/ubuntu:24.04                                                                                                      0.0s
 => [internal] load .dockerignore                                                                                                                                    0.0s
 => => transferring context: 2B                                                                                                                                      0.0s
 => [1/3] FROM docker.io/library/ubuntu:24.04@sha256:534baea6a22c03a63003dbc8dbe78fe34bc0d7e595d9a9dc9834884ff530eb55                                                0.0s
 => => resolve docker.io/library/ubuntu:24.04@sha256:534baea6a22c03a63003dbc8dbe78fe34bc0d7e595d9a9dc9834884ff530eb55                                                0.0s
 => [internal] load build context                                                                                                                                    0.0s
 => => transferring context: 32B                                                                                                                                     0.0s
 => CACHED [2/3] RUN apt-get update -y && apt-get install nginx -y && apt-get install curl -y                                                                        0.0s
 => CACHED [3/3] COPY ./index.html /var/www/html/index.html                                                                                                          0.0s
 => exporting to image                                                                                                                                               0.0s
 => => exporting layers                                                                                                                                              0.0s
 => => exporting manifest sha256:13af0353e8fb8ac687cad7ff700574c7888360ec4bd2cc1bb8007affa4bc623c                                                                    0.0s
 => => exporting config sha256:575c8beef8d4688c8febf1f0a9f110860767897a56f56a7d417418e2c5e400db                                                                      0.0s
 => => exporting attestation manifest sha256:c5efcbed6945268864bb800a87a0027f3677357ede6ad1ce77c5d44f0d83f41d                                                        0.0s
 => => exporting manifest list sha256:2a5ade4334baa8b9e1ee7e013e4b1f4386a6ba8d5574510551573ca89160d7a2                                                               0.0s
 => => naming to docker.io/library/nginx-install-ubuntu:1.5                                                                                                          0.0s
 => => unpacking to docker.io/library/nginx-install-ubuntu:1.5                                                                                                       0.0s

# 만들어진 이미지를 통해 컨테이너 생성
$ sudo docker run -p 8081:80 --name my-ubuntu-1-5 nginx-install-ubuntu:1.5

```

## 포트 매핑

#### 포트 설정

| 구분 | 포트 |
| --- | --- |
| 호스트 포트 | 8081 |
| 컨테이너 포트 | 80 |

#### 실행 명령어 및 결과

```bash
# 실행중인 컨테이너 확인 (포트 매핑 확인용)
$ sudo docker ps
CONTAINER ID   IMAGE                      COMMAND                  CREATED         STATUS                   PORTS                                     NAMES
3a9d49bad5ec   nginx-install-ubuntu:1.5   "nginx -g 'daemon of…"   5 minutes ago   Up 5 minutes (healthy)   0.0.0.0:8081->80/tcp, [::]:8081->80/tcp   my-ubuntu-1-5
```

#### 접속 결과

- 접속 주소: [http://localhost:8081]

![포트 매핑 접속 성공](../images/trouble_shooting/정상적으로%20나온%20화면.png)