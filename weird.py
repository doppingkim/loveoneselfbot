#!/usr/bin/env python3
"""
마음챙김 챗봇 - 메인 실행 파일
매일매일 자존감 한 스푼을 전달하는 텔레그램 봇
"""

from telegram_bot import main
import asyncio

if __name__ == "__main__":
    print("💖 마음챙김 챗봇을 시작합니다...")
    asyncio.run(main())
