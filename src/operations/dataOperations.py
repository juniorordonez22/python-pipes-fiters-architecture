import re

def NormalizeText(all_excel_data):
    for data in all_excel_data:
        for idx in data.index:
            if(not data[idx]):
                continue
            if(not isinstance(data[idx] , str)):
                continue
            
            data[idx] = data[idx].lower().strip()

            data[idx] = data[idx].replace('{', '').replace('}', '')

            data[idx] = data[idx].replace('“', '"').replace('”', '"').replace('‘', "'").replace('’', "'").replace('"', '').replace("'", '')

            data[idx] = data[idx].replace('–', '-').replace('—', '-')

            data[idx] = re.sub(r'[.,;:!?()\[\]]', '', data[idx])

            data[idx] = re.sub(r'\s+', ' ', data[idx]).strip()

        yield data

def FilterDenegatedRequest(all_excel_data):
    for data in all_excel_data:
        pass

def FilterPurchaseOrders(all_excel_data):
    pass

def IndentifyDuplicatedData(entrie: dict):
    Observed_Titles = []
    Observed_DOIs = []
    for key , data_in_entrie in entrie.items():
        if(str(key).lower().strip() in ["title" , "doi"]):
            data = NormalizeText(data_in_entrie)
            