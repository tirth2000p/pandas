import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, FileFormatType

wb = Workbook("out.xlsx")

# save workbook as HTML file

wb.save("workbook.html")