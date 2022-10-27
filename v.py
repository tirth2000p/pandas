import jpype

# import asposecells

# load XLSX workbook

from asposecells.api import Workbook

wb = Workbook("out.xlsx")

# save workbook as HTML file

wb.save("workbook.html")