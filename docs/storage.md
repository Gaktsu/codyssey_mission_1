# 바인드 마운트 및 Docker 볼륨 검증

[← README로 돌아가기](../README.md)

## 바인드 마운트

#### 실행 명령어 및 결과

```bash
$ sudo docker run -it -v ~/Desktop/bind-mount:/bind-mount -p 1234:56 --name bind-mount-test nginx-install-ubuntu:1.4

$ sudo touch ~/Desktop/bind-mount/hello-codyssey.txt

# 호스트에서 파일에 내용을 작성한 뒤 컨테이너에서 확인
$ sudo docker exec -it bind-mount-test bash
root@9eb6e5016749:/# cd bind-mount/
root@9eb6e5016749:/bind-mount# cat hello-codyssey.txt 
코디세이 화이팅!

root@9eb6e5016749:/bind-mount# echo cody-ssey fighting! >> hello-codyssey.txt
root@9eb6e5016749:/bind-mount# cat hello-codyssey.txt 
코디세이 화이팅!
cody-ssey fighting!

# 컨테이너에서 추가한 내용이 호스트에 반영되었는지 확인
$ cat ~/Desktop/bind-mount/hello-codyssey.txt
코디세이 화이팅!
cody-ssey fighting!
```

## Docker 볼륨

#### 실행 명령어 및 결과

```bash
# 볼륨 생성
$ sudo docker volume create my-volume
my-volume

# 생성 확인
$ sudo docker volume ls
DRIVER    VOLUME NAME
local     docker-compose-practice_web_data
local     my-volume
local     project_mysql_data
local     project_qdrant_data

# 볼륨을 마운트한 컨테이너 생성 
# 마운트 확인
# 파일 생성
$ sudo docker run -it -v my-volume:/container-storate -p 4545:45 --name volume-connect-test nginx-install-ubuntu:1.4
root@aeb512c8c919:/# cd container-storate
root@aeb512c8c919:/container-storate# 
root@aeb512c8c919:/container-storate# touch hello-codyssey.txt

# 컨테이너 종료(exit) 후 제거
$ sudo docker rm volume-connect-test

# 동일 볼륨을 마운트한 새로운 컨테이너 생성
# 마운트 확인
# 이전에 생성한 파일 확인
$ sudo docker run -it -v my-volume:/container-storate -p 4545:45 --name container-delete-after nginx-install-ubuntu:1.4
root@2bcbd3df01a7:/# cd container-storate/
root@2bcbd3df01a7:/container-storate# cat hello-codyssey.txt 
hellotouch hello-codyssey.txt! codyssey
root@2bcbd3df01a7:/container-storate# 

# 다른 컨테이너에서 파일 삭제
$ sudo docker run -it -v my-volume:/storage -p 6575:85 --name container-volume nginx-install-ubuntu:1.4
root@f35644de2b7c:/# cd storage/
root@f35644de2b7c:/storage# rm hello-codyssey.txt 

# 파일 제거가 되었는지 확인
$ sudo docker exec -it container-delete-after bash
root@2bcbd3df01a7:/# cd container-storate/
root@2bcbd3df01a7:/container-storate# cat hello-codyssey.txt
cat: hello-codyssey.txt: No such file or directory
```

#### 결과 해석

- **볼륨**은 컨테이너에 종속되지 않는다
    - 컨테이너가 제거되더라도 볼륨 내 데이터에 영향을 주지 않는다
- **볼륨**은 **영속성**을 보장한다
- **볼륨**에 직접 접근하여 제거를 시도하면 사라진다 

<영속성> : 비휘발성 장치에 데이터가 계속 존재하게 하는 특성
