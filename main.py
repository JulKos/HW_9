import requests
from pprint import pprint

from ya_disk import YaUploader
from SOF import Stackoverflow

if __name__ == '__main__':
    token = ""
    path_to_file = "netology/test3.txt"
    filename = "test.txt"
    uploader = YaUploader(token=token)
    result = uploader.upload_file_to_disk(path_to_file, filename)

if __name__ == '__main__':
    Stackoverflow = Stackoverflow()
    pprint(Stackoverflow.get_all_requests())