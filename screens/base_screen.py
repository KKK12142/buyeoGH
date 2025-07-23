"""
이 페이지는 agreement_screen 페이지를 제외한 모든 페이지에 공통으로 렌더링 되어야할 페이지 입니다.
"""

import tkinter as tk
from utils.utils import get_current_datetime


class BaseScreen:
    def __init__(self, title="키오스크", size="800x480"):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(size)
        self.setup_common_ui()
        self.setup_ui()  # 각 화면별 UI

    # TODO: 현재 열쇠 대여가능 상태 표시하기 (마지막 대여 시간 등 표시)
    def setup_common_ui(self):
        """모든 화면 공통 요소"""
        # 시간 표시
        self.datetime_label = tk.Label(
            self.root, text=get_current_datetime(), font=("맑은고딕", 14), fg="blue"
        )
        self.datetime_label.pack(pady=10)

    def setup_ui(self):
        """각 화면별로 오버라이드할 메서드"""
        pass

    def update_time(self):
        """시간 업데이트"""
        current_time = get_current_datetime()
        self.datetime_label.config(text=current_time)
        self.root.after(1000, self.update_time)

    def run(self):
        self.update_time()  # 시간 업데이트 시작
        self.root.mainloop()
