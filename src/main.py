from ui.desktop.main_window import MainWindow

if(__name__ == "__main__"):
    app_main_window = MainWindow()

    app_main_window.CreateWindowAndWidgets()
    app_main_window.DisplayWindowAndWidgets()