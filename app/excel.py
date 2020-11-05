from openpyxl import Workbook
from openpyxl.styles import Font, Border, Side, Alignment
from models import Course
import datetime
import saveData

def dataToExcel(fname:str, fnameExcel:str) :
    workbook = Workbook()
    worksheet = workbook.active
    thin_border = Border(left=Side(style='thin'), 
                        right=Side(style='thin'), 
                        top=Side(style='thin'), 
                        bottom=Side(style='thin'))
    text_align = Alignment(horizontal='center')
    #date
    worksheet[chr(ord('A')) + '1'] = "Date"
    worksheet.column_dimensions[chr(ord('A'))].width = 20
    worksheet[chr(ord('A')) + '1'].font = Font(bold=True)
    worksheet[chr(ord('A')) + '1'].alignment = text_align
    worksheet[chr(ord('A')) + '1'].border = thin_border
    #begin
    worksheet[chr(ord('B')) + '1'] = "Début"
    worksheet.column_dimensions[chr(ord('B'))].width = 20
    worksheet[chr(ord('B')) + '1'].font = Font(bold=True)
    worksheet[chr(ord('B')) + '1'].alignment = text_align
    worksheet[chr(ord('B')) + '1'].border = thin_border
    #ending
    worksheet[chr(ord('C')) + '1'] = "Fin"
    worksheet.column_dimensions[chr(ord('C'))].width = 20
    worksheet[chr(ord('C')) + '1'].font = Font(bold=True)
    worksheet[chr(ord('C')) + '1'].alignment = text_align
    worksheet[chr(ord('C')) + '1'].border = thin_border
    #course
    worksheet[chr(ord('D')) + '1'] = "Cours"
    worksheet.column_dimensions[chr(ord('D'))].width = 20
    worksheet[chr(ord('D')) + '1'].font = Font(bold=True)
    worksheet[chr(ord('D')) + '1'].alignment = text_align
    worksheet[chr(ord('D')) + '1'].border = thin_border
    #total
    worksheet[chr(ord('E')) + '1'] = "Durée"
    worksheet.column_dimensions[chr(ord('E'))].width = 20
    worksheet[chr(ord('E')) + '1'].font = Font(bold=True)
    worksheet[chr(ord('E')) + '1'].alignment = text_align
    worksheet[chr(ord('E')) + '1'].border = thin_border
    #total
    worksheet[chr(ord('G')) + '1'] = "Total"
    worksheet.column_dimensions[chr(ord('G'))].width = 20
    worksheet[chr(ord('G')) + '1'].font = Font(bold=True)
    worksheet[chr(ord('G')) + '1'].alignment = text_align
    worksheet[chr(ord('G')) + '1'].border = thin_border
    #algo
    r = 2
    tot = 0
    lines = readFile(fname)
    for line in lines :
        date, begin, ending, course, nbHours = line.split("&")
        d,h = date.split("-")
        worksheet[chr(ord('A')) + str(r)] = d + " à " + h
        h, m, s = begin.split(":")
        worksheet[chr(ord('B')) + str(r)] = h + "H" + m
        h, m, s = ending.split(":")
        worksheet[chr(ord('C')) + str(r)] = h + "H" + m
        worksheet[chr(ord('D')) + str(r)] = course
        worksheet[chr(ord('E')) + str(r)] = nbHours.strip()
        #style
        worksheet[chr(ord('A')) + str(r)].alignment = text_align
        worksheet[chr(ord('A')) + str(r)].border = thin_border
        worksheet[chr(ord('B')) + str(r)].alignment = text_align
        worksheet[chr(ord('B')) + str(r)].border = thin_border
        worksheet[chr(ord('C')) + str(r)].alignment = text_align
        worksheet[chr(ord('C')) + str(r)].border = thin_border
        worksheet[chr(ord('D')) + str(r)].alignment = text_align
        worksheet[chr(ord('D')) + str(r)].border = thin_border
        worksheet[chr(ord('E')) + str(r)].alignment = text_align
        worksheet[chr(ord('E')) + str(r)].border = thin_border
        tot+=int(nbHours)
        r+=1
    worksheet[chr(ord('G')) + '2'] = tot
    worksheet[chr(ord('G')) + '2'].alignment = text_align
    worksheet[chr(ord('G')) + '2'].border = thin_border
    workbook.save(fnameExcel)
    print("saved in Excel")

def readFile(fname:str) :
    readFile = open(fname, "r")
    lines = readFile.readlines()
    readFile.close()
    return lines
