# 코디세이 미션 1 - 개발자 환경 세팅

## 1. 프로젝트 개요

Linux CLI, Docker, Git/GitHub를 활용해 개발 환경을 구축하고, 명령어 실행과 결과 검증을 통해 **재현 가능한 개발 환경**을 구성한다. 기술별 동작 원리를 설명하고 문제 해결 과정을 기록한다.

**최종 결과물:** Dockerfile 기반 웹 서버, 포트 매핑·마운트·볼륨 검증 증거, GitHub 연동 결과, 수행 기록 및 트러블슈팅 2건 이상.

### 디렉토리

| 디렉토리 | 역할 |
| --- | --- |
| `docs` | 실습 결과, 학습 내용 및 트러블 슈팅 기록 |
| `images` | 검증 스크린샷 보관 |
| `Dockerfile` | 커스텀 Docker 이미지 구성 |
| `index.html` | Nginx에서 제공할 웹 페이지 |
| `README.md` | 미션 개요 및 상세 문서 링크 |

## 2. 실행 환경

| 구분 | 환경 / 버전 |
| --- | --- |
| OS | Ubuntu 24.04.4 LTS |
| Shell | Bash (/bin/bash) |
| Docker / Git | version 29.9.0 / version 2.43.0 |
| 개발 도구 | Visual Studio Code (version 1.144.1) |

→ [환경 확인 명령어와 실제 출력](./docs/environment.md)

## 3. 수행 항목 체크리스트

- [x] **Linux CLI:** 파일·디렉토리 조작, 권한 변경 전후 검증
- [x] **Docker:** 설치·동작 점검, 이미지·컨테이너 운영, hello-world 및 Ubuntu 실습
- [x] **Dockerfile:** 직접 작성, 커스텀 이미지 빌드 및 실행, 포트 매핑 접속 검증
- [x] **데이터 관리:** 바인드 마운트 변경 반영, 볼륨 영속성 검증
- [x] **Git/GitHub:** Git 설정, VS Code 연동 및 원격 저장소 업로드
- [x] **문서화:** 명령어·출력·증거 기록, 트러블슈팅 2건 이상

## 4. 검증 방법

실습 기록은 아래 문서에 **명령어 + 실제 출력 결과(코드 블록)** 로 작성한다. 스크린샷은 기존 `image/` 폴더에 저장하고 해당 문서에서 연결한다.

| 항목 | 상세 기록 |
| --- | --- |
| Linux CLI / 파일 권한 | [Linux CLI 및 권한 검증](./docs/linux-cli.md) |
| Docker 환경 | [Docker 설치·운영 검증](./docs/docker.md) |
| Dockerfile / 포트 매핑 | [이미지 빌드 및 웹 접속 검증](./docs/dockerfile-port.md) |
| 바인드 마운트 / Docker 볼륨 | [데이터 관리 검증](./docs/storage.md) |
| Git/GitHub | [Git 설정 및 연동 검증](./docs/git-github.md) |

## 5. 트러블슈팅

- [트러블슈팅 사례 1 · 사례 2](./docs/troubleshooting.md) — 문제 → 원인 가설 → 확인 → 해결/대안 → 결과 검증

## 6. 학습 내용 정리 (선택)

- [6가지 목표 개념 정리](./docs/learning_notes.md) — 절대·상대 경로, 파일 권한, 커스텀 이미지, 포트 매핑, 볼륨, Git/GitHub

---

> **제출 전 확인:** 모든 링크가 열리는지, 명령어와 출력이 함께 있는지, 브라우저 캡처에 주소창과 응답이 보이는지, 토큰·비밀번호 등 민감정보가 없는지 확인한다.
