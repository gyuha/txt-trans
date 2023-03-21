import os
from googletrans import Translator
import tkinter as tk
from tkinter import filedialog

translator = Translator(service_urls=["translate.google.com"])
print(tk.TkVersion)


def translate_files():
    # 번역할 언어 선택
    target_lang = "ko"
    # 시작 폴더 경로 설정
    start_folder = folder_path.get()
    # 번역할 파일 확장자 리스트
    extensions = [ext.strip() for ext in extension_entry.get().split(",")]
    # 하위 폴더의 모든 파일에서 확장자가 extensions 리스트에 있는 파일을 찾아 번역
    for root, dirs, files in os.walk(start_folder):
        for filename in files:
            ext = os.path.splitext(filename)[1]
            if ext in extensions:
                filepath = os.path.join(root, filename)
                print("📢[app.py:22]: ", filepath)
                with open(filepath, "r", encoding="utf-8") as f:
                    # 파일 내용 읽기
                    content = f.read()
                    # 영어에서 한국어로 번역
                    translated = translator.translate(content, dest=target_lang).text
                with open(filepath, "w", encoding="utf-8") as f:
                    # 번역된 내용을 파일에 쓰기
                    f.write(translated)
                # 원본 파일 저장
                origin_path = os.path.join(
                    root,
                    f"{os.path.splitext(filename)[0]}.origin{os.path.splitext(filename)[1]}",
                )
                os.rename(filepath, origin_path)
    # 번역이 완료되었음을 알리는 메시지 박스 출력
    tk.messagebox.showinfo(title="번역 완료", message="파일 번역이 완료되었습니다.")


class DragDropEntry(tk.Entry):
    def __init__(self, master, **kw):
        tk.Entry.__init__(self, master, **kw)

        # 드래그 이벤트에 대한 바인딩 추가
        self.bind("<Drop>", self.drop_event)

    def drop_event(self, event):
        # 드롭된 파일 경로 추출
        file_path = event.data

        # Entry 위젯에 경로 삽입
        self.delete(0, tk.END)
        self.insert(0, file_path)


def select_folder():
    # 폴더 선택 다이얼로그 열기
    folder_path.set(filedialog.askdirectory())


# tkinter 윈도우 생성
window = tk.Tk()
window.geometry("500x300")

# 윈도우 제목 설정
window.title("파일 번역기")

# 폴더 선택 라벨
folder_label = tk.Label(text="폴더 선택")
folder_label.pack()


# 폴더 선택 박스
folder_path = tk.StringVar()
folder_entry = tk.Entry(textvariable=folder_path)
folder_entry.pack()

# 폴더 입력 박스에 DropTarget 기능 추가
DragDropEntry(folder_entry)

# 폴더 선택 버튼
folder_button = tk.Button(text="폴더 선택", command=select_folder)
folder_button.pack()

# 확장자 입력 라벨
extension_label = tk.Label(text="확장자 입력 (여러 개일 경우 ,로 구분)")
extension_label.pack()

# 확장자 입력 박스
extension_entry = tk.Entry()
extension_entry.insert(0, "srt,vtt")
extension_entry.pack()

# 실행 버튼
run_button = tk.Button(text="실행", command=translate_files)
run_button.pack()

# 윈도우 실행
window.mainloop()
