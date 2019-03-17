
# author: Xavier Collantes xaviercollantes.me
# date: Mar. 16, 2019
# file: PwnedMe.py
# purpose: Check if input password has been compromised via haveibeenpwned.com API 

import requests, hashlib, pandas,

API = 'https://api.pwnedpasswords.com/'
PARAMS = { 'range': }

def main():
  inputPw('HelloWorld')
  
    
	
# inputPw: intake password as plain text and encode 
#          into SHA-1 as required by API
def inputPw(password):
  hashP = hashlib.sha1(password)
  print(hashP)
  
def pwned(hash):
  try:
    response = requests.get(API, params=hash)
  except:

  
  return response


if __name__=='__main__':
  main()