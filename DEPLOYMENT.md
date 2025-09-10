# 🚀 Railway 배포 가이드

## 1. 텔레그램 봇 생성

1. 텔레그램에서 [@BotFather](https://t.me/botfather)와 대화
2. `/newbot` 명령어로 새 봇 생성
3. 봇 이름과 사용자명 설정
4. 받은 토큰을 안전하게 보관

## 2. OpenAI API 키 발급

1. [OpenAI 웹사이트](https://platform.openai.com/) 방문
2. 계정 생성 및 로그인
3. API Keys 섹션에서 새 키 생성
4. 받은 API 키를 안전하게 보관

## 3. Railway 배포

### 3.1 Railway 계정 생성
1. [Railway](https://railway.app/) 방문
2. GitHub 계정으로 로그인

### 3.2 프로젝트 배포
1. "New Project" 클릭
2. "Deploy from GitHub repo" 선택
3. 이 프로젝트 저장소 선택
4. 배포 시작

### 3.3 환경 변수 설정
Railway 대시보드에서 다음 환경 변수들을 설정:

```
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
OPENAI_API_KEY=your_openai_api_key_here
GROUP_CHAT_ID=your_group_chat_id_here (선택사항)
MESSAGE_INTERVAL=30
```

### 3.4 그룹 채팅 ID 확인 (선택사항)
1. 봇을 그룹에 추가
2. 그룹에서 메시지 전송
3. `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates` 방문
4. 응답에서 `chat.id` 값 확인

## 4. 봇 사용법

### 4.1 개인 채팅
- `/start` - 봇 시작
- `/message` - 긍정적인 메시지 받기
- `/affirmation` - 자기 확언 받기
- `/help` - 도움말 보기

### 4.2 그룹 채팅
- 봇을 그룹에 추가
- 환경 변수에 `GROUP_CHAT_ID` 설정
- 매시 30분마다 자동으로 메시지 전송

## 5. 모니터링

Railway 대시보드에서 다음을 확인할 수 있습니다:
- 로그 확인
- 리소스 사용량
- 배포 상태
- 환경 변수 관리

## 6. 문제 해결

### 6.1 봇이 응답하지 않는 경우
- 환경 변수가 올바르게 설정되었는지 확인
- Railway 로그에서 오류 메시지 확인
- 텔레그램 봇 토큰이 유효한지 확인

### 6.2 OpenAI API 오류
- API 키가 유효한지 확인
- API 사용량 한도 확인
- 계정에 충분한 크레딧이 있는지 확인

### 6.3 스케줄 메시지가 전송되지 않는 경우
- `GROUP_CHAT_ID`가 올바르게 설정되었는지 확인
- 봇이 그룹에 추가되어 있는지 확인
- 봇이 그룹에서 메시지를 전송할 권한이 있는지 확인

## 7. 비용 관리

- Railway: 무료 티어 제공 (월 5달러 크레딧)
- OpenAI API: 사용량에 따라 과금 (GPT-4o-mini는 저렴)
- 텔레그램 봇: 무료

## 8. 보안 주의사항

- 환경 변수에 민감한 정보 저장
- API 키를 코드에 하드코딩하지 않기
- 정기적으로 API 키 갱신
- 불필요한 권한 부여하지 않기
