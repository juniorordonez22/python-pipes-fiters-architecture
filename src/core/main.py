import core.filters.fileOperations as FileOp
import core.calcs.calcTotalOperations as CalcTO

import core.filters.transformOperations as TransformOp
import core.filters.filterDataOperations as FilterDataOp

def ManageOperations(folder_path):
    # Obtener el(los) archivo(s)
    files_path = FileOp.GetFilesPathInFolder(folder_path)

    excel_files_data = FileOp.GetExcelFilesData(files_path)
    data_collection = FileOp.ConcatExcelFiles(excel_files_data)
    FileOp.SaveExcelFile(data_collection)
    # leer los datos del archivo
    all_excel_data = FileOp.GetExcelData()
    
    all_excel_data = TransformOp.NormalizeText(all_excel_data)
    all_excel_data = TransformOp.AddColumnYearsOfHiring(all_excel_data)
    
    all_excel_data = FilterDataOp.FilterAnulatedRequests(all_excel_data)
    all_excel_data = FilterDataOp.FilterRequestsByYear(all_excel_data)
    all_excel_data = FilterDataOp.FilterAmountsBelowFiveThousand(all_excel_data)

    import pandas
    all_excel_data = pandas.DataFrame(all_excel_data)
    FileOp.SaveExcelFile(all_excel_data)

    N_OC , N_OS = CalcTO.CalcNumberOfPurchaseOrders(all_excel_data)

    return {
        "Numero de Ordenes de Servicio": N_OS , 
        "Numero de Ordenes de Compra": N_OC , 
    }


