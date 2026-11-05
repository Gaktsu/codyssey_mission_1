# Git 및 GitHub 연동 검증

[← README로 돌아가기](../README.md)

## Git/GitHub

#### Git 설정 명령어 및 결과

```bash
# 사용자 정보 설정 후 확인한 명령어/출력
$ git config --list
user.email=******@naver.com
user.name=Gaktsu
credential.helper=cache --timeout=3600
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
remote.origin.url=https://github.com/Gaktsu/codyssey_mission_1.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.main.remote=origin
branch.main.merge=refs/heads/main
branch.main.vscode-merge-base=origin/main
```

#### GitHub 저장소 연동 확인

```bash
# 연동된 레포지터리의 정보 확인
$ git remote -v
origin  https://github.com/Gaktsu/codyssey_mission_1.git (fetch)
origin  https://github.com/Gaktsu/codyssey_mission_1.git (push)

# 연동된 레포지터리에 없는 모 커밋을 업로드
$ git push
Enumerating objects: 24, done.
Counting objects: 100% (24/24), done.
Delta compression using up to 8 threads
Compressing objects: 100% (18/18), done.
Writing objects: 100% (20/20), 82.28 KiB | 16.46 MiB/s, done.
Total 20 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/Gaktsu/codyssey_mission_1.git
   b67cdbb..18475b4  main -> main
```

#### VS Code 및 GitHub 연동 결과

![github과 vscode 연동 확인](../images/git_github/github과%20vscode%20연동%20확인.png)
