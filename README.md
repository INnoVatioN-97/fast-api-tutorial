# FastAPI 입문 튜토리얼 프로젝트

이 프로젝트는 Spring Boot, Node.js 등 다른 백엔드 프레임워크에 익숙한 개발자가 FastAPI의 핵심 개념을 빠르게 학습하고, 실제 면접에 대비할 수 있도록 설계된 핸즈온 튜토리얼입니다.

프로젝트는 외부 API를 호출하는 **탄력적 API 게이트웨이(Resilient API Gateway)**를 구축하는 과정을 담고 있으며, FastAPI의 주요 기능과 모범 사례를 적용합니다.

---

## 🚀 핵심 학습 목표

- **계층형 아키텍처:** 역할에 따른 코드 분리 (Models, Services, Routers)
- **데이터 유효성 검사:** Pydantic을 활용한 강력하고 자동화된 데이터 검증
- **비동기 프로그래밍:** `async`/`await`와 `httpx`를 이용한 논블로킹 I/O 처리
- **탄력성 설계:** 외부 API 장애에 대비한 "지수 백오프 재시도" 패턴 구현
- **의존성 주입:** `Depends`를 활용한 공통 로직(페이지네이션) 재사용
- **컨테이너화:** Docker를 이용한 애플리케이션 패키징 및 실행

## 📂 프로젝트 구조

```
.
├── Dockerfile          # Docker 이미지 설정을 위한 파일
├── .dockerignore       # Docker 빌드 시 제외할 파일 목록
├── main.py             # FastAPI 앱의 시작점 (라우터 포함)
├── models.py           # Pydantic 데이터 모델 (DTO) 정의
├── requirements.txt    # Python 의존성 목록
├── services.py         # 비즈니스 로직 (외부 API 호출 등)
├── routers/
│   └── gateway.py      # API 엔드포인트(라우트) 정의
└── wiki/                 # 학습 내용을 정리한 위키 문서
    └── ...
```

## ⚡️ 시작하기

### 1. 로컬 개발 환경

```bash
# 1. 가상환경 생성 및 활성화
python3 -m venv .venv
source .venv/bin/activate

# 2. 의존성 설치
pip install -r requirements.txt

# 3. 개발 서버 실행 (자동 리로드)
uvicorn main:app --reload
```

### 2. Docker 환경

```bash
# 1. Docker 이미지 빌드
docker build -t fastapi-tutorial-app .

# 2. Docker 컨테이너 실행
docker run -d -p 8000:8000 --name fastapi-container fastapi-tutorial-app

# 3. 애플리케이션 접속
# http://127.0.0.1:8000
```

---

## 💡 다른 프레임워크 경험자를 위한 FastAPI 핵심 포인트

#### 1. Pydantic: 단순한 DTO 그 이상
- **하나로 모든 것을 해결:** TypeScript의 `interface` + `class-validator` 조합과 달리, Pydantic 모델 하나만으로 **런타임 데이터 유효성 검사, 직렬화/역직렬화, 자동 API 문서 생성**까지 모두 처리합니다. 보일러플레이트 코드가 획기적으로 줄어듭니다.

#### 2. Async 네이티브 지원
- **Node.js와 유사한 경험:** 프레임워크 레벨에서 `async`/`await`를 완벽하게 지원합니다. I/O 바운드 작업이 많은 최신 웹 환경에서 별도의 설정 없이도 높은 처리량을 보여줍니다.

#### 3. 유연한 프로젝트 구조
- **"기본형" 프레임워크:** Django나 NestJS처럼 정해진 구조를 강요하지 않습니다. 개발자가 필요에 따라 구조를 직접 만들어가야 합니다. 하지만 프로젝트가 성장하면 결국 **기능별(Domain-based) 모듈 구조**로 수렴하는 경향을 보이며, 이는 다른 프레임워크에서의 설계 경험이 큰 자산이 됨을 의미합니다.

#### 4. 함수 기반 의존성 주입 (DI)
- **클래스가 아닌 함수:** Spring/NestJS의 클래스 기반 DI와 달리, FastAPI는 `Depends()`를 사용하는 **함수 기반 DI** 시스템을 사용합니다. 이는 더 유연하고, 간결하며, Python의 특징을 잘 살린 독특한 방식입니다. 이 프로젝트에서는 공통 페이지네이션 로직을 의존성으로 분리하여 코드 재사용성을 높였습니다.
