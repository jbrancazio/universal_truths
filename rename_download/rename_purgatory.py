import os
import zipfile
from datetime import date
from holy_grail import cm_download_path, carrier_data_path


def rename(carrier, kind, target_year, target_month):
    file_date = date(target_year, target_month, 1)
    file_month = file_date.strftime("%m")
    file_year = file_date.strftime("%Y")

    i = 1
    restart = True
    while restart is True:
        for f in os.scandir(cm_download_path):
            if len(os.listdir(cm_download_path)) == 2:
                if f.is_file() and f.name.endswith('.xlsx') or f.name.endswith('.XLSX'):
                    print('moving: ' + f.name)
                    os.rename(f,
                              carrier_data_path + carrier + '/' + kind + '/'
                              + carrier + '_' + kind + '_' + file_year + file_month + '.xlsx')
                    print(
                        'Your file has now left purgatory as: ' + carrier + '_' + kind + '_' + file_year + file_month +
                        '.xlsx')
                    restart = False
                elif f.is_file() and f.name.endswith('.xls') or f.name.endswith('.XLS'):
                    print('moving: ' + f.name)
                    os.rename(f,
                              carrier_data_path + carrier + '/' + kind + '/'
                              + carrier + '_' + kind + '_' + file_year + file_month + '.xls')
                    print(
                        'Your file has now left purgatory as: ' +
                        carrier + '_' + kind + '_' + file_year + file_month + '.xls')
                    restart = False
                elif f.is_file() and f.name.endswith('.csv') or f.name.endswith('.CSV'):
                    print('moving: ' + f.name)
                    os.rename(f,
                              carrier_data_path + carrier + '/' + kind + '/'
                              + carrier + '_' + kind + '_' + file_year + file_month + '.csv')
                    print(
                        'Your file has now left purgatory as: ' +
                        carrier + '_' + kind + '_' + file_year + file_month + '.csv')
                    restart = False
                elif f.is_file() and f.name.endswith('.pdf') or f.name.endswith('.PDF'):
                    print('moving: ' + f.name)
                    os.rename(f,
                              carrier_data_path + carrier + '/' + kind + '/'
                              + carrier + '_' + kind + '_' + file_year + file_month + '.pdf')
                    print(
                        'Your file has now left purgatory as: ' +
                        carrier + '_' + kind + '_' + file_year + file_month + '.pdf')
                    restart = False
                elif f.is_file() and f.name.endswith('.zip') or f.name.endswith('.ZIP'):
                    with zipfile.ZipFile(f, 'r') as zip_ref:
                        zip_ref.extractall(cm_download_path)
                        os.remove(f)
            elif len(os.listdir(cm_download_path)) >= 3:
                if f.is_file() and f.name.endswith('.xlsx') or f.name.endswith('.XLSX'):
                    print('moving: ' + f.name)
                    os.rename(f,
                              carrier_data_path + carrier + '/' + kind + '/'
                              + carrier + '_' + kind + '_' + file_year + file_month + '_00' + str(i) + '.xlsx')
                    i = i + 1
                    print('Your file has now left purgatory as: ' + carrier + '_' + kind + '_' + file_year +
                          file_month + '_00' + str(i) + '.xlsx')
                    restart = False
                elif f.is_file() and f.name.endswith('.xls') or f.name.endswith('.XLS'):
                    print('moving: ' + f.name)
                    os.rename(f,
                              carrier_data_path + carrier + '/' + kind + '/'
                              + carrier + '_' + kind + '_' + file_year + file_month + '_00' + str(i) + '.xls')
                    i = i + 1
                    print('Your file has now left purgatory as: ' + carrier + '_' + kind + '_' + file_year +
                          file_month + '_00' + str(i) + '.xls')
                    restart = False
                elif f.is_file() and f.name.endswith('.csv') or f.name.endswith('.CSV'):
                    print('moving: ' + f.name)
                    os.rename(f,
                              carrier_data_path + carrier + '/' + kind + '/'
                              + carrier + '_' + kind + '_' + file_year + file_month + '_00' + str(i) + '.csv')
                    i = i + 1
                    print('Your file has now left purgatory as: ' + carrier + '_' + kind + '_' + file_year +
                          file_month + '_00' + str(i) + '.csv')
                    restart = False
                elif f.is_file() and f.name.endswith('.pdf') or f.name.endswith('.PDF'):
                    print('moving: ' + f.name)
                    os.rename(f,
                              carrier_data_path + carrier + '/' + kind + '/'
                              + carrier + '_' + kind + '_' + file_year + file_month + '_00' + str(i) + '.pdf')
                    i = i + 1
                    print('Your file has now left purgatory as:' + carrier + '_' + kind + '_' + file_year +
                          file_month + '_00' + str(i) + '.pdf')
                    restart = False
                elif f.is_file() and f.name.endswith('.zip') or f.name.endswith('.ZIP'):
                    with zipfile.ZipFile(f, 'r') as zip_ref:
                        zip_ref.extractall(cm_download_path)
                        os.remove(f)
            else:
                print("There are no files ready to be judged in Purgatory")
                restart = False

