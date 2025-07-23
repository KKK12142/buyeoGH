"""
이 페이지는 키오스크 사용약관에 대한 동의 페이지 입니다.
"""

import tkinter as tk
from tkinter import messagebox


class AgreementFrame(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.setup_ui()

    def setup_ui(self):
        # 제목
        title_label = tk.Label(
            self, text="열쇠 키오스크 이용약관", font=("맑은고딕", 20, "bold")
        )
        title_label.pack(pady=10)

        # 주의사항 프레임
        notice_frame = tk.Frame(self)
        notice_frame.pack(pady=10)

        # 주의사항 텍스트
        notice_text = tk.Text(
            notice_frame, height=10, width=60, wrap=tk.WORD, font=("맑은고딕", 15)
        )
        notice_text.pack(pady=20)

        # 텍스트 내용 삽입
        notice_content = """
        1. 열쇠를 분실하지 않겠습니다.\n
        2. 용무를 마치고 열쇠를 즉시 반납하겠습니다.\n
        3. 다른 사람에게 양도하지 않겠습니다.\n
        4. 사용 후 반드시 제자리에 반납하겠습니다.
        """
        notice_text.insert(tk.END, notice_content)
        notice_text.config(state=tk.DISABLED)

        # 버튼 프레임
        button_frame = tk.Frame(self)
        button_frame.pack(expand=True)

        # 동의 버튼
        agree_btn = tk.Button(
            button_frame,
            text="동의합니다",
            command=self.app.show_main_screen,
            width=20,
            height=3,
            bg="lightgreen",
            font=("맑은고딕", 14, "bold"),
            relief="raised",
            bd=3,
        )
        agree_btn.pack(side=tk.LEFT, padx=10)

        # 비동의 버튼
        deny_btn = tk.Button(
            button_frame,
            text="동의하지 않습니다",
            command=lambda: messagebox.showwarning(
                "경고", "위 내용에 동의하지 않으면 사용하실 수 없습니다"
            ),
            width=20,
            height=3,
            bg="lightcoral",
            font=("맑은고딕", 14, "bold"),
            relief="raised",
            bd=3,
        )
        deny_btn.pack(side=tk.RIGHT, padx=10)
