# imports
from PyPDF2 import PdfFileReader, PdfFileWriter
import os
import re
import pandas as pd
import numpy as np
from datetime import datetime


def list_files(filepath, filetype):
    paths = []
    for root, dirs, files in os.walk(filepath):
        for file in files:
            if file.lower().endswith(filetype.lower()):
                paths.append(os.path.join(root, file))
    return paths


def Christus_parser(raw_pdf):
    # Open PDF
    pdfFileObj = open(raw_pdf, 'rb')
    pdfReader = PdfFileReader(pdfFileObj)

    filename = os.path.basename(raw_pdf)

    del_carrier = filename.split('_')[0]
    del_date = filename.split('_')[1].split('.')[0]

    pdf_del = PdfFileWriter()
    pdf_ter = PdfFileWriter()
    pdf_extra = PdfFileWriter()

    keep_del = []
    keep_ter = []
    extra = []
    raw_data = pd.DataFrame(columns=['Carrier', 'Name', 'Member_Id', 'Contact_date', 'Contact_Type', 'Due_Date'])

    # find pages with key words
    for pageNum in range(0, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        text = pageObj.extractText()
        lines = set(text.lower().split('\n'))
        name = None
        member_id = None
        contact_type = None
        due_date = None
        for line in lines:
            for match in re.finditer(r'^\>?\w*\!?t?\)?dear\s(\w+\s\w+\s?\w+?),?$', line):
                name = str(re.sub(r',?', '', re.sub(r'\>?\w*\!?t?\)?dear\s', '', match.group())))
            for match in re.finditer(r'^member\sid[:|;]\s(\d+)', line):
                member_id = str(re.sub(r'^member\sid[:|;]\s', '', match.group()))
            if re.match(r'>?\w+:\s\w+\s\w+\scancellation\s\w+', line):
                keep_ter.append(pageNum)
                contact_type = 'Termination'
            if re.match(r'\w+:\s\w+\s\w+\s\w+\s\w+\sterminated', line):
                keep_ter.append(pageNum)
                contact_type = 'Termination'
            if re.match(r'\w+:\s\w+\s\w+\s\w+\s\w+\scancelled', line):
                keep_ter.append(pageNum)
                contact_type = 'Termination'
            if re.match(r'\w+\s\w+\shipaa\s\w+\s\w+', line):
                keep_ter.append(pageNum)
            if re.match(r'\w+:\swelcome!', line):
                contact_type = 'Welcome'
            if re.match(r're\:\scredit\scard\spayment\sprocess', line) :
                contact_type = 'Direct Deposit Change'
            if re.match(r'^\$\d+\.\d{2}(\d{2}\/\d{2}\/\d{4})', line) or \
                    re.match(r'^(\d{2}\/\d{2}\/\d{4})\$\d+\.\d{2}', line) or \
                    re.match(r'^(\d{2}\/\d{2}\/\d{4})make\scheck\spayable', line) :
                keep_del.append(pageNum)
                keep_del.append(pageNum + 1)
                match_date = re.match(r'^\$\d+\.\d{2}(\d{2}\/\d{2}\/\d{4})', line)
                match_date_2 = re.match(r'^(\d{2}\/\d{2}\/\d{4})\$\d+\.\d{2}', line)
                match_date_3 = re.match(r'^(\d{2}\/\d{2}\/\d{4})make\scheck\spayable', line)
                if match_date is not None :
                    due_date = match_date.groups()[0]
                if match_date_2 is not None :
                    due_date = match_date_2.groups()[0]
                if match_date_2 is not None :
                    due_date = match_date_2.groups()[0]
                contact_type = 'payment due'
                pageObj_2 = pdfReader.getPage(pageNum + 1)
                text_2 = pageObj_2.extractText()
                lines_2 = set(text_2.lower().split('\n'))
                for line_2 in lines_2 :
                    for match in re.finditer(r'\>?\w*\!?t?\)?dear\s(\w+\s\w+\s?\w+?),?$', line_2) :
                        name = str(re.sub(r',?', '', re.sub(r'\>?\w*\!?t?\)?dear\s', '', match.group())))
            if re.match(r'^\$\d+\.\d{2}(upon\sreceipt)', line) or \
                    re.match(r'^(upon\sreceipt)\$\d+\.\d{2}', line) or \
                    re.match(r'^upon\sreceipt$', line) :
                keep_del.append(pageNum)
                keep_del.append(pageNum + 1)
                match_date = re.match(r'^\$\d+\.\d{2}(upon\sreceipt)', line)
                match_date_2 = re.match(r'^(upon\sreceipt)\$\d+\.\d{2}', line)
                match_date_3 = re.match(r'^(upon\sreceipt)$', line)
                if match_date is not None :
                    due_date = match_date.groups()[0]
                if match_date_2 is not None :
                    due_date = match_date_2.groups()[0]
                if match_date_3 is not None :
                    due_date = match_date_3.groups()[0]
                contact_type = 'past due'
                pageObj_2 = pdfReader.getPage(pageNum + 1)
                text_2 = pageObj_2.extractText()
                lines_2 = set(text_2.lower().split('\n'))
                for line_2 in lines_2 :
                    for match in re.finditer(r'\>?\w*\!?t?\)?dear\s(\w+\s\w+\s?\w+?),?$', line_2) :
                        name = str(re.sub(r',?', '', re.sub(r'\>?\w*\!?t?\)?dear\s', '', match.group())))
        if name is not None or member_id is not None :
            if name in raw_data.values and member_id in raw_data.values :
                pass
            else:
                raw_data = raw_data.append({'Carrier': del_carrier, 'Name': name, 'Member_Id': member_id,
                                            'Contact_date': del_date, 'Contact_Type': contact_type,
                                            'Due_Date': due_date}, ignore_index=True)

        if pageNum not in keep_del and pageNum not in keep_ter:
            extra.append(pageNum)

    # Add pages to pdf
    if len(keep_del) > 0:
        for i in range(len(keep_del)):
            pdf_del.addPage(pdfReader.getPage(keep_del[i]))

        # assign path
        output_filename = '/Users/joshuabrancazio/Documents/carrier_data/' + str(del_carrier) + '/{}_DEL_{}.pdf'.format(
            str(del_carrier), str(del_date))

        # write Delinquency PDF
        with open(output_filename, 'wb') as out :
            pdf_del.write(out)

    # Add pages to pdf
    if len(keep_ter) > 0 :
        for i in range(len(keep_ter)) :
            pdf_ter.addPage(pdfReader.getPage(keep_ter[i]))

        # assign path
        output_filename = '/Users/joshuabrancazio/Documents/carrier_data/' + str(del_carrier) + '/{}_TER_{}.pdf'.format(
            str(del_carrier), str(del_date))

        # write Delinquency PDF
        with open(output_filename, 'wb') as out :
            pdf_ter.write(out)

    # Add pages to pdf
    if len(extra) > 0 :
        for i in range(len(extra)) :
            pdf_extra.addPage(pdfReader.getPage(extra[i]))

        # assign path
        output_filename = '/Users/joshuabrancazio/Documents/carrier_data/' + str(
            del_carrier) + '/{}_Extra_{}.pdf'.format(str(del_carrier), str(del_date))

        # write Delinquency PDF
        with open(output_filename, 'wb') as out :
            pdf_extra.write(out)
    return raw_data


def Cigna_parser(raw_pdf):
    # Open PDF
    pdfFileObj = open(raw_pdf, 'rb')
    pdfReader = PdfFileReader(pdfFileObj)

    filename = os.path.basename(raw_pdf)

    del_carrier = filename.split('_')[0]
    del_date = filename.split('_')[1].split('.')[0]

    pdf_del = PdfFileWriter()
    pdf_ter = PdfFileWriter()
    pdf_extra = PdfFileWriter()

    keep_del = []
    keep_ter = []
    extra = []
    raw_data = pd.DataFrame(columns=['Carrier', 'Name', 'Member_Id', 'Contact_date', 'Contact_Type', 'Due_Date'])

    # find pages with key words
    for pageNum in range(0, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        text = pageObj.extractText()
        lines = set(text.lower().split('\n'))
        name = None
        member_id = None
        contact_type = None
        due_date = None
        s_date = None
        for line in lines:
            for match in re.finditer(r'^\w*\.?hello\s(\w+-?\s\w+\s?-?\w+?)', line):
                name = str(re.sub(r'^\w*\.?hello\s', '', match.group()))
            for match in re.finditer(r'^\>?\w*\!?t?\)?dear\s*(\w+-?\s\w+\s?-?\w+?)[:;]$', line):
                name = str(re.sub(r'[:;]?', '', re.sub(r'\>?\w*\!?t?\)?dear\s*', '', match.group())))
            for match in re.finditer(r'case[\:\;]\s?(\w{6})', line):
                member_id = str(re.sub(r'case[\:\;]\s?', '', match.group()))
            for match in re.finditer(r'\w+\s\d{1,2}[\,\.]\s?\d{4}', line):
                s_date = str(re.sub(r'\.', ',', match.group()))
                s_date = str(re.sub(r' ', '', s_date))
                s_date = datetime.strptime(s_date, '%B%d,%Y')
            if re.match(r'^[\.!]deletion\sof\scoverage$', line) or re.match('^[\.!]subsidy\samount\schange$', line):
                contact_type = 'coverage adjustment'
            if re.match(r'\w*\s\w*\stermination\s\w*\s\w*\s\w*\.$', line):
                keep_ter.append(pageNum)
                keep_ter.append(pageNum + 1)
                contact_type = 'termination'
            if re.match(r'\w*\s?\w*?\s?\w*\ssaying\sgood-bye\.', line):
                keep_ter.append(pageNum)
                keep_ter.append(pageNum + 1)
                contact_type = 'termination'
            if re.match(r'this\sis\san\surgent\srequest\.', line):
                keep_del.append(pageNum)
                keep_del.append(pageNum + 1)
                keep_del.append(pageNum + 2)
                keep_del.append(pageNum + 3)
                contact_type = 'past due'
                due_date = 'upon receipt'
            if re.match(r'your\sinsurance\spremium\sis\sone\smonth\spast', line) or \
                    re.match(r'\spast\sdue\.', line) or \
                    re.match(r'are still within your 31-day grace period\.', line) or \
                    re.match(r'this\sis\sa\s?friendly\sreminder\.', line):
                keep_del.append(pageNum)
                keep_del.append(pageNum + 1)
                keep_del.append(pageNum + 2)
                keep_del.append(pageNum + 3)
                contact_type = 'past due'
                due_date = 'upon receipt'
            if re.match(r'welcome\sto\scigna\!', line):
                contact_type = 'welcome'
        if name is not None or member_id is not None:
            if name in raw_data.values and member_id in raw_data.values:
                pass
            else :
                raw_data = raw_data.append({'Carrier': del_carrier, 'Name': name, 'Member_Id': member_id,
                                            'Contact_date': s_date.strftime('%Y%m%d'), 'Contact_Type': contact_type,
                                            'Due_Date': due_date}, ignore_index=True)
        if pageNum not in keep_del and pageNum not in keep_ter:
            extra.append(pageNum)

    # Add pages to pdf
    if len(keep_del) > 0:
        for i in range(len(keep_del)):
            pdf_del.addPage(pdfReader.getPage(keep_del[i]))

        # assign path
        output_filename = '/Users/joshuabrancazio/Documents/carrier_data/' + str(del_carrier) + '/{}_DEL_{}.pdf'.format(
            str(del_carrier), str(del_date))

        # write Delinquency PDF
        with open(output_filename, 'wb') as out:
            pdf_del.write(out)

    # Add pages to pdf
    if len(keep_ter) > 0 :
        for i in range(len(keep_ter)) :
            pdf_ter.addPage(pdfReader.getPage(keep_ter[i]))

        # assign path
        output_filename = '/Users/joshuabrancazio/Documents/carrier_data/' + str(del_carrier) + '/{}_TER_{}.pdf'.format(
            str(del_carrier), str(del_date))

        # write Delinquency PDF
        with open(output_filename, 'wb') as out:
            pdf_ter.write(out)

    # Add pages to pdf
    if len(extra) > 0:
        for i in range(len(extra)):
            pdf_extra.addPage(pdfReader.getPage(extra[i]))

        # assign path
        output_filename = '/Users/joshuabrancazio/Documents/carrier_data/' + str(
            del_carrier) + '/{}_Extra_{}.pdf'.format(str(del_carrier), str(del_date))

        # write Delinquency PDF
        with open(output_filename, 'wb') as out:
            pdf_extra.write(out)
    return raw_data

# doing the work
my_file_list = list_files('/Users/joshuabrancazio/Purgatory/scan', '.pdf')
print(my_file_list)

master_df = pd.read_csv('~/Documents/mail/master_mail_contact.csv')

master_df = master_df.append(Cigna_parser('/Users/joshuabrancazio/Purgatory/scan/Cigna_202103.pdf'), sort=False, ignore_index=True)


master_df.to_csv('~/Documents/mail/master_mail_contact.csv', index= False)

master_df = master_df[(master_df.Contact_date != '20210408') | (master_df.Carrier != 'Cigna')]
