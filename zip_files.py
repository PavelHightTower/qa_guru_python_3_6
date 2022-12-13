from zipfile import ZipFile
import os
from os.path import basename


def zip_file(new_dir_name: str, zip_file_name: str, dir_with_files_to_zip: str):
    os.mkdir(new_dir_name)
    with ZipFile(f'{new_dir_name}/{zip_file_name}', 'w') as z:
        for folderName, subfiles, filenames in os.walk(f'{dir_with_files_to_zip}'):
            for filename in filenames:
                filePath = os.path.join(folderName, filename)
                z.write(filePath, basename(filePath))


zip_file('resources', 'test.zip', 'files')