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
        """15줄의 자기확언 리스트 생성"""
        
        prompt = """
        당신은 심리학과 철학을 깊이 이해하는 마음챙김 전문가입니다. 
        현대인들이 겪는 내면의 고민과 불안을 정확히 파악하고, 
        진정한 치유와 성장을 이끌어내는 깊이 있는 자기확언을 만들어주세요.
        
        다음 조건을 정확히 지켜주세요:
        
        1. 정확히 15줄의 자기확언을 작성
        2. 각 줄은 "1. ~~~", "2. ~~~", ... "15. ~~~" 형식
        3. 상투적이지 않고 깊이 있는 내용
        4. 현대인의 실제 고민을 다룬 공감대 형성
        5. 심리학적 근거가 있는 치유적 메시지
        6. 각 줄당 20-40자 내외
        7. 이모지는 사용하지 않음
        8. 진정성 있고 따뜻한 톤
        
        주제 예시:
        - 내면의 비판자와 화해하기
        - 불완전함을 받아들이기
        - 진정한 자아 발견
        - 관계에서의 경계 설정
        - 실패에 대한 새로운 관점
        - 감정 조절과 마음챙김
        - 자기 가치 인정하기
        
        반드시 15줄로 구성된 자기확언 리스트만 작성해주세요.
        """
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "당신은 심리학과 철학을 깊이 이해하는 마음챙김 전문가입니다. 현대인들의 내면을 정확히 파악하고 진정한 치유를 이끌어내는 전문가입니다."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=800,
                temperature=0.9
            )
            
            message = response.choices[0].message.content.strip()
            return message
            
        except Exception as e:
            # API 호출 실패 시 기본 메시지 반환
            fallback_message = """1. 나는 내 감정을 있는 그대로 받아들일 권리가 있다
2. 완벽하지 않아도 충분히 가치 있는 존재다
3. 내 실수는 나를 성장시키는 소중한 경험이다
4. 다른 사람의 기대보다 내 마음의 소리가 더 중요하다
5. 나는 내 인생의 주인공이고 선택할 권리가 있다
6. 지금 이 순간의 나는 이미 충분히 훌륭하다
7. 내 약점도 나를 구성하는 소중한 부분이다
8. 나는 내 경계를 지킬 권리와 용기가 있다
9. 과거의 나와 미래의 나 모두 사랑받을 만하다
10. 내 가치는 다른 사람의 평가로 결정되지 않는다
11. 나는 내 감정을 표현할 자유와 권리가 있다
12. 실패는 끝이 아니라 새로운 시작의 기회다
13. 나는 내 몸과 마음을 소중히 여길 가치가 있다
14. 내 꿈과 목표는 충분히 의미 있고 가치 있다
15. 나는 매일 조금씩 더 나은 사람이 되어가고 있다"""
            return fallback_message
    
    def generate_daily_affirmation(self) -> str:
        """일일 자기 확언 메시지 생성 (15줄 리스트)"""
        return self.generate_positive_message()  # 같은 형식으로 통일
