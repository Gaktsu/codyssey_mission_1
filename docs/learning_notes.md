# 미션 1 - 학습 내용 정리

[← README로 돌아가기](../README.md)

본 문서는 미션 1의 학습 목표 6가지를 이해하고,
각 개념을 스스로 설명할 수 있도록 정리한 학습 노트이다.

---

## 절대 경로와 상대 경로

### 개념

- **절대 경로**는 최상위 루트 `/` 디렉터리부터 목적지 디렉터리 또는 파일까지의 전체 경로를 표현하는 방식
- **상대 경로**는 현재 디렉터리를 기준으로 목적지 디렉터리 또는 파일까지의 경로를 표현하는 방식 

### 용도

- **절대 경로**는 어느 디렉토리에 있어도 항상 같은 경로를 가리킬 때 사용된다
- **상대 경로**는 프로젝트 디렉토리 내에 존재하는 디렉토리 또는 파일에 접근할 때 사용된다 

---

## 파일 권한

### 개념

- 리눅스의 파일 권한은 효율적인 권한 관리를 위해 사용자를 **소유자(Owner)**, **그룹(Group)**, **기타 사용자(Other)**로 나누어 각각 권한을 부여한다
- 각 사용자별로 **읽기(r)**, **쓰기(w)**, **실행(x)** 권한을 부여한다

### 소유자 / 그룹 / 기타 사용자

- **소유자**는 디렉터리 또는 파일을 생성한 사용자이다.
- **그룹**은 작성자가 속해 있는 팀을 의미한다.
- **기타 사용자**는 소유자, 그룹에 속한자가 아닌 사용자를 의미한다

### (권한) 숫자 표기

- `chmod 777 abcd1122`와 같은 명령어의 `777`에 해당되는 부분을 의미한다.
- 각 숫자는 **자리**마다 서로 다른 의미를 지닌다
    - `100`의 자리 숫자는 **소유자**를 의미한다
    - `10`의 자리 숫자는 **그룹**을 의미한다
    - `1`의 자리 숫자는 **기타 사용자**를 의미한다

- 각 숫자는 **값**마다 서로 다른 의미를 지닌다
    - 숫자를 **2진수**로 다음과 같은 범위로 표현이 가능하다
    - `000(0)` ~ `111(7)`
    - 각 숫자는 **자리**마다 서로 다른 의미를 지닌다
        - `100`의 자리 숫자는 **읽기**를 의미한다
        - `10`의 자리 숫자는 **쓰기**를 의미한다
        - `1`의 자리 숫자는 **실행**을 의미한다
    - `7`은 **2진수**로 `111`로 표현이 되며 의미는 다음과 같다
        - **읽기**, **쓰기**, **실행** 권한 부여
    - `0`은 **2진수**로 `000`으로 표현이 되며 의미는 다음과 같다
        - **읽기**, **쓰기**, **실행** 권한 미부여

- 이제 처음의 명령어를 해석하면 다음과 같이 표현할 수 있다
    - 지정한 디렉토리 또는 파일에 대해 **소유자**, **그룹**, **기타 사용자** 모두에게 **읽기**, **쓰기**, **실행** 권한을 부여한다

--

## docker 명령어마다 sudo가 필요한 이유

**docker**의 핵심 프로그램이 리눅스의 관리자 권한으로 실행되기 때문이다.
**docker**는 리눅스 OS의 핵심 영역을 건드리는 작업을 하기 때문이다.

--

## docker의 attach와 exec의 차이

exec는 컨테이너에서 특정 프로그램을 실행시키는 명령어이다.
attach는 컨테이너를 작동할때 제일 먼저 실행되는 프로그램을 호스트의 터미널에서 조작할 수 있게 해주는 명령어이다.

### 실험 1 : nginx 이미지로 컨테이너를 만들고 실행한 뒤 attach를 하였을 경우

아무런 반응이 없었으며, 단순히 입력한것이 화면에 뜰 뿐이었다
`Ctrl+C`로 강제 종료하였을때 해당 컨테이너는 종료되는 것을 확인하였다.

#### 명령어와 출력

```bash
$ sudo docker attach nginx
dfds
fasd
fsa
q
^C2026/11/04 06:23:23 [notice] 1#1: signal 2 (SIGINT) received, exiting
2026/11/04 06:23:23 [notice] 29#29: exiting
2026/11/04 06:23:23 [notice] 29#29: exit
2026/11/04 06:23:23 [notice] 32#32: exiting
2026/11/04 06:23:23 [notice] 31#31: exiting
2026/11/04 06:23:23 [notice] 30#30: exiting
2026/11/04 06:23:23 [notice] 33#33: exiting
2026/11/04 06:23:23 [notice] 30#30: exit
2026/11/04 06:23:23 [notice] 32#32: exit
2026/11/04 06:23:23 [notice] 31#31: exit
2026/11/04 06:23:23 [notice] 33#33: exit
2026/11/04 06:23:23 [notice] 35#35: exiting
2026/11/04 06:23:23 [notice] 35#35: exit
2026/11/04 06:23:23 [notice] 34#34: exiting
2026/11/04 06:23:23 [notice] 36#36: exiting
2026/11/04 06:23:23 [notice] 36#36: exit
2026/11/04 06:23:23 [notice] 34#34: exit
2026/11/04 06:23:23 [notice] 1#1: signal 17 (SIGCHLD) received from 29
2026/11/04 06:23:23 [notice] 1#1: worker process 29 exited with code 0
2026/11/04 06:23:23 [notice] 1#1: signal 29 (SIGIO) received
2026/11/04 06:23:23 [notice] 1#1: signal 17 (SIGCHLD) received from 30
2026/11/04 06:23:23 [notice] 1#1: worker process 30 exited with code 0
2026/11/04 06:23:23 [notice] 1#1: signal 29 (SIGIO) received
2026/11/04 06:23:23 [notice] 1#1: signal 17 (SIGCHLD) received from 32
2026/11/04 06:23:23 [notice] 1#1: worker process 32 exited with code 0
2026/11/04 06:23:23 [notice] 1#1: signal 29 (SIGIO) received
2026/11/04 06:23:23 [notice] 1#1: signal 17 (SIGCHLD) received from 36
2026/11/04 06:23:23 [notice] 1#1: worker process 36 exited with code 0
2026/11/04 06:23:23 [notice] 1#1: signal 29 (SIGIO) received
2026/11/04 06:23:23 [notice] 1#1: signal 17 (SIGCHLD) received from 33
2026/11/04 06:23:23 [notice] 1#1: worker process 33 exited with code 0
2026/11/04 06:23:23 [notice] 1#1: signal 29 (SIGIO) received
2026/11/04 06:23:23 [notice] 1#1: signal 17 (SIGCHLD) received from 31
2026/11/04 06:23:23 [notice] 1#1: worker process 31 exited with code 0
2026/11/04 06:23:23 [notice] 1#1: signal 29 (SIGIO) received
2026/11/04 06:23:23 [notice] 1#1: signal 17 (SIGCHLD) received from 34
2026/11/04 06:23:23 [notice] 1#1: worker process 34 exited with code 0
2026/11/04 06:23:23 [notice] 1#1: signal 29 (SIGIO) received
2026/11/04 06:23:23 [notice] 1#1: signal 17 (SIGCHLD) received from 35
2026/11/04 06:23:23 [notice] 1#1: worker process 35 exited with code 0
2026/11/04 06:23:23 [notice] 1#1: exit
```

### 실험 2 : ubuntu 이미지로 컨테이너를 만들고 실행한 뒤 attach를 하였을 경우

**실험 1**과는 다르게 `root@<코드>` 가 나타나는 것을 확인하였다.

#### 명령어와 출력 

```bash
$ sudo docker run -dit -p 8080:80 --name ubuntu ubuntu:24.04
82e00a5070e6203e94f372e33e16ea6ebd39d5bbfdd8909813d1e38d143244af
$ sudo docker attach ubuntu
root@82e00a5070e6:/# 
```

### 실험 3 : nginx와 ubuntu의 bash 프로그램을 실행시켰을 경우

#### nginx

##### 명령어와 출력

```bash
$ sudo docker exec -it nginx bash
root@940797a0c4ff:/# 
```

#### ubuntu

###### 명령어와 출력

```bash
$ sudo docker exec -it ubuntu bash
root@82e00a5070e6:/# 
```

### 깨달은 점

`nginx`의 첫번째 프로세스는 `bash` 가 아니다.
`ubuntu`의 첫번째 프로세스는 `/bin/bash` 이다. 

`nginx`와 `ubuntu` 모두 bash 프로그램이 존재한
--

## Dockerfile으로 커스텀 이미지 만들기

프로젝트 루트의 [Dockerfile](../Dockerfile)을 사용한다. (작성 후 링크 동작 확인)

```dockerfile
# 이미지는 ubuntu:24.04으로 설정
FROM ubuntu:24.04

# 빌드 중 다음 명령어를 실행
RUN apt-get update -y && apt-get install nginx -y

# 환경 변수
ENV codyssey=minseong

# 포트 매핑을 80임을 보여줌 (실제로 80으로 매핑을 해주지는 않음)
EXPOSE 80

# localhost:80 으로 접속 시도 했지만 응답이 없을 경우 exit 1을 실행
# 응답을 3초동안 기다리며, 실패 후 재시도까지 30초를 대기한다
HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl -f http://localhost:80/ || exit 1

# 호스트에 있는 파일 index.html을 이미지의 디렉터리에 복사 붙여넣기
COPY ./index.html /var/www/html/index.html

# 첫번째 프로세스 설정
CMD ["/bin/bash"]
```

--

## 포트 매핑이 필요한 이유

외부(호스트 및 외부 네트워크)에서 컨테이너 내부로 접속하여 서로 통신할 수 있도록 통로를 열어주는 역할을 하기 때문이다 

--

## 바인드 마운트와 볼륨을 동시에 사용이 가능한가

### 실험

#### 명령어와 출력

```bash
# ~/Desktop/codyssey/:/bind-mount 으로 바인드 마운트를 함
# my-volume:/volume 으로 볼륨 마운트를 함
$ sudo docker run -it -v ~/Desktop/codyssey/:/bind-mount -v my-volume:/volume -p 1111:11 --name bind-mount-volume-container nginx-install-ubuntu:1.4
root@b6e5ea264d3b:/# cd volume/       
root@b6e5ea264d3b:/volume# cd ../bind-mount/
root@b6e5ea264d3b:/bind-mount# 
```

#### 결과

**바인드 마운트**, **볼륨** 동시에 마운트 하는것이 가능하다

--

## Git vs GitHub

Git은 내 컴퓨터에서만 커밋 후 상태를 버전별로 저장하여 관리하는 도구이다
GitHub은 프로젝트 폴더 내 디렉터리와 파일을 클라우드 저장을 하여 여러 사람이 보고, 수정하고, 협업할 수 있도록 하는 플랫폼이다 