from openpyxl import load_workbook

wb = load_workbook("studentsinfo.xlsx")
ws = wb.active

ws["F1"] = "Total"
ws
ws["F2"] = "=SUM(B2:E2)"
ws["F3"] = "=SUM(B3:E3)"
ws["F4"] = "=SUM(B4:E4)"
ws["F5"] = "=SUM(B5:E5)"

wb.save("studentsinfo.xlsx")
print("file save sucessfully")

