from pathlib import Path

def check_files( required_files):
    corrupted_files = False
    print('================== Checking Files ==================')
    for file in required_files:
        file_path = Path(file)
        if file_path.is_file() == True:
            print('File {} has found'.format(file))
        else:
            print('File {} not found'.format(file))
            corrupted_files = True
    if corrupted_files == True:
        exit = input('Press enter to exit.....')
        quit()