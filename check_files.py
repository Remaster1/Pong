from pathlib import Path

def check_files( required_files):
    corrupted_files = False
    print('================== Checking Files ==================')
    for file in required_files:
        file_path = Path(file)
        if file_path.is_file() == True:
            print(f'File {file} has found')
        else:
            print(f'File {file} not found')
            corrupted_files = True
    if corrupted_files == True:
        exit = input('Press enter to exit.....')
        quit()