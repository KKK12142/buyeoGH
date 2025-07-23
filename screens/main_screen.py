"""
이 페이지는 키오스크 사용약관에 대한 동의를 한경우 렌더링되는 페이지 입니다.
대여 / 반납 메뉴를 렌더링 합니다.
"""

import tkinter as tk


class MainFrame(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.setup_ui()

    def setup_ui(self):
        # 메인 제목
        title_label = tk.Label(
            self, text="열쇠 관리 시스템", font=("맑은고딕", 20, "bold")
        )
        title_label.pack(pady=50)

        # 버튼 프레임
        button_frame = tk.Frame(self)
        button_frame.pack(expand=True)

        # 대여 버튼
        rental_btn = tk.Button(
            button_frame,
            text="열쇠 대여",
            font=("맑은고딕", 16),
            width=15,
            height=3,
            bg="lightblue",
            relief="raised",
            bd=3,
            command=self.app.show_rental_screen,
        )
        rental_btn.pack(side=tk.LEFT, padx=30)

        # 반납 버튼
        return_btn = tk.Button(
            button_frame,
            text="열쇠 반납",
            font=("맑은고딕", 16),
            width=15,
            height=3,
            bg="lightyellow",
            relief="raised",
            bd=3,
            command=self.app.show_return_screen,
        )
        return_btn.pack(side=tk.RIGHT, padx=30)

        # 뒤로가기 버튼
        back_btn = tk.Button(
            self,
            text="← 뒤로가기",
            command=self.app.show_agreement_screen,
            font=("맑은고딕", 12),
            width=20,
            height=3,
        )
        back_btn.pack(side=tk.BOTTOM, pady=20)
