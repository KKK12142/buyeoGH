"""
이 페이지는 main_screen에서 "대여" 버튼을 눌럿ㅇㄹ때 렌더링 되는 페이지 입니다.
"""

import tkinter as tk
from tkinter import ttk

# TODO: 대여가능 여부 판단 후 창전환
# TODO: 학년, 반, 번호, 이름 입력
# TODO: 캔버스로 터치스크린 서명
#  -> util.py에서 임포트해서 가져오기
# TODO: 카메라모듈 사진촬영
#  -> hardware_controller.py에서 임포트해서 가져오기
# TODO:DB에 저장 및 키 상태 업데이트
# TODO:제출 완료되면 GPIO핀 이용해서 자물쇠통 문열기


class RentalFrame(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.last_x = None
        self.last_y = None
        self.setup_ui()

    def setup_ui(self):
        """메인컨테이너 (2개의 열)"""
        main_container = tk.Frame(self)
        main_container.pack(fill="both", expand=True, padx=15)

        """왼쪽, 인적사항 입력칸"""
        left_frame = tk.Frame(main_container)
        left_frame.pack(side="left", fill="both", expand=True)
        self.create_student_info_form(left_frame)

        """오른쪽, 카메라 화면"""
        right_frame = tk.Frame(main_container)
        right_frame.pack(side="right", fill="both", expand=True)
        # self.create_camera_preview(right_frame)

        # 뒤로가기 버튼
        back_btn = tk.Button(
            self,
            text="← 뒤로가기",
            command=self.app.show_main_screen,
            font=("맑은고딕", 12),
            width=20,
            height=3,
        )
        back_btn.pack(side=tk.BOTTOM, pady=20)

    def create_student_info_form(self, parent):
        """이름"""
        tk.Label(parent, text="이름", font=("맑은고딕", 12)).grid(
            row=0, column=0, sticky="w", pady=5, padx=(0, 10)
        )
        self.name_entry = tk.Entry(parent, font=("맑은고딕", 12))
        self.name_entry.grid(row=0, column=1, pady=5)

        """학년"""
        tk.Label(parent, text="학년:", font=("맑은고딕", 12)).grid(
            row=1, column=0, sticky="w", pady=5, padx=(0, 10)
        )
        grade_value = ["1", "2", "3"]
        self.grade_combo = ttk.Combobox(parent, values=grade_value, state="readonly")
        self.grade_combo.grid(row=1, column=1, pady=5)

        """반"""
        tk.Label(parent, text="반", font=("맑은고딕", 12)).grid(
            row=2, column=0, sticky="w", pady=5, padx=(0, 10)
        )
        class_value = ["1", "2", "3", "4", "5"]
        self.class_combo = ttk.Combobox(parent, values=class_value, state="readonly")
        self.class_combo.grid(row=2, column=1, pady=5)

        """번호"""
        tk.Label(parent, text="번호", font=("맑은고딕", 12)).grid(
            row=3, column=0, sticky="w", pady=5, padx=(0, 10)
        )

        number_value = [str(i) for i in range(1, 26)]
        self.number_combo = ttk.Combobox(
            parent, values=number_value, state="readonly", height=5
        )
        self.number_combo.grid(row=3, column=1, pady=5)

        """서명칸"""
        tk.Label(parent, text="서명", font=("맑은고딕", 12)).grid(
            row=4, column=0, sticky="nw", pady=(20, 5), padx=(0, 10)
        )
        self.canvas = tk.Canvas(
            parent, width=300, height=150, bg="white", relief="sunken", border=2
        )
        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw_signature)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)
        self.canvas.grid(row=4, column=1, pady=(20, 5))

        clear_btn = tk.Button(
            parent, text="서명 지우기", command=lambda: self.canvas.delete("all")
        )
        clear_btn.grid(row=5, column=1)

        submit_btn = tk.Button(
            parent,
            text="제출",
            command=self.submit_rental,
            font=("맑은고딕", 12),
            bg="lightblue",
        )
        submit_btn.grid(row=6, column=1, pady=20, sticky="ew")

    def start_drawing(self, event):
        print(event)
        self.last_x = event.x
        self.last_y = event.y

    def stop_drawing(self, event):
        print(event)
        self.last_x = None
        self.last_y = None

    def draw_signature(self, event):
        if self.last_x is not None and self.last_y is not None:
            self.canvas.create_line(
                self.last_x,
                self.last_y,
                event.x,
                event.y,
                width=3,
                fill="black",
                capstyle=tk.ROUND,
                smooth=tk.TRUE,
            )
        self.last_x = event.x
        self.last_y = event.y

    def submit_rental(self):
        print("제출완료")
