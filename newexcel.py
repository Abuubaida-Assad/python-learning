
from openpyxl import load_workbook


wb = load_workbook("studentsinfo.xlsx")
ws = wb.active


ws["F1"] = "Total"
ws["G1"] = "Average"
ws["H1"] = "Result"


for row in range(2, ws.max_row + 1):

    
    ws[f"F{row}"] = f"=SUM(B{row}:E{row})"

    
    ws[f"G{row}"] = f"=AVERAGE(B{row}:E{row})"

    
    ws[f"H{row}"] = f'=IF(G{row}>=40,"Pass","Fail")'

wb.save("studentsinfo.xlsx")

print("File saved successfully!")








