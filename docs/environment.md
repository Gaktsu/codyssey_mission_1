# 실행 환경 상세 정보

[← README로 돌아가기](../README.md)

## 개발 환경 정보

| 구분 | 환경 |
| --- | --- |
| 운영체제(OS) | Ubuntu 24.04.4 LTS |
| Shell | Bash (/bin/bash) |
| 개발 도구 | Visual Studio Code |

#### 환경 확인 명령어 및 결과

```bash
# 운영체제 정보 확인 (OS 확인용)
$ cat /etc/os-release
PRETTY_NAME="Ubuntu 24.04.4 LTS"
NAME="Ubuntu"
VERSION_ID="24.04"
VERSION="24.04.4 LTS (Noble Numbat)"
VERSION_CODENAME=noble
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=noble
LOGO=ubuntu-logo

# 환경변수 SHELL의 데이터 확인 (shell 정보 확인용)
$ echo $SHELL
/bin/bash

```

## 도구 및 버전

| 도구 | 버전 |
| --- | --- |
| Docker | version 29.9.0 |
| Git | version 2.43.0 |
| Visual Studio Code | version 1.144.1 |

#### 버전 확인 명령어 및 결과

```bash
# docker의 버전 확인
$ docker --version

Docker version 29.9.0, build f415da8

# git의 버전 확인
$ git --version

git version 2.43.0

# vscode의 버전 확인 
$ code --version

1.144.1
261c84cb1eddf11235f9e2c921425e9663fbe556
x64
```