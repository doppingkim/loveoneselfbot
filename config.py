import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

class Config:
    """환경 변수 설정 클래스"""
    
    # 텔레그램 봇 토큰
    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN') or os.getenv('TELEGRAM_BOT_TOKEN')
    
    # OpenAI API 키
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY') or os.getenv('OPENAI_API_KEY')
    
    # 그룹 채팅 ID (선택사항)
    GROUP_CHAT_ID = os.getenv('GROUP_CHAT_ID') or os.getenv('GROUP_CHAT_ID')
    
    # 메시지 전송 간격 (분 단위)
    MESSAGE_INTERVAL = int(os.getenv('MESSAGE_INTERVAL', 60))
    
    @classmethod
    def debug_env_vars(cls):
        """환경 변수 디버깅용"""
        print("🔍 환경 변수 디버깅:")
        print(f"TELEGRAM_BOT_TOKEN: {cls.TELEGRAM_BOT_TOKEN[:10] if cls.TELEGRAM_BOT_TOKEN else 'None'}...")
        print(f"OPENAI_API_KEY: {cls.OPENAI_API_KEY[:10] if cls.OPENAI_API_KEY else 'None'}...")
        print(f"GROUP_CHAT_ID: {cls.GROUP_CHAT_ID}")
        print(f"MESSAGE_INTERVAL: {cls.MESSAGE_INTERVAL}")
        print("=" * 50)
    
    @classmethod
    def validate(cls):
        """필수 환경 변수 검증"""
        if not cls.TELEGRAM_BOT_TOKEN or cls.TELEGRAM_BOT_TOKEN == "your_telegram_bot_token_here":
            raise ValueError("TELEGRAM_BOT_TOKEN이 설정되지 않았습니다.")
        # OPENAI_API_KEY는 선택사항으로 변경 (기본 메시지 사용 가능)
        return True
