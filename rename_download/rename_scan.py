# import libraries
import os
from re import search

# import paths
from secrets.secrets import carrier_data_path, scan_path, mail_path

# iterate through folder
for f in os.scandir(scan_path):

        # Move TER documents
        if search('_TER_', f.name):
                # define variable names from file name
                carrier = (f.name[:-17])
                kind = (f.name[(len(f.name)-16):-13])
                year = (f.name[-12:-8])
                new_path = str(carrier_data_path + carrier + '/' + kind + '/' + year + '/')

                # try to move. If path does not exist - make it.
                try:
                    os.rename(f, new_path + f.name)
                except:
                    os.makedirs(new_path)

        # Move DEL documents
        elif search('_DEL_', f.name):

                # define variable names from file name
                carrier = (f.name[:-17])
                kind = (f.name[(len(f.name)-16):-13])
                year = (f.name[-12:-8])
                new_path = str(carrier_data_path + carrier + '/' + kind + '/' + year + '/')

                # try to move. If path does not exist - make it.
                try:
                    os.rename(f, new_path + f.name)
                except:
                    os.makedirs(new_path)

        # Move CM documents
        elif search('_CM_', f.name):

                # define variable names from file name
                carrier = (f.name[:-14])
                kind = (f.name[(len(f.name)-13):-11])
                year = (f.name[-10:-6])
                new_path = str(carrier_data_path + carrier + '/' + kind + '/' + year + '/')

                # try to move. If path does not exist - make it.
                try:
                    os.rename(f, new_path + f.name)
                except:
                    os.makedirs(new_path)

        # Move BONUS documents
        elif search('_BONUS_', f.name):

                # define variable names from file name
                carrier = (f.name[:-17])
                kind = (f.name[(len(f.name)-16):-11])
                year = (f.name[-10:-6])
                new_path = str(carrier_data_path + carrier + '/' + kind + '/' + year + '/')

                # try to move. If path does not exist - make it.
                try:
                    os.rename(f, new_path + f.name)
                except:
                    os.makedirs(new_path)

        # Move EDD documents
        elif search('_EDD_', f.name):

                # defining variables
                kind = (f.name[5:8])
                year = (f.name[9:13])
                new_path = str(mail_path + kind + '/' + year + '/')

                # try to move. If path does not exist - make it.
                try:
                    os.rename(f, new_path + f.name)
                except:
                    os.makedirs(new_path)

        # Move TAX documents
        elif search('_TAX_', f.name):

                # defining variables
                kind = (f.name[5:8])
                year = (f.name[9:13])
                new_path = str(mail_path + kind + '/' + year + '/')

                # try to move. If path does not exist - make it.
                try:
                    os.rename(f, new_path + f.name)
                except:
                    os.makedirs(new_path)

        # Move MISC documents
        elif search('_MISC_', f.name):

                # defining variables
                kind = (f.name[5:9])
                year = (f.name[10:14])
                new_path = str(mail_path + kind + '/' + year + '/')

                # try to move. If path does not exist - make it.
                try:
                    os.rename(f, new_path + f.name)
                except:
                    os.makedirs(new_path)



        # Move Checks
        elif search('ChecksDeposited', f.name):

                # defining variables
                kind = ('Checks')
                year = (f.name[-12:-8])
                new_path = str(mail_path + kind + '/' + year + '/')

                # try to move. If path does not exist - make it.
                try:
                    os.rename(f, new_path + f.name)
                except:
                    os.makedirs(new_path)






