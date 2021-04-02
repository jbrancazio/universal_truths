import os
import zipfile
from datetime import date
from holy_grail import cm_download_path, carrier_data_path


def rename(carrier, kind, target_year, target_month):
    file_date = date(target_year, target_month, 1)
    file_month = file_date.strftime("%m")
    file_year = file_date.strftime("%Y")

    i = 1
    for f in os.scandir(cm_download_path):
        if len(os.listdir(cm_download_path)) == 2:
            while True:
                restart = False
                if f.is_file() and f.name.endswith('.xlsx') or f.name.endswith('.XLSX'):
                    os.rename(f,
                              carrier_data_path + carrier + '/'
                              + kind + '/'
                              + carrier + '_' + kind + '_' + file_year + file_month + '.xlsx')
                    print('Your file has now left purgatory')
                elif f.is_file() and f.name.endswith('.xls') or f.name.endswith('.XLS'):
                    os.rename(f,
                              carrier_data_path + carrier + '/'
                              + kind + '/'
                              + carrier + '_' + kind + '_' + file_year + file_month + '.xls')
                    print('Your file has now left purgatory')
                elif f.is_file() and f.name.endswith('.csv') or f.name.endswith('.CSV'):
                    os.rename(f,
                              carrier_data_path + carrier + '/'
                              + kind + '/'
                              + carrier + '_' + kind + '_' + file_year + file_month + '.csv')
                    print('Your file has now left purgatory')
                elif f.is_file() and f.name.endswith('.pdf') or f.name.endswith('.PDF'):
                    os.rename(f,
                              carrier_data_path + carrier + '/'
                              + kind + '/'
                              + carrier + '_' + kind + '_' + file_year + file_month + '.pdf')
                    print('Your file has now left purgatory')
                elif f.is_file() and f.name.endswith('.zip') or f.name.endswith('.ZIP'):
                    with zipfile.ZipFile(f, 'r') as zip_ref:
                        zip_ref.extractall(cm_download_path)
                        os.remove(f)
                    restart = True
                    break
                if not restart:
                    break
        elif len(os.listdir(cm_download_path)) >= 3:
            while True:
                restart = False
                if f.is_file() and f.name.endswith('.xlsx') or f.name.endswith('.XLSX'):
                    os.rename(f,
                              carrier_data_path + carrier + '/'
                              + kind + '/'
                              + carrier + '_' + kind + '_' + file_year + file_month + '_00' + str(i) + '.xlsx')
                    i = i + 1
                    print('Your file has now left purgatory')
                elif f.is_file() and f.name.endswith('.xls') or f.name.endswith('.XLS'):
                    os.rename(f,
                              carrier_data_path + carrier + '/'
                              + kind + '/'
                              + carrier + '_' + kind + '_' + file_year + file_month + '_00' + str(i) + '.xls')
                    i = i + 1
                    print('Your file has now left purgatory')
                elif f.is_file() and f.name.endswith('.csv') or f.name.endswith('.CSV'):
                    os.rename(f,
                              carrier_data_path + carrier + '/'
                              + kind + '/'
                              + carrier + '_' + kind + '_' + file_year + file_month + '_00' + str(i) + '.csv')
                    i = i + 1
                    print('Your file has now left purgatory')
                elif f.is_file() and f.name.endswith('.pdf') or f.name.endswith('.PDF'):
                    os.rename(f,
                              carrier_data_path + carrier + '/'
                              + kind + '/'
                              + carrier + '_' + kind + '_' + file_year + file_month + '_00' + str(i) + '.pdf')
                    i = i + 1
                    print('Your file has now left purgatory')
                elif f.is_file() and f.name.endswith('.zip') or f.name.endswith('.ZIP'):
                    with zipfile.ZipFile(f, 'r') as zip_ref:
                        zip_ref.extractall(cm_download_path)
                        os.remove(f)
                    restart = True
                    break
                if not restart:
                    break
        else:
            print("There are no files ready to be judged in Purgatory")

