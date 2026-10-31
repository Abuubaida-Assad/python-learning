
# from openpyxl import Workbook

# # Create a new Excel workbook
# wb = Workbook()

# # Select the active worksheet
# ws = wb.active

# # Add column headings
# ws["A1"] = "Name"
# ws["B1"] = "Maths"
# ws["C1"] = "Physics"
# ws["D1"] = "Chemistry"
# ws["E1"] = "Total"

# # Add student data
# ws["A2"] = "Assad"
# ws["B2"] = 85
# ws["C2"] = 90
# ws["D2"] = 88

# # Add a formula
# ws["E2"] = "=SUM(B2:D2)"

# # Save the Excel file
# wb.save("students.xlsx")

# print("Excel file created successfully!")

from openpyxl import Workbook

wb = Workbook()
ws=wb.active;
ws.title="students";
ws["F1"] = "Total"

print("Excel file created successfully!")


