def CalcNumberOfPurchaseOrders(all_excel_data):
    N_OS = 0
    N_OC = 0
    for _ , data in all_excel_data.iterrows():
        if(data["Tipo de Orden"] == "o/c"):
            N_OC += 1
        if(data["Tipo de Orden"] == "o/s"):
            N_OS += 1
    return N_OC , N_OS