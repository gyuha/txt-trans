import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from googletrans import Translator

# 번역 함수
def translate_file(filename, progress_label):
    # 파일 읽기
    with open(filename, 'r', encoding='utf-8') as f:
        original_text = f.read()

    # 번역
    translator = Translator()
    translated = translator.translate(original_text, dest='ko')

    # 번역 결과 저장
    new_filename = f"{os.path.splitext(filename)[0]}.origin{os.path.splitext(filename)[1]}"
    with open(new_filename, 'w', encoding='utf-8') as f:
        f.write(original_text)

    # 번역된 내용 파일에 저장
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(translated.text)
        
    # 처리된 파일명 프로그레스 레이블에 추가
    progress_label.configure(text=f"{progress_label['text']}\n{filename} 처리 완료")

# 파일 선택 대화 상자
def choose_files():
    # 파일 대화 상자 열기
    filenames = filedialog.askopenfilenames()

    if filenames:
        # 이미지 파일 읽기
        img = Image.open("drag_drop.png")
        img = img.resize((400, 400), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)

        # 이미지 보이기
        drop_label.configure(image=photo)
        drop_label.image = photo

        # 파일 번역
        progress_label.configure(text="번역 진행 중...")
        for filename in filenames:
            translate_file(filename, progress_label)

        # 성공적으로 저장됨 메시지 박스 표시
        messagebox.showinfo("번역 완료", "모든 파일의 번역이 완료되었습니다.")

# 윈도우 생성
window = tk.Tk()
window.title("파일 번역기")
window.geometry("450x450")

# 이미지 표시 레이블
img = Image.open("drag_drop.png")
img = img.resize((400, 400), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(img)
drop_label = tk.Label(window, image=photo)
drop_label.pack(padx=25, pady=25)

# 드래그 앤 드랍 레이블
drag_label = tk.Label(window, text="파일을 여기에 드래그&드랍하세요.", font=("Helvetica", 12))
drag_label.pack(pady=10)

# 파일 선택 버튼
choose_button = tk.Button(window, text="파일 선택", command=choose_files)
choose_button.pack(pady=10)

# 진행 상황 표시 레이블
progress_label = tk.Label(window, text="", font=("Helvetica", 10), justify="left")
progress_label.pack(pady=10)

# 윈도우 실행
window.mainloop()