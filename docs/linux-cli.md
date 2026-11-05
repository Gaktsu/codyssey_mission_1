# Linux CLI 및 파일 권한 검증

[← README로 돌아가기](../README.md)

## Linux CLI

#### 주요 사용 명령어

`pwd`, `ls -la`, `cd`, `mkdir`, `touch`, `cp`, `mv`, `rm`, `cat`

#### 실행 명령어 및 결과

```bash

# 현재 절대 경로를 출력한다 
$ pwd
/home/minsung/Desktop/codyssey/codyssey_mission_1

# 현재 디렉토리 내 하위 디렉토리 및 파일들의 이름을 출력한다
$ ls
docs  images  README.md

# 현재 디렉토리 내 모든 하위 디렉토리 및 파일들의 이름을 출력한다
# 차이점은 숨겨진 디렉토리 또는 파일들도 출력한다
# -a는 all의 약자이다
$ ls -a
.  ..  docs  .env  .git  .gitignore  images  README.md

# 현재 디렉토리 내 하위 디렉토리 및 파일들의 상세 정보들을 출력한다
# 왼쪽부터 [파일 종류 및 권한] [링크 수] [소유자 이름] [그룹 이름] [파일 크기] [마지막 수정 시간] [파일/디렉토리명]
$ ls -l
total 12
drwxrwxr-x 2 minsung minsung 4096 Nov  3 17:03 docs
drwxrwxr-x 4 minsung minsung 4096 Nov  3 11:32 images
-rw-r--r-- 1 minsung minsung 2665 Nov  3 08:00 README.md

# 현재 디렉토리 내 모든 하위 디렉토리 및 파일들의 상세 정보들을 출력한다
$ ls -al
total 32
drwxrwxr-x 5 minsung minsung 4096 Nov  3 17:03 .
drwxrwxr-x 3 minsung minsung 4096 Nov  3 10:50 ..
drwxrwxr-x 2 minsung minsung 4096 Nov  3 17:03 docs
-rw-rw-r-- 1 minsung minsung   56 Nov  3 16:33 .env
drwxrwxr-x 8 minsung minsung 4096 Nov  3 16:38 .git
-rw-rw-r-- 1 minsung minsung  326 Nov  3 16:37 .gitignore
drwxrwxr-x 4 minsung minsung 4096 Nov  3 11:32 images
-rw-r--r-- 1 minsung minsung 2665 Nov  3 08:00 README.md

# 따로 출력되는 것은 없었으나, 현재 경로가 ~ 으로 변경된 것을 확인
$ cd

# 따로 출력되는 것은 없었으나, 현재 경로가 위와 같이 변경된 것을 확인
$ cd ~/Desktop/codyssey/codyssey_mission_1

# 디렉토리가 아닌 파일로 이동을 시도하였다
$ cd README.md
bash: cd: README.md: Not a directory

# 현재 경로에 존재하지 않는 디렉토리로 이동을 시도하였다
$ cd nothing
bash: cd: nothing: No such file or directory

# 디렉토리를 생성을 시도하였다
$ mkdir
mkdir: missing operand
Try 'mkdir --help' for more information.

# 따로 출력되는 것은 없었으나, abcd 라는 이름의 디렉토리가 생성되는 것을 확인 
$ mkdir abcd

# 따로 출력되는 것은 없었으나, 1122abcd 라는 이름의 빈 파일이 생성되는 것을 확인
$ touch 1122abcd

# 디렉토리 또는 파일에 대한 복사 붙여넣기를 시도하였다
$ cp
cp: missing file operand
Try 'cp --help' for more information.

# 따로 출력되는 것은 없었으나, 1122abcd 파일의 내용 그대로 abcd1122 파일에 작성된 채로 생성된 것을 확인
$ cp 1122abcd ./abcd1122

# 디렉토리 또는 파일을 이동하는 것을 시도하였다
$ mv
mv: missing file operand
Try 'mv --help' for more information.

# 따로 출력되는 것은 없었으나, 1122abcd 파일이 상위 디렉토리에 이동된 것을 확인
$ mv 1122abcd ../1122abcd

# 디렉토리 또는 파일을 삭제하는 것을 시도하였다
$ rm
rm: missing operand
Try 'rm --help' for more information.

# 디렉토리가 삭제되지 않는 것을 확인하였다 
$ rm abcd
rm: cannot remove 'abcd': Is a directory

# 따로 출력되는 것은 없었으나, abcd 폴더가 삭제된 것을 확인
# -r은 Recursive의 약자로 디렉토리 내 하위 디렉토리 또는 파일들을 모두 제거한 후 해당 디렉토리도 제거한다
$ rm -r abcd

# 따로 출력되는 것은 없었으나, abcd1122 파일이 삭제된 것을 확인
$ rm abcd1122

# 상위 디렉토리로 옮긴 1122abcd 파일을 복사하여 abcd1122 파일을 다시 생성
$ cp ../1122abcd ./abcd1122

# 따로 출력되는 것은 없었으나, abcd1122 파일이 삭제된 것을 확인
$ rm -r abcd1122

# 권한 실습에 사용할 abcd1122 파일을 다시 생성하고 내용을 작성
$ cp ../1122abcd ./abcd1122
$ printf 'hello codyssey!' > abcd1122

# abcd1122파일 내용이 출력되는 것을 확인
$ cat abcd1122
hello codyssey!

```

#### 결과 정리

`pwd`   : 현재 디렉토리의 절대 경로를 출력하는 명령어이다.
`ls`    : 현재 디렉토리 내에 존재하는 하위 디렉토리 및 파일들을 출력하는 명령어이다.
`cd`    : 지정된 경로로 현재 위치를 이동시는 명령어이다.  
`mkdir` : 디렉토리를 생성하는 명령어이다.
`touch` : 파일을 생성하는 명령어이다.
`cp`    : 디렉토리 또는 파일을 다른 경로에 복사 붙여넣기 하는 명령어이다.
`mv`    : 디렉토리 또는 파일을 다른 경로로 이동시키는 명령어이다. (또한 디렉토리 또는 파일명 변경이 가능하다.)
`rm`    : 디렉토리 또는 파일을 삭제하는 명령어이다.
`cat`   : 파일 내용을 출력하는 명령어이다.

## 파일 권한

#### 주요 사용 명령어

`ls -l`, `ls -ld`, `chmod`

#### 파일 권한 변경 전후 비교

```bash
# -rw-rw-r--
$ ls -l abcd1122
-rw-rw-r-- 1 minsung minsung 15 Nov  3 17:56 abcd1122

$ chmod 777 abcd1122

# -rwxrwxrwx로 바뀐것을 확인
$ ls -l abcd1122
-rwxrwxrwx 1 minsung minsung 15 Nov  3 17:56 abcd1122

# 따로 출력되는 것은 없었으나, abcd1122에서 2211dcba 로 이름이 변경되는 것을 확인
$ mv abcd1122 2211dcba
```

#### 디렉토리 권한 변경 전후 비교

```bash
# 권한이 rwxrwxr-x 이다
$ ls -ld
drwxrwxr-x 5 minsung minsung 4096 Nov  3 17:56 .

$ chmod 751 ./

# 권한이 rwxr-x--x로 변경되었다 
$ ls -ld
drwxr-x--x 5 minsung minsung 4096 Nov  3 17:56 .
```