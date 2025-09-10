import openai
from config import Config
import random

class OpenAIService:
    """OpenAI API를 활용한 긍정적인 메시지 생성 서비스"""
    
    def __init__(self):
        """OpenAI 클라이언트 초기화"""
        openai.api_key = Config.OPENAI_API_KEY
        self.client = openai.OpenAI(api_key=Config.OPENAI_API_KEY)
    
    def generate_positive_message(self) -> str:
        """긍정적인 메시지 생성"""
        
        # 다양한 메시지 유형
        message_types = [
            "자존감을 높이는 자기 확언",
            "일상에 힘이 되는 명언",
            "마음을 따뜻하게 하는 격려의 말",
            "오늘 하루를 위한 긍정적인 메시지",
            "자신을 사랑하는 방법에 대한 조언"
        ]
        
        # 랜덤하게 메시지 유형 선택
        message_type = random.choice(message_types)
        
        prompt = f"""
        다음 조건에 맞는 {message_type}을 한국어로 작성해주세요:
        
        1. 50-100자 내외의 간결한 메시지
        2. 따뜻하고 긍정적인 톤
        3. 일상에서 실천할 수 있는 내용
        4. 이모지 1-2개 포함
        5. 격려와 희망을 주는 내용
        
        메시지만 작성해주세요. 다른 설명은 필요하지 않습니다.
        """
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "당신은 따뜻하고 긍정적인 마음챙김 코치입니다. 사용자에게 힘이 되는 메시지를 전달하는 것이 목표입니다."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150,
                temperature=0.8
            )
            
            message = response.choices[0].message.content.strip()
            return message
            
        except Exception as e:
            # API 호출 실패 시 기본 메시지 반환
            fallback_messages = [
                "오늘도 당신은 충분히 훌륭합니다! 💖",
                "작은 진전도 진전입니다. 조금씩 나아가세요! 🌱",
                "당신의 노력은 반드시 빛을 발할 거예요! ✨",
                "오늘 하루도 자신을 사랑하며 보내세요! 💕",
                "모든 순간이 당신을 성장시키고 있어요! 🌟"
            ]
            return random.choice(fallback_messages)
    
    def generate_daily_affirmation(self) -> str:
        """일일 자기 확언 메시지 생성"""
        prompt = """
        오늘을 위한 자기 확언을 한국어로 작성해주세요:
        
        - "나는..." 으로 시작하는 긍정적인 문장
        - 30-60자 내외
        - 자신감과 사랑을 주는 내용
        - 이모지 1개 포함
        
        메시지만 작성해주세요.
        """
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "당신은 자기 확언 전문가입니다. 사용자의 자존감을 높이는 긍정적인 자기 확언을 만들어주세요."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=100,
                temperature=0.7
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            fallback_affirmations = [
                "나는 오늘도 최선을 다하고 있어요! 💪",
                "나는 사랑받을 만한 사람이에요! 💖",
                "나는 내 자신을 믿고 있어요! ✨",
                "나는 매일 조금씩 성장하고 있어요! 🌱",
                "나는 내 가치를 알고 있어요! 🌟"
            ]
            return random.choice(fallback_affirmations)
