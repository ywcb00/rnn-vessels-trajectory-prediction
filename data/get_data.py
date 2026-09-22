#!/usr/bin/env python3

import requests

BASE_URL = "http://aisdata.ais.dk"
FILE_PREFIX = "aisdk-"
FILE_SUFFIX = ".zip"

def downloadAndSaveFile(url, dest):
    response = requests.get(url)
    if response.status_code == 200:
        with open(dest, 'wb') as file:
            file.write(response.content)
        return True
    else:
        return False

def downloadAISData(year, month, day):
    date_string = f'{year}-{month:02}-{day:02}'
    file_name = f'{FILE_PREFIX}{date_string}{FILE_SUFFIX}'
    url = f'{BASE_URL}/{file_name}'
    dest = file_name
    successful = downloadAndSaveFile(url, dest)
    if not successful:
        url = f'{BASE_URL}/{year}/{file_name}'
        successful = downloadAndSaveFile(url, dest)
    if successful:
        print(f'File {url} downloaded successfully.')
    else:
        print(f'FAILED to download file {url}')

YEAR = 2025
for MONTH in range(1, 13):
    for DAY in range(1, 32):
        downloadAISData(YEAR, MONTH, DAY)
