from constants.config_keys import OUTPUT_FOLDER_PATH

import pandas as pd
import xlrd , openpyxl
import os
from pathlib import Path


def GetFilesPathInFolder(folder_path):
    for file_name in os.listdir(folder_path):
        pathlib_var = Path(file_name)
        if(pathlib_var.suffix in [".xls" , ".xlsx"]):
            file_path = os.path.join(folder_path , file_name)

            print(f"Archivo encontrado: {file_path}")
            yield file_path

def GetExcelFilesData(files_path):
    for file_path in files_path:
        excel_file_data = pd.read_excel(file_path)
        yield excel_file_data

def ConcatExcelFiles(excel_files_data):
    data_collection = pd.DataFrame()
    for excel_file_data in excel_files_data:
        data_collection = pd.concat([data_collection , excel_file_data] , ignore_index=True)

    return data_collection

def SaveExcelFile(data_collection):
    if(not os.path.exists(OUTPUT_FOLDER_PATH)):
        os.mkdir(os.path.join(OUTPUT_FOLDER_PATH))
    
    excel_file_name = os.path.join(OUTPUT_FOLDER_PATH , "excel_final.xlsx")
    with pd.ExcelWriter(excel_file_name) as excel_writer:
        excel_writer.book.create_sheet("Hoja 1")
        data_collection.to_excel(excel_writer , sheet_name="Hoja 1" , index=False)

def GetExcelData():
    all_excel_data = pd.read_excel(os.path.join(OUTPUT_FOLDER_PATH , "excel_final.xlsx") , sheet_name=0 , engine="openpyxl")
    for _ , data in all_excel_data.iterrows():
        yield data