from time import sleep
import requests
import os
import http.client


def file_write(file_name, mode, value):
    file = open(file_name, mode)
    file.write(value)
    file.close()


def probe_status(http_ts_link):

    ts_response = requests.get(http_ts_link)
    print(ts_response.status_code)
    print(http_ts_link)
    check = 'wget --spider '+http_ts_link
    os.system(check)
    check2 = 'ffplay '+http_ts_link
    os.system(check2)
    file_write("response.txt", "a", http_ts_link)
    '''conn = http.client.HTTPSConnection('http         weq21`s://bonappetit-samsung.amagi.tv/hls/amagi_hls_data_condenast-bonappetitsamsung/CDN/640x360_985600/index.m3u8')
    conn.request("GET", 'https://bonappetit-samsung.amagi.tv/hls/amagi_hls_data_condenast-bonappetitsamsung/CDN/640x360_985600/index.m3u8')
    ts_response = conn.getresponse()
    print(ts_response.status, ts_response.reason)'''


def first_probe_parser():
    os.system('cat first.txt |grep http >first2.txt && rm first.txt && mv first2.txt first.txt')
    with open('first.txt', 'r') as files:
        first_ts_link = files.readlines()
    return first_ts_link[0]


def probe_parser(first_ts):
    os.system('cat sample.txt |grep http >sample2.txt && rm sample.txt && mv sample2.txt sample.txt')
    with open('sample.txt', 'r') as file2:
        http_array = file2.readlines()
    if http_array[0] == first_ts:
        return first_ts
    else:
        return http_array[0]


def ts_segment_info():
    response = requests.get(
        'https://bonappetit-samsung.amagi.tv/hls/amagi_hls_data_condenast-bonappetitsamsung/CDN/640x360_985600/index'
        '.m3u8')
    file_write("first.txt", "w", response.text)

    first_ts = first_probe_parser()
    probe_status(first_ts)
    infinite_loop = 1
    while infinite_loop == 1:
        response = requests.get(
            'https://bonappetit-samsung.amagi.tv/hls/amagi_hls_data_condenast-bonappetitsamsung/CDN/640x360_985600'
            '/index.m3u8')
        file_write("sample.txt", "w", response.text)
        second_ts = probe_parser(first_ts)
        if first_ts != second_ts:
            first_ts = second_ts
            probe_status(first_ts)


if __name__ == '__main__':
    os.system('rm response.txt')
    ts_segment_info()
