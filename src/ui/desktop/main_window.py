from utils.window_utils import CenterWindow
from ui.desktop.interfaces.window_interfaces import BasicWindowActions   # Importacion desde la carpeta ui/
from ui.desktop.controllers.main_window_controller import MainWindowController

import tkinter as tk
from tkinter import filedialog
import os

def ExamineUserDevice(file_path: tk.StringVar):
    folder_path = filedialog.askdirectory()
    if(folder_path and os.path.isdir(folder_path)):
        file_path.set(folder_path)

class MainWindow(BasicWindowActions):
    main_window: tk.Tk
    selected_file_option: tk.StringVar
    file_path: tk.StringVar

    def CreateWindowAndWidgets(self):
        self.main_window = tk.Tk()

        for idx_row in range(1):
            self.main_window.rowconfigure(idx_row , weight=1)
        
        self.main_window.columnconfigure(0 , weight=0)
        self.main_window.columnconfigure(1 , weight=1)
        self.main_window.columnconfigure(2 , weight=0)

        self.selected_file_option = tk.StringVar(self.main_window)
        self.file_path = tk.StringVar(self.main_window)        

        self.btn_examine_files_in_user_device = tk.Button(self.main_window , text="Examinar" , font=("Times New Roman" , 12) , command= lambda: ExamineUserDevice(self.file_path))
        self.entry_file_path = tk.Entry(self.main_window , font=("Times New Roman" , 12) , textvariable=self.file_path)
        self.btn_process_file = tk.Button(self.main_window , text="Procesar" , font=("Times New Roman" , 12) , command=self.ProcessFiles)

    def DisplayWindowAndWidgets(self):
        self.main_window.geometry(
            CenterWindow(self.main_window , 1000 , 100)
        )
        self.main_window.title("Tuberias y Filtros")
        self.main_window.lift()

        self.btn_examine_files_in_user_device.grid(
            row=0 , column=0 , padx=(10 , 10)
        )
        self.entry_file_path.grid(
            row=0 , column=1 , sticky="ew" , padx=(10 , 10)
        )
        self.btn_process_file.grid(
            row=0 , column=2 , padx=(10 , 10)
        )

        self.main_window.mainloop()

    def DestroyWindow(self):
        for widget in self.main_window.winfo_children():
            widget.destroy()
        self.main_window.destroy()

    def ProcessFiles(self):
        if(self.file_path.get()):
            main_window_ctrll = MainWindowController()
            results_data = main_window_ctrll.StartCalcs(self.file_path.get())

            from ui.terminal.main_cli import PrintResultsInTerminal
            PrintResultsInTerminal(results_data)