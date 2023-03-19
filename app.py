import tkinter as tk
from tkinter import ttk


class ListboxFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Listbox with header")

        # configure row and column weights for resizing
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)

        self.tree = ttk.Treeview(self)
        self.tree["columns"] = ("filename", "process")
        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("filename", anchor=tk.W, width=120)
        self.tree.column("process", anchor=tk.W, width=80)

        self.tree.heading("#0", text="", anchor=tk.W)
        self.tree.heading("filename", text="파일명", anchor=tk.W)
        self.tree.heading("process", text="처리", anchor=tk.W)

        # insert some items
        self.tree.insert(
            parent="", index="end", iid=0, text="", values=("file1.txt", "Yes")
        )
        self.tree.insert(
            parent="", index="end", iid=1, text="", values=("file2.txt", "No")
        )
        self.tree.insert(
            parent="", index="end", iid=2, text="", values=("file3.txt", "Yes")
        )

        # grid the treeview
        self.tree.grid(row=0, column=0, sticky="nsew")

        # create close and run buttons
        self.close_button = tk.Button(self, text="닫기", command=self.master.destroy)
        self.run_button = tk.Button(self, text="실행", command=self.run)

        # grid the buttons
        self.close_button.grid(row=1, column=0, sticky="e")
        self.run_button.grid(row=1, column=0, sticky="w")

    def run(self):
        # get the selected item
        selected_item = self.tree.focus()
        # get the values of the selected item
        values = self.tree.item(selected_item)["values"]

        # print the values
        print(values)


if __name__ == "__main__":
    window = tk.Tk()
    listbox_frame = ListboxFrame(window)
    listbox_frame.pack()
    window.mainloop()
