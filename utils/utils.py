from datetime import datetime

def get_current_datetime():
    """현재 날짜와 시간을 문자열로 반환"""
    now = datetime.now()
    return now.strftime("%Y년 %m월 %d일 %H:%M:%S")

