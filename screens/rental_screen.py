import tkinter as tk

class RentalFrame(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.setup_ui()

    def setup_ui(self):
        title_label = tk.Label(self, text="대여 페이지 입니다.")
        title_label.pack()
        
        # 뒤로가기 버튼
        back_btn = tk.Button(self, text="← 뒤로가기",
                            command=self.app.show_main_screen,
                            font=("맑은고딕", 12), width=20, height=3)
        back_btn.pack(side=tk.BOTTOM, pady=20)