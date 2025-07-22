"""
열쇠 대여/반납 키오스크 시스템
메인 진입점
"""

from app.kiosk_app import KioskApp

if __name__ == "__main__":
    app = KioskApp()
    app.run()