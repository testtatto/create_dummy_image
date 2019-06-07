import subprocess
from read_csv import read_csv_data


class CreateImage:
    def __init__(self):
        self.CREATE_FOLDER_PATH = '''C:\\Users\\tatsuto.inoue\\Desktop'''
        self.CREATE_FOLDER_NAME = 'dummy_images'
        self.CREATE_FILE_NAME = 'sample'
        self.CSV_PATH = './testdata.csv'

    def create(self, file_name, file_size):
        cmd = 'cd ' + self.CREATE_FOLDER_PATH
        subprocess.Popen(cmd)
        cmd = 'md ' + self.CREATE_FOLDER_NAME
        subprocess.Popen(cmd)
        cmd = 'cd ' + self.CREATE_FOLDER_NAME
        subprocess.Popen(cmd)
        cmd = 'fsutil file createnew ' + file_name + ' ' + file_size
        subprocess.Popen(cmd)


if __name__ == '__main__':
    test = CreateImage()
    data_info_list = test.read_csv_data(test.CSV_PATH)
    print(data_info_list[0])
