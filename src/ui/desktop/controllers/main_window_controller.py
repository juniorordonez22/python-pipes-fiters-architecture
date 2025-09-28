from core.main import ManageOperations

class MainWindowController:
    def StartCalcs(self , folder_path):
        results_data = ManageOperations(folder_path)

        return results_data