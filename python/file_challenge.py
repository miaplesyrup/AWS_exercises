# pylint: disable=missing-module-docstring
# import csv
# import os
# import subprocess
# import sys

# def gumawa_ng_folders_at_kopyahin_ang_file(arg):
#     with open(arg) as file:
#         reader = csv.reader(file, delimiter=',')
#         rows = list(reader)

#         directories = rows[0]

#         # Gumawa ng folders
#         for laman_ni_row_zero in directories:
#             os.makedirs(laman_ni_row_zero)

#         # Gumawa ng text files (maliban sa first row)
#         for laman_ni_row_zero_index, laman_ni_row_zero in enumerate(directories):
#             for row in rows[1:]:
#                 text = row[laman_ni_row_zero_index]
#                 with open(os.path.join(laman_ni_row_zero, f'{text}.txt'), 'w') as sulat:
#                     sulat.write(f'KAMUSTA NAMAN ANG MONDAY MO? {text}')
# def main(arg):
#     gumawa_ng_folders_at_kopyahin_ang_file(arg)

#     # Listahan ng laman ng folders
#     for polder in os.listdir():
#         if os.path.isdir(polder):
#             subprocess.run(['ls', '-la', polder])

# if __name__ == "__main__":
#     main(sys.argv[1])

import csv
import os
import sys

def gumawa_ng_folders_at_kopyahin_ang_file(arg):
    with open(arg) as file:
        reader = csv.reader(file, delimiter=',')
        rows = list(reader)

        directories = rows[0]

        [os.makedirs(directory) for directory in directories]

        [open(f'{directory}/{row[index]}.txt', 'a').close() for index, directory in enumerate(directories) for row in rows[1:]]

def main(arg):
    gumawa_ng_folders_at_kopyahin_ang_file(arg)

    # Listahan ng laman ng folders
    [print(f'Contents of {polder}:\n{", ".join(os.listdir(polder))}') for polder in os.listdir() if os.path.isdir(polder)]

if __name__ == "__main__":
    main(sys.argv[1])
