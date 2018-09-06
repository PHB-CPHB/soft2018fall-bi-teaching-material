import os
import sys
import json
import shutil


def download(url):
    if os.path.isfile(os.path.basename(url)):
        print(f'File : {file_name already exists')
    else:
    os.system(f'wget {url}')
    print(f'Downloading file: {file_name}')


def get_url_from_config_file():
    with open('links.json') as fp:
        contents = json.load(fp)
    return contents['url']

if __name__ == '__main__':
    if not shutil.which('wget'):
        print('Error')
        sys.exit(1)
    if len(sys.argv) == 2:
        if sys.argv[-1] == '--use-config':
            url = get_url_from_config_file()
        else:
            url = sys.argv[-1]
        download(url)
    else:
        print("Error")
        sys.exit(1)