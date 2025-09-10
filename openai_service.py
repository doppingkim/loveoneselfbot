import openai
from config import Config
import random
import time
from datetime import datetime, timedelta

class OpenAIService:
    """OpenAI API를 활용한 긍정적인 메시지 생성 서비스"""
    
    def __init__(self):
        """OpenAI 클라이언트 초기화"""
        if Config.OPENAI_API_KEY and Config.OPENAI_API_KEY != "your_openai_api_key_here":
            openai.api_key = Config.OPENAI_API_KEY
            self.client = openai.OpenAI(api_key=Config.OPENAI_API_KEY)
        else:
            self.client = None
            print("⚠️ OPENAI_API_KEY가 설정되지 않았습니다. 기본 메시지만 사용됩니다.")
        
        # API 호출 제한 (보안)
        self.last_call_time = 0
        self.min_call_interval = 5  # 최소 5초 간격
        self.daily_call_count = 0
        self.daily_limit = 100  # 하루 최대 100회
        self.last_reset_date = datetime.now().date()
    
    def _check_rate_limit(self) -> bool:
        """API 호출 제한 확인"""
        current_time = time.time()
        current_date = datetime.now().date()
        
        # 날짜가 바뀌면 카운트 리셋
        if current_date != self.last_reset_date:
            self.daily_call_count = 0
            self.last_reset_date = current_date
        
        # 하루 호출 제한 확인
        if self.daily_call_count >= self.daily_limit:
            print(f"⚠️ 일일 API 호출 제한 초과: {self.daily_call_count}/{self.daily_limit}")
            return False
        
        # 최소 간격 확인
        if current_time - self.last_call_time < self.min_call_interval:
            print(f"⚠️ API 호출 간격이 너무 짧음: {current_time - self.last_call_time:.1f}초")
            return False
        
        return True
    
    def generate_positive_message(self) -> str:
        """10줄의 자기확언 리스트 생성"""
        
        # 다양한 주제와 톤
        topics = [
            "내면의 비판자와 화해하기",
            "불완전함을 받아들이기", 
            "진정한 자아 발견",
            "관계에서의 경계 설정",
            "실패에 대한 새로운 관점",
            "감정 조절과 마음챙김",
            "자기 가치 인정하기",
            "과거와의 화해",
            "미래에 대한 희망",
            "현재 순간의 소중함",
            "자기 사랑과 용서",
            "성장과 변화 수용",
            "스트레스 관리",
            "자신감 회복",
            "꿈과 목표 추구"
        ]
        
        tones = [
            "따뜻하고 위로하는",
            "격려하고 힘을 주는", 
            "성찰적이고 깊이 있는",
            "희망적이고 밝은",
            "용기를 주는",
            "평화롭고 안정적인"
        ]
        
        # 랜덤하게 주제와 톤 선택
        selected_topic = random.choice(topics)
        selected_tone = random.choice(tones)
        
        prompt = f"""
        당신은 심리학과 철학을 깊이 이해하는 마음챙김 전문가입니다. 
        현대인들이 겪는 내면의 고민과 불안을 정확히 파악하고, 
        진정한 치유와 성장을 이끌어내는 깊이 있는 자기확언을 만들어주세요.
        
        오늘의 주제: "{selected_topic}"
        톤: {selected_tone}
        
        다음 조건을 정확히 지켜주세요:
        
        1. 정확히 10줄의 자기확언을 작성
        2. 각 줄은 "1. ~~~", "2. ~~~", ... "10. ~~~" 형식
        3. 위 주제에 집중한 깊이 있는 내용
        4. {selected_tone} 톤으로 작성
        5. 심리학적 근거가 있는 치유적 메시지
        6. 각 줄당 20-40자 내외
        7. 이모지는 사용하지 않음
        8. 진정성 있고 따뜻한 톤
        9. 한국어 문법에 맞는 올바른 문장
        10. 이전과 다른 새로운 관점과 표현 사용
        
        반드시 10줄로 구성된 자기확언 리스트만 작성해주세요.
        """
        
        if not self.client:
            # OpenAI 클라이언트가 없으면 기본 메시지 반환
            return self._get_fallback_message()
        
        # API 호출 제한 확인
        if not self._check_rate_limit():
            return self._get_fallback_message()
            
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "당신은 심리학과 철학을 깊이 이해하는 마음챙김 전문가입니다. 현대인들의 내면을 정확히 파악하고 진정한 치유를 이끌어내는 전문가입니다. 매번 새로운 관점과 표현으로 창의적인 자기확언을 만들어주세요."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=800,
                temperature=1.2  # 더 창의적이고 다양한 응답을 위해 증가
            )
            
            message = response.choices[0].message.content.strip()
            
            # 호출 성공 시 카운트 증가
            self.daily_call_count += 1
            self.last_call_time = time.time()
            
            return message
            
        except Exception as e:
            # API 호출 실패 시 기본 메시지 반환
            return self._get_fallback_message()
    
    def _get_fallback_message(self) -> str:
        """기본 자기확언 메시지 반환 (다양한 버전)"""
        fallback_messages = [
            """1. 나는 내 감정을 있는 그대로 받아들일 권리가 있다
2. 완벽하지 않아도 충분히 가치 있는 존재다
3. 내 실수는 나를 성장시키는 소중한 경험이다
4. 다른 사람의 기대보다 내 마음의 소리가 더 중요하다
5. 나는 내 인생의 주인공이고 선택할 권리가 있다
6. 지금 이 순간의 나는 이미 충분히 훌륭하다
7. 내 약점도 나를 구성하는 소중한 부분이다
8. 나는 내 경계를 지킬 권리와 용기가 있다
9. 과거의 나와 미래의 나 모두 사랑받을 만하다
10. 나는 매일 조금씩 더 나은 사람이 되어가고 있다""",
            
            """1. 나는 내 가치를 다른 사람의 평가로 결정하지 않는다
2. 실패는 끝이 아니라 새로운 시작의 기회다
3. 나는 내 꿈을 추구할 자유와 권리가 있다
4. 지금 이 순간이 내가 가진 모든 것이다
5. 나는 내 몸과 마음을 소중히 여길 가치가 있다
6. 변화는 성장의 증거이지 실패가 아니다
7. 나는 내 감정을 표현할 자유와 권리가 있다
8. 과거의 상처는 나를 더 강하게 만들었다
9. 나는 내 인생의 주도권을 가지고 있다
10. 매일 작은 진전도 의미 있는 성장이다""",
            
            """1. 나는 내 내면의 소리를 신뢰할 수 있다
2. 불완전함 속에서도 아름다움이 있다
3. 나는 내 경계를 존중받을 권리가 있다
4. 실수는 배움의 기회이지 죄가 아니다
5. 나는 내 감정을 조절할 힘이 있다
6. 과거는 나를 정의하지 않는다
7. 나는 내 꿈을 실현할 능력이 있다
8. 자신을 사랑하는 것은 이기적이지 않다
9. 나는 내 인생의 의미를 스스로 만들 수 있다
10. 오늘도 나는 충분히 훌륭한 사람이다"""
        ]
        
        return random.choice(fallback_messages)
    
    def generate_daily_affirmation(self) -> str:
        """일일 자기 확언 메시지 생성 (10줄 리스트)"""
        return self.generate_positive_message()  # 같은 형식으로 통일
