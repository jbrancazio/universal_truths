#imports
from PyPDF2 import PdfFileReader, PdfFileWriter
import datetime
import os
import re


def list_files(filepath, filetype):
    paths = []
    for root, dirs, files in os.walk(filepath):
        for file in files:
            if file.lower().endswith(filetype.lower()):
                paths.append(os.path.join(root, file))
    return paths


my_files_list = list_files('/Users/joshuabrancazio/Purgatory/scan/tobesplit', '.pdf')

# flashy display:
print('{}\n'.format(len(my_files_list)))
for i in my_files_list:
    print(i)




def Christus_DEL(raw_pdf):
    # Open PDF
    pdfFileObj = open(raw_pdf, 'rb')
    pdfReader = PdfFileReader(pdfFileObj)

    # search phrases
    search_phrase = 'please detach and return this portion with your payment'
    search_phrase_2 = 'thank you for choosing christus health plan.'
    search_phrase_3 = 'if you have any questions, please call us at the number listed above.'

    pdf_del = PdfFileWriter()
    pdf_delete = PdfFileWriter()
    pdfs = {}

    # create variable and loops
    del_date = None
    loop = True
    keep = []
    delete = []

    # find date loop
    while loop == True:
        for pageNum in range(0, pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            text = pageObj.extractText()
            search_text = text.lower().split('\n')
            for words in search_text:
                match = re.match(r'^(\w+)[" "]\d{2}\,[" "]\d{4}$', words)
                if match:
                    del_date = match.group(0)
                    loop = False

    # create date dictionary key
    del_date = datetime.datetime.strptime(del_date, '%B %d, %Y')
    pdfs[del_date] = None

    # find pages with key words
    for pageNum in range(0, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        text = pageObj.extractText()
        search_text = text.lower().split('\n')
        for words in search_text:
            if search_phrase in words:
                keep.append(pageNum)
            elif search_phrase_2 in words:
                keep.append(pageNum)
            elif search_phrase_3 in words:
                keep.append(pageNum)

    # assign pages to key
    pdfs[del_date] = keep

    # Add pages to pdf
    for i in range(len(pdfs[del_date])):
        pdf_del.addPage(pdfReader.getPage(pdfs[del_date][i]))

    # assign path
    output_filename = 'Christus_DEL_{}.pdf'.format(del_date)

    # write Delinquency PDF
    with open(output_filename, 'wb') as out:
        pdf_del.write(out)

    # find leftover pages
    for page_num in range(1, pdfReader.numPages):
        if page_num not in pdfs[del_date]:
            pdf_delete.addPage(pdfReader.getPage(page_num))

    # assign path
    output_filename = str(raw_pdf)

    # write leftover pdf
    with open(output_filename, 'wb') as out:
        pdf_delete.write(out)

    return pdf_delete

def Christus_TER(raw_pdf):
    # Open PDF
    pdfFileObj = open(my_files_list[3], 'rb')
    pdfReader = PdfFileReader(pdfFileObj)

    # search phrases
    search_phrase = 'we received your request to cancel your policy.'
    search_phrase_2 = 'statement of hipaa portability rights'

    pdf_ter = PdfFileWriter()
    pdf_delete = PdfFileWriter()
    pdfs = {}

    # create variable and loops
    ter_date = None
    loop = True
    keep = []

    # find date loop
    while loop == True:
        for pageNum in range(0, pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            text = pageObj.extractText()
            search_text = text.lower().split('\n')
            for words in search_text:
                match = re.match(r'^(january|february|march|april|may|june|july|august|september|october|november'
                                 r'|december)', words)
                if match:
                    print(match.group(0))

    # create date dictionary key
    ter_date = datetime.datetime.strptime(ter_date, '%B %d, %Y')
    pdfs[ter_date] = None

    # find pages with key words
    for pageNum in range(0, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        text = pageObj.extractText()
        search_text = text.lower().split('\n')
        for words in search_text:
            if search_phrase in words:
                keep.append(pageNum)
            elif search_phrase_2 in words:
                keep.append(pageNum)

    # assign pages to key
    pdfs[ter_date] = keep

    # Add pages to pdf
    for i in range(len(pdfs[ter_date])):
        pdf_ter.addPage(pdfReader.getPage(pdfs[ter_date][i]))

    # assign path
    output_filename = 'Christus_TER_{}.pdf'.format(ter_date)

    # write Delinquency PDF
    with open(output_filename, 'wb') as out:
        pdf_del.write(out)

    # find leftover pages
    for page_num in range(1, pdfReader.numPages):
        if page_num not in pdfs[ter_date]:
            pdf_delete.addPage(pdfReader.getPage(page_num))

    # assign path
    output_filename = str(raw_pdf)+ '.pdf'

    # write leftover pdf
    with open(output_filename, 'wb') as out:
        pdf_delete.write(out)

    return pdf_delete
