import re

def NormalizeText(rows):
    for row in rows:
        for idx in row.index:
            if(not row[idx]):
                continue
            if(not isinstance(row[idx] , str)):
                continue
            
            row[idx] = row[idx].lower().strip()
            row[idx] = row[idx].replace('{', '').replace('}', '')
            row[idx] = row[idx].replace('“', '"').replace('”', '"').replace('‘', "'").replace('’', "'").replace('"', '').replace("'", '')
            row[idx] = row[idx].replace('–', '-').replace('—', '-')
            row[idx] = re.sub(r'[.,;:!?()\[\]]', '', row[idx])
            row[idx] = re.sub(r'\s+', ' ', row[idx]).strip()

        yield row

def AddColumnYearsOfHiring(rows):
    for row in rows:
        row["Años de Contratación"] = 2025 - int(row["Fecha de Emisión"][-4:])
        yield row