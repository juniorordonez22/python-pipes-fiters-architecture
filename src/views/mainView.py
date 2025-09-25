import tkinter as tk
from tkinter import filedialog
from abc import ABC, abstractmethod
import os

def CenterWindow(Window: tk.Tk | tk.Toplevel , window_width: int , window_height: int) -> str:
    screen_width = Window.winfo_screenwidth()
    screen_height = Window.winfo_screenheight()

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    return f"{window_width}x{window_height}+{x}+{y}"

def ExamineUserDevice(bibtex_file_path: tk.StringVar):
    folder_path = filedialog.askdirectory()
    if(folder_path and os.path.isdir(folder_path)):
        bibtex_file_path.set(folder_path)

class BasicWindowActions(ABC):
    @abstractmethod
    def Create(self):
        pass
    @abstractmethod
    def Destroy(self):
        pass

class MainWindow(BasicWindowActions):
    def Create(self):
        self.main_window = tk.Tk()

        self.main_window.geometry(
            CenterWindow(self.main_window , 1000 , 100)
        )

        self.main_window.title("Tuberias y Filtros")
        self.main_window.lift()

        self.csv_file_path = tk.StringVar(self.main_window)

        
        for idx_row in range(1):
            self.main_window.rowconfigure(idx_row , weight=1)
        
        self.main_window.columnconfigure(0 , weight=0)
        self.main_window.columnconfigure(1 , weight=1)
        self.main_window.columnconfigure(2 , weight=0)


        self.btn_examine_files_in_user_device = tk.Button(self.main_window , text="Examinar" , font=("Times New Roman" , 12) , command= lambda: ExamineUserDevice(self.csv_file_path))
        self.btn_examine_files_in_user_device.grid(
            row=0 , column=0 , padx=(10 , 10)
        )

        self.entry_csv_file_path = tk.Entry(self.main_window , font=("Times New Roman" , 12) , textvariable=self.csv_file_path)
        self.entry_csv_file_path.grid(
            row=0 , column=1 , sticky="ew" , padx=(10 , 10)
        )

        self.btn_process_file = tk.Button(self.main_window , text="Procesar" , font=("Times New Roman" , 12))
        self.btn_process_file.grid(
            row=0 , column=2 , padx=(10 , 10)
        )

        self.main_window.mainloop()

    def Destroy(self):
        for widget in self.main_window.winfo_children():
            widget.destroy()
        
        self.main_window.destroy()
