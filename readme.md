# 💖 마음챙김 챗봇: 매일매일 자존감 한 스푼

## 📋 프로젝트 개요

마음챙김 챗봇은 바쁜 일상 속에서 자신을 잃어가는 사람들을 위해 매일 긍정적인 메시지를 전달하는 텔레그램 봇입니다. OpenAI의 강력한 언어 모델(LLM)을 활용하여 사용자의 마음을 어루만지는 자기 확언, 명언, 또는 긍정적인 메시지를 생성하고, 정해진 시간마다 그룹 채팅방에 자동으로 전송합니다.

## ✨ 주요 기능

- **자동 메시지 전송**: 매시 30분마다 설정된 그룹 채팅방에 자동으로 메시지를 전송합니다.
- **AI 기반 메시지 생성**: OpenAI의 GPT-4o-mini 모델을 이용해 독창적이고 긍정적인 메시지를 생성합니다.
- **1:N 그룹 서비스**: 1:1 채팅뿐만 아니라 그룹 채팅방에서도 사용할 수 있어 여러 사람과 함께 긍정적인 에너지를 나눌 수 있습니다.
- **다양한 메시지 유형**: 자기 확언, 명언, 격려의 말 등 다양한 형태의 긍정적인 메시지를 제공합니다.

## 🛠️ 기술 스택

### 언어 및 라이브러리
- **Python 3.11+**
- **python-telegram-bot**: 텔레그램 봇 기능 구현
- **openai**: OpenAI API 통신
- **schedule**: 스케줄링 기능
- **python-dotenv**: 환경 변수 관리

### 호스팅
- **Railway**: PaaS 클라우드 서비스

## 🚀 빠른 시작

### 1. 저장소 클론
```bash
git clone <repository-url>
cd weird
```

### 2. 의존성 설치
```bash
pip install -r requirements.txt
```

### 3. 환경 변수 설정
`.env` 파일을 생성하고 다음 내용을 입력하세요:
```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
OPENAI_API_KEY=your_openai_api_key_here
GROUP_CHAT_ID=your_group_chat_id_here
MESSAGE_INTERVAL=30
```

### 4. 봇 실행
```bash
python weird.py
```

## 📱 사용법

### 개인 채팅 명령어
- `/start` - 봇 시작
- `/message` - 긍정적인 메시지 받기
- `/affirmation` - 자기 확언 받기
- `/help` - 도움말 보기

### 그룹 채팅
1. 봇을 그룹에 추가
2. 환경 변수에 `GROUP_CHAT_ID` 설정
3. 매시 30분마다 자동으로 메시지 전송

## 🚀 Railway 배포

자세한 배포 가이드는 [DEPLOYMENT.md](DEPLOYMENT.md)를 참고하세요.

## 📁 프로젝트 구조

```
weird/
├── weird.py              # 메인 실행 파일
├── telegram_bot.py       # 텔레그램 봇 메인 코드
├── openai_service.py     # OpenAI API 서비스
├── config.py             # 환경 변수 설정
├── requirements.txt      # Python 의존성
├── railway.json          # Railway 배포 설정
├── Procfile              # Railway 프로세스 설정
├── runtime.txt           # Python 버전 설정
├── DEPLOYMENT.md         # 배포 가이드
└── readme.md            # 프로젝트 문서
```

## 🔧 API 요구사항

- **Telegram Bot API**: BotFather를 통해 발급받은 API Token 필요
- **OpenAI API**: OpenAI 계정과 API Key 필요

## ⚠️ 보안 주의사항

- **환경 변수**: API 키와 토큰을 코드에 하드코딩하지 마세요
- **사용자 제한**: `ALLOWED_USER_IDS`로 비밀 명령어 사용자 제한
- **API 제한**: 하루 최대 100회, 5초 간격 제한으로 크레딧 보호
- **로그 모니터링**: 권한 없는 접근 시도 로그 확인

## 💡 주요 특징

- **에러 처리**: API 호출 실패 시 기본 메시지로 대체
- **로깅**: 상세한 로그 기록으로 디버깅 지원
- **확장성**: 새로운 메시지 유형 쉽게 추가 가능
- **안정성**: 예외 처리 및 재시도 로직 포함

## 🤝 기여하기

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.

## 💖 감사의 말

이 프로젝트는 모든 사람이 매일 조금씩 더 나은 하루를 보낼 수 있도록 도와주는 것을 목표로 합니다. 여러분의 피드백과 기여를 환영합니다!