import os
import zipfile
from holy_grail import cm_download_path, carrier_data_path


def rename(carrier, kind, year, mon):
    i = 1
    for f in os.scandir(cm_download_path):
        if len(os.listdir(cm_download_path)) == 2:
            while True:
                restart = False
                if f.is_file() and f.name.endswith('.xlsx') or f.name.endswith('.XLSX'):
                    os.rename(f,
                              carrier_data_path + carrier + '/'
                              + kind + '/'
                              + carrier + '_' + kind + '_' + year + mon + '.xlsx')
                    print('Your file has now left purgatory')
                elif f.is_file() and f.name.endswith('.xls') or f.name.endswith('.XLS'):
                    os.rename(f,
                              carrier_data_path + carrier + '/'
                              + kind + '/'
                              + carrier + '_' + kind + '_' + year + mon + '.xls')
                    print('Your file has now left purgatory')
                elif f.is_file() and f.name.endswith('.csv') or f.name.endswith('.CSV'):
                    os.rename(f,
                              carrier_data_path + carrier + '/'
                              + kind + '/'
                              + carrier + '_' + kind + '_' + year + mon + '.csv')
                    print('Your file has now left purgatory')
                elif f.is_file() and f.name.endswith('.pdf') or f.name.endswith('.PDF'):
                    os.rename(f,
                              carrier_data_path + carrier + '/'
                              + kind + '/'
                              + carrier + '_' + kind + '_' + year + mon + '.pdf')
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
                              + carrier + '_' + kind + '_' + year + mon + '_00' + str(i) + '.xlsx')
                    i = i + 1
                    print('Your file has now left purgatory')
                elif f.is_file() and f.name.endswith('.xls') or f.name.endswith('.XLS'):
                    os.rename(f,
                              carrier_data_path + carrier + '/'
                              + kind + '/'
                              + carrier + '_' + kind + '_' + year + mon + '_00' + str(i) + '.xls')
                    i = i + 1
                    print('Your file has now left purgatory')
                elif f.is_file() and f.name.endswith('.csv') or f.name.endswith('.CSV'):
                    os.rename(f,
                              carrier_data_path + carrier + '/'
                              + kind + '/'
                              + carrier + '_' + kind + '_' + year + mon + '_00' + str(i) + '.csv')
                    i = i + 1
                    print('Your file has now left purgatory')
                elif f.is_file() and f.name.endswith('.pdf') or f.name.endswith('.PDF'):
                    os.rename(f,
                              carrier_data_path + carrier + '/'
                              + kind + '/'
                              + carrier + '_' + kind + '_' + year + mon + '_00' + str(i) + '.pdf')
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

