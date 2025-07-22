import tkinter as tk
from screens.base_screen import BaseScreen
from screens.agreement_screen import AgreementFrame
from screens.main_screen import MainFrame
from screens.rental_screen import RentalFrame
from screens.return_screen import ReturnFrame

class KioskApp(BaseScreen):
    def __init__(self):
        super().__init__(title="열쇠 키오스크", size="800x480")
        self.root.attributes('-fullscreen', True)
        
        # 프레임들 생성
        self.agreement_frame = AgreementFrame(self.root, self)
        self.main_frame = MainFrame(self.root, self)
        self.rental_frame = RentalFrame(self.root, self)
        self.return_frame = ReturnFrame(self.root, self)

        # 첫 화면 표시
        self.show_frame(self.agreement_frame)

    # def setup_ui(self):
    #     """BaseScreen에서 요구하는 메서드 - 비워둠"""
    #     pass
    
    def show_frame(self, frame):
        """프레임 전환"""
        # 모든 프레임 숨기기
        self.agreement_frame.pack_forget()
        self.main_frame.pack_forget()
        self.rental_frame.pack_forget()
        self.return_frame.pack_forget()

        # 선택한 프레임만 표시
        frame.pack(fill='both', expand=True)

    def show_agreement_screen(self):
        self.show_frame(self.agreement_frame)

    def show_main_screen(self):
        self.show_frame(self.main_frame)

    def show_rental_screen(self):
        self.show_frame(self.rental_frame)
    
    def show_return_screen(self):
        self.show_frame(self.return_frame)
