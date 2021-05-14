import os
import zipfile
from datetime import date


def rename_cm(carrier, kind, target_year, target_month):
    file_date = date(target_year, target_month, 1)
    file_month = file_date.strftime("%m")
    file_year = file_date.strftime("%Y")

    i = 1
    restart = True
    while restart is True:
        for f in os.scandir('../../../Purgatory/cm'):
            if len(os.listdir('../../../Purgatory/cm')) == 2:
                if f.is_file() and f.name.endswith('.xlsx') or f.name.endswith('.XLSX'):
                    print('moving: ' + f.name)
                    os.rename(f,
                              '../../carrier_data/' + carrier + '/' + kind + '/' + 'raw/'
                              + carrier + '_' + kind + '_' + date + '.xlsx')
                    print(
                        'Your file has now left purgatory as: ' + carrier + '_' + kind + '_' + date +
                        '.xlsx')
                    restart = False
                elif f.is_file() and f.name.endswith('.xls') or f.name.endswith('.XLS'):
                    print('moving: ' + f.name)
                    os.rename(f,
                              '../../carrier_data/' + carrier + '/' + kind + '/' + 'raw/'
                              + carrier + '_' + kind + '_' + date + '.xls')
                    print(
                        'Your file has now left purgatory as: ' +
                        carrier + '_' + kind + '_' + date + '.xls')
                    restart = False
                elif f.is_file() and f.name.endswith('.csv') or f.name.endswith('.CSV'):
                    print('moving: ' + f.name)
                    os.rename(f,
                              '../../carrier_data/' + carrier + '/' + kind + '/' + 'raw/'
                              + carrier + '_' + kind + '_' + date + '.csv')
                    print(
                        'Your file has now left purgatory as: ' +
                        carrier + '_' + kind + '_' + date + '.csv')
                    restart = False
                elif f.is_file() and f.name.endswith('.pdf') or f.name.endswith('.PDF'):
                    print('moving: ' + f.name)
                    os.rename(f,
                              '../../carrier_data/' + carrier + '/' + kind + '/' + 'raw/'
                              + carrier + '_' + kind + '_' + date + '.pdf')
                    print(
                        'Your file has now left purgatory as: ' +
                        carrier + '_' + kind + '_' + date + '.pdf')
                    restart = False
                elif f.is_file() and f.name.endswith('.zip') or f.name.endswith('.ZIP'):
                    with zipfile.ZipFile(f, 'r') as zip_ref:
                        zip_ref.extractall('../../../Purgatory/cm')
                        os.remove(f)
            elif len(os.listdir('../../../Purgatory/cm')) >= 3:
                if f.is_file() and f.name.endswith('.xlsx') or f.name.endswith('.XLSX'):
                    print('moving: ' + f.name)
                    os.rename(f,
                              '../../carrier_data/' + carrier + '/' + kind + '/' + 'raw/'
                              + carrier + '_' + kind + '_' + date + '_00' + str(i) + '.xlsx')
                    i = i + 1
                    print('Your file has now left purgatory as: ' + carrier + '_' + kind + '_' + date
                          + '_00' + str(i) + '.xlsx')
                    restart = False
                elif f.is_file() and f.name.endswith('.xls') or f.name.endswith('.XLS'):
                    print('moving: ' + f.name)
                    os.rename(f,
                              '../../carrier_data/' + carrier + '/' + kind + '/' + 'raw/'
                              + carrier + '_' + kind + '_' + date + '_00' + str(i) + '.xls')
                    i = i + 1
                    print('Your file has now left purgatory as: ' + carrier + '_' + kind + '_' + date
                          + '_00' + str(i) + '.xls')
                    restart = False
                elif f.is_file() and f.name.endswith('.csv') or f.name.endswith('.CSV'):
                    print('moving: ' + f.name)
                    os.rename(f,
                              '../../carrier_data/' + carrier + '/' + kind + '/' + 'raw/'
                              + carrier + '_' + kind + '_' + date + '_00' + str(i) + '.csv')
                    i = i + 1
                    print('Your file has now left purgatory as: ' + carrier + '_' + kind + '_' + date
                          + '_00' + str(i) + '.csv')
                    restart = False
                elif f.is_file() and f.name.endswith('.pdf') or f.name.endswith('.PDF'):
                    print('moving: ' + f.name)
                    os.rename(f,
                              '../../carrier_data/' + carrier + '/' + kind + '/' + 'raw/'
                              + carrier + '_' + kind + '_' + date + '_00' + str(i) + '.pdf')
                    i = i + 1
                    print('Your file has now left purgatory as:' + carrier + '_' + kind + '_' + date
                          + '_00' + str(i) + '.pdf')
                    restart = False
                elif f.is_file() and f.name.endswith('.zip') or f.name.endswith('.ZIP'):
                    with zipfile.ZipFile(f, 'r') as zip_ref:
                        zip_ref.extractall('../../../Purgatory/cm')
                        os.remove(f)
            else:
                print("There are no files ready to be judged in Purgatory")
                restart = False


def rename_bob(carrier, kind, date):

    i = 1
    restart = True
    while restart is True:
        for f in os.scandir('../../../Purgatory/cm'):
            if len(os.listdir('../../../Purgatory/cm')) == 2:
                if f.is_file() and f.name.endswith('.xlsx') or f.name.endswith('.XLSX'):
                    print('moving: ' + f.name)
                    os.rename(f,
                              '../../carrier_data/' + carrier + '/' + kind + '/' + 'raw/'
                              + carrier + '_' + kind + '_' + date + '.xlsx')
                    print(
                        'Your file has now left purgatory as: ' + carrier + '_' + kind + '_' + date +
                        '.xlsx')
                    restart = False
                elif f.is_file() and f.name.endswith('.xls') or f.name.endswith('.XLS'):
                    print('moving: ' + f.name)
                    os.rename(f,
                              '../../carrier_data/' + carrier + '/' + kind + '/' + 'raw/'
                              + carrier + '_' + kind + '_' + date + '.xls')
                    print(
                        'Your file has now left purgatory as: ' +
                        carrier + '_' + kind + '_' + date + '.xls')
                    restart = False
                elif f.is_file() and f.name.endswith('.csv') or f.name.endswith('.CSV'):
                    print('moving: ' + f.name)
                    os.rename(f,
                              '../../carrier_data/' + carrier + '/' + kind + '/' + 'raw/'
                              + carrier + '_' + kind + '_' + date + '.csv')
                    print(
                        'Your file has now left purgatory as: ' +
                        carrier + '_' + kind + '_' + date + '.csv')
                    restart = False
                elif f.is_file() and f.name.endswith('.pdf') or f.name.endswith('.PDF'):
                    print('moving: ' + f.name)
                    os.rename(f,
                              '../../carrier_data/' + carrier + '/' + kind + '/' + 'raw/'
                              + carrier + '_' + kind + '_' + date + '.pdf')
                    print(
                        'Your file has now left purgatory as: ' +
                        carrier + '_' + kind + '_' + date + '.pdf')
                    restart = False
                elif f.is_file() and f.name.endswith('.zip') or f.name.endswith('.ZIP'):
                    with zipfile.ZipFile(f, 'r') as zip_ref:
                        zip_ref.extractall('../../../Purgatory/cm')
                        os.remove(f)
            elif len(os.listdir('../../../Purgatory/cm')) >= 3:
                if f.is_file() and f.name.endswith('.xlsx') or f.name.endswith('.XLSX'):
                    print('moving: ' + f.name)
                    os.rename(f,
                              '../../carrier_data/' + carrier + '/' + kind + '/' + 'raw/'
                              + carrier + '_' + kind + '_' + date + '_00' + str(i) + '.xlsx')
                    i = i + 1
                    print('Your file has now left purgatory as: ' + carrier + '_' + kind + '_' + date
                          + '_00' + str(i) + '.xlsx')
                    restart = False
                elif f.is_file() and f.name.endswith('.xls') or f.name.endswith('.XLS'):
                    print('moving: ' + f.name)
                    os.rename(f,
                              '../../carrier_data/' + carrier + '/' + kind + '/' + 'raw/'
                              + carrier + '_' + kind + '_' + date + '_00' + str(i) + '.xls')
                    i = i + 1
                    print('Your file has now left purgatory as: ' + carrier + '_' + kind + '_' + date
                          + '_00' + str(i) + '.xls')
                    restart = False
                elif f.is_file() and f.name.endswith('.csv') or f.name.endswith('.CSV'):
                    print('moving: ' + f.name)
                    os.rename(f,
                              '../../carrier_data/' + carrier + '/' + kind + '/' + 'raw/'
                              + carrier + '_' + kind + '_' + date + '_00' + str(i) + '.csv')
                    i = i + 1
                    print('Your file has now left purgatory as: ' + carrier + '_' + kind + '_' + date
                          + '_00' + str(i) + '.csv')
                    restart = False
                elif f.is_file() and f.name.endswith('.pdf') or f.name.endswith('.PDF'):
                    print('moving: ' + f.name)
                    os.rename(f,
                              '../../carrier_data/' + carrier + '/' + kind + '/' + 'raw/'
                              + carrier + '_' + kind + '_' + date + '_00' + str(i) + '.pdf')
                    i = i + 1
                    print('Your file has now left purgatory as:' + carrier + '_' + kind + '_' + date
                          + '_00' + str(i) + '.pdf')
                    restart = False
                elif f.is_file() and f.name.endswith('.zip') or f.name.endswith('.ZIP'):
                    with zipfile.ZipFile(f, 'r') as zip_ref:
                        zip_ref.extractall('../../../Purgatory/cm')
                        os.remove(f)
            else:
                print("There are no files ready to be judged in Purgatory")
                restart = False