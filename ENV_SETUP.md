# 🔧 환경 변수 설정 가이드

## 📋 필수 환경 변수

프로젝트를 실행하기 위해 다음 환경 변수들을 설정해야 합니다.

### 1. 텔레그램 봇 토큰
```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
```

**설정 방법:**
1. 텔레그램에서 [@BotFather](https://t.me/botfather)와 대화
2. `/newbot` 명령어로 새 봇 생성
3. 봇 이름과 사용자명 설정
4. 받은 토큰을 위 값으로 교체

**토큰 예시:**
```
1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
```

### 2. OpenAI API 키
```env
OPENAI_API_KEY=your_openai_api_key_here
```

**설정 방법:**
1. [OpenAI 웹사이트](https://platform.openai.com/) 방문
2. 계정 생성 및 로그인
3. API Keys 섹션에서 새 키 생성
4. 받은 API 키를 위 값으로 교체

**API 키 예시:**
```
sk-1234567890abcdefghijklmnopqrstuvwxyz
```

## 🔧 선택적 환경 변수

### 3. 그룹 채팅 ID (선택사항)
```env
GROUP_CHAT_ID=your_group_chat_id_here
```

**설정 방법:**
1. 봇을 그룹에 추가
2. 그룹에서 아무 메시지나 전송
3. 다음 URL 방문: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
4. 응답에서 `chat.id` 값 확인 (보통 음수)
5. 해당 값을 위에 입력

**채팅 ID 예시:**
```
-1001234567890
```

### 4. 메시지 전송 간격
```env
MESSAGE_INTERVAL=30
```

**설명:**
- 메시지 전송 간격을 분 단위로 설정
- 기본값: 30분
- 30분마다 자동으로 메시지 전송

### 5. 봇 언어 설정
```env
BOT_LANGUAGE=ko
```

**설명:**
- 봇의 기본 언어 설정
- 기본값: ko (한국어)

### 6. 로그 레벨
```env
LOG_LEVEL=INFO
```

**설정값:**
- `DEBUG`: 상세한 디버그 정보
- `INFO`: 일반적인 정보 (기본값)
- `WARNING`: 경고 메시지
- `ERROR`: 오류 메시지만

## 📁 환경 변수 파일 생성

### 로컬 개발용
프로젝트 루트에 `.env` 파일을 생성하고 다음 내용을 입력하세요:

```env
# 텔레그램 봇 토큰
TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz

# OpenAI API 키
OPENAI_API_KEY=sk-1234567890abcdefghijklmnopqrstuvwxyz

# 그룹 채팅 ID (선택사항)
GROUP_CHAT_ID=-1001234567890

# 메시지 전송 간격 (분)
MESSAGE_INTERVAL=30

# 봇 언어
BOT_LANGUAGE=ko

# 로그 레벨
LOG_LEVEL=INFO
```

### Railway 배포용
Railway 대시보드에서 환경 변수를 설정하세요:

1. Railway 프로젝트 대시보드 접속
2. "Variables" 탭 클릭
3. 각 환경 변수를 추가:
   - `TELEGRAM_BOT_TOKEN`: 실제 봇 토큰
   - `OPENAI_API_KEY`: 실제 API 키
   - `GROUP_CHAT_ID`: 그룹 채팅 ID (선택사항)
   - `MESSAGE_INTERVAL`: 30
   - `BOT_LANGUAGE`: ko
   - `LOG_LEVEL`: INFO

## ⚠️ 보안 주의사항

1. **`.env` 파일을 Git에 커밋하지 마세요**
   - `.gitignore`에 `.env` 추가
   - 민감한 정보가 포함되어 있습니다

2. **API 키 보안**
   - API 키를 코드에 하드코딩하지 마세요
   - 정기적으로 API 키를 갱신하세요
   - 불필요한 권한을 부여하지 마세요

3. **환경 변수 검증**
   - 봇 시작 전 필수 환경 변수가 설정되었는지 확인
   - 잘못된 값이 있으면 오류 메시지 출력

## 🧪 환경 변수 테스트

환경 변수가 올바르게 설정되었는지 확인하려면:

```bash
python -c "from config import Config; Config.validate(); print('환경 변수 설정 완료!')"
```

성공하면 "환경 변수 설정 완료!" 메시지가 출력됩니다.

## 🔍 문제 해결

### 환경 변수가 인식되지 않는 경우
1. `.env` 파일이 프로젝트 루트에 있는지 확인
2. 파일명이 정확한지 확인 (`.env`, `.env.local` 등)
3. 파일 인코딩이 UTF-8인지 확인

### API 키 오류
1. API 키가 올바른지 확인
2. OpenAI 계정에 충분한 크레딧이 있는지 확인
3. API 키 권한이 올바른지 확인

### 텔레그램 봇 오류
1. 봇 토큰이 올바른지 확인
2. 봇이 활성화되어 있는지 확인
3. 봇이 그룹에 추가되어 있는지 확인
