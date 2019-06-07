import subprocess
from read_csv import read_csv_data


class CreateImage:
    def __init__(self):
        self.CREATE_FOLDER_NAME = 'dummy_images'
        self.CSV_PATH = './testdata.csv'

    def determine_file_info(self):
        return read_csv_data(self.CSV_PATH)

    def create_folder(self):
        cmd1 = 'md ' + self.CREATE_FOLDER_NAME
        subprocess.Popen(cmd1, shell=True)

    def create_images(self, file_name, file_size):
        cmd1 = 'cd ' + self.CREATE_FOLDER_NAME
        cmd2 = 'fsutil file createnew ' + file_name + ' ' + file_size
        print(cmd1)
        subprocess.Popen(cmd1 + ' & ' + cmd2, shell=True)


if __name__ == '__main__':
    test = CreateImage()
    # csvファイルからファイル名とファイルサイズを取得する
    data_info_list = test.determine_file_info()

    # 作成したダミーデータを格納するフォルダを作成する
    test.create_folder()
    # ファイル名とファイルサイズに応じたダミーデータを作成する
    for i in data_info_list:
        test.create_images(i[0], i[1])
