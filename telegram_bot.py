import asyncio
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from config import Config
from openai_service import OpenAIService
import schedule
import time
from datetime import datetime

# 로깅 설정
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class MindfulBot:
    """마음챙김 텔레그램 봇"""
    
    def __init__(self):
        """봇 초기화"""
        self.openai_service = OpenAIService()
        self.application = None
        
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """봇 시작 명령어 처리"""
        welcome_message = """
        💖 마음챙김 챗봇에 오신 것을 환영합니다!
        
        이 봇은 매일매일 당신에게 긍정적인 메시지를 전달해드립니다.
        
        사용 가능한 명령어:
        /start - 봇 시작
        /message - 지금 바로 긍정적인 메시지 받기
        /affirmation - 자기 확언 받기
        /help - 도움말 보기
        
        매시 30분마다 자동으로 긍정적인 메시지가 전송됩니다! ✨
        """
        await update.message.reply_text(welcome_message)
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """도움말 명령어 처리"""
        help_message = """
        💖 마음챙김 챗봇 도움말
        
        📋 명령어 목록:
        /start - 봇 시작하기
        /message - 긍정적인 메시지 받기
        /affirmation - 자기 확언 받기
        /help - 이 도움말 보기
        
        ⏰ 자동 메시지:
        매시 30분마다 자동으로 긍정적인 메시지가 전송됩니다.
        
        💡 팁:
        이 봇을 그룹 채팅에 추가하면 모든 멤버가 함께 긍정적인 에너지를 나눌 수 있어요!
        """
        await update.message.reply_text(help_message)
    
    async def send_message_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """수동으로 긍정적인 메시지 전송"""
        try:
            message = self.openai_service.generate_positive_message()
            await update.message.reply_text(f"💖 {message}")
        except Exception as e:
            logger.error(f"메시지 생성 중 오류 발생: {e}")
            await update.message.reply_text("죄송합니다. 메시지를 생성하는 중 오류가 발생했습니다. 잠시 후 다시 시도해주세요.")
    
    async def send_affirmation_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """자기 확언 메시지 전송"""
        try:
            affirmation = self.openai_service.generate_daily_affirmation()
            await update.message.reply_text(f"✨ {affirmation}")
        except Exception as e:
            logger.error(f"자기 확언 생성 중 오류 발생: {e}")
            await update.message.reply_text("죄송합니다. 자기 확언을 생성하는 중 오류가 발생했습니다. 잠시 후 다시 시도해주세요.")
    
    async def send_scheduled_message(self, context: ContextTypes.DEFAULT_TYPE):
        """스케줄된 메시지 전송"""
        try:
            message = self.openai_service.generate_positive_message()
            
            # 그룹 채팅 ID가 설정되어 있으면 그룹에 전송
            if Config.GROUP_CHAT_ID:
                await context.bot.send_message(
                    chat_id=Config.GROUP_CHAT_ID,
                    text=f"💖 {message}"
                )
                logger.info(f"그룹 채팅에 스케줄 메시지 전송: {Config.GROUP_CHAT_ID}")
            else:
                logger.info("GROUP_CHAT_ID가 설정되지 않아 스케줄 메시지를 전송하지 않습니다.")
                
        except Exception as e:
            logger.error(f"스케줄 메시지 전송 중 오류 발생: {e}")
    
    def setup_handlers(self):
        """명령어 핸들러 설정"""
        # 명령어 핸들러 등록
        self.application.add_handler(CommandHandler("start", self.start_command))
        self.application.add_handler(CommandHandler("help", self.help_command))
        self.application.add_handler(CommandHandler("message", self.send_message_command))
        self.application.add_handler(CommandHandler("affirmation", self.send_affirmation_command))
    
    def setup_scheduler(self):
        """스케줄러 설정"""
        # 매시 30분마다 메시지 전송
        schedule.every().hour.at(":30").do(
            lambda: asyncio.create_task(self.send_scheduled_message(None))
        )
        
        logger.info("스케줄러가 설정되었습니다. 매시 30분마다 메시지가 전송됩니다.")
    
    async def run_scheduler(self):
        """스케줄러 실행"""
        while True:
            schedule.run_pending()
            await asyncio.sleep(60)  # 1분마다 스케줄 확인
    
    async def start_bot(self):
        """봇 시작"""
        try:
            # 환경 변수 검증
            Config.validate()
            
            # 텔레그램 봇 애플리케이션 생성
            self.application = Application.builder().token(Config.TELEGRAM_BOT_TOKEN).build()
            
            # 핸들러 설정
            self.setup_handlers()
            
            # 스케줄러 설정
            self.setup_scheduler()
            
            logger.info("마음챙김 챗봇이 시작되었습니다!")
            
            # 봇 시작
            await self.application.initialize()
            await self.application.start()
            await self.application.updater.start_polling()
            
            # 스케줄러 실행
            await self.run_scheduler()
            
        except Exception as e:
            logger.error(f"봇 시작 중 오류 발생: {e}")
            raise
    
    async def stop_bot(self):
        """봇 중지"""
        if self.application:
            await self.application.updater.stop()
            await self.application.stop()
            await self.application.shutdown()
            logger.info("봇이 중지되었습니다.")

# 봇 인스턴스 생성
bot = MindfulBot()

async def main():
    """메인 함수"""
    try:
        await bot.start_bot()
    except KeyboardInterrupt:
        logger.info("사용자에 의해 봇이 중지되었습니다.")
    except Exception as e:
        logger.error(f"예상치 못한 오류 발생: {e}")
    finally:
        await bot.stop_bot()

if __name__ == "__main__":
    asyncio.run(main())
