import fileOperations as FileOp

def ManageOperations(folder_path):
    files_names = FileOp.GetFilesNamesInFolder(folder_path)
    
    files_path = FileOp.GetFilesPathInFolder(files_names)

    excel_files_data = FileOp.GetExcelFilesData(files_path)

    data_collection = FileOp.ConcatExcelFiles(excel_files_data)
    FileOp.SaveMergedExcelFile(data_collection)