# write a program to bombard a url
import requests

def takeinput():
    url = input('Enter Url: ')
    num = int(input('Enter Number of Times: '))
    request(url, num)

def request(url, num):
    print('Use CTRL/COMMAND + C to EXIT')
    i = 1
    while i <= num:
        requests.get(url)
        print(i, end=", ",flush=True)
        if i%50 == 0:
            print("")
        i = i + 1

takeinput()