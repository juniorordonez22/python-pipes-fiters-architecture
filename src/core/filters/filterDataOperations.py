def FilterAnulatedRequests(rows):
    for row in rows:
        if(row["Estado"] != "anulada"):
            yield row

def FilterRequestsByYear(rows):
    for row in rows:
        if(int(row["Fecha de Emisión"][-4:]) == 2023):
            yield row

def FilterAmountsBelowFiveThousand(rows):
    for row in rows:
        if(float(row["Monto"][4:]) >= 5000):
            yield row