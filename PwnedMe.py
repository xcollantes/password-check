
# author: Xavier Collantes xaviercollantes.me
# date: Mar. 16, 2019
# file: PwnedMe.py
# purpose: Check if input password has been compromised via haveibeenpwned.com API 

import requests, hashlib, pandas, logging, time

logging.basicConfig(level=logging.DEBUG)
API = 'https://api.pwnedpasswords.com/range/'

def main():
  START = time.time()
  hashPass = inputPw('Password')
  firstFive = hashPass[:5]
  
  resData = pwned(firstFive)
  df = pandas.Series(resData.decode('utf-8').split('\r\n'), name='sha1')
  
  hashPassTail = hashPass[-20:].upper()
  
  matchDF = df[df.str.contains(hashPassTail)]
  matchDF = matchDF.str.rsplit(pat=':', n=1, expand=True).rename(columns={ 0: 'Passwd_Hash', 1: 'Times_Found' })

  pretty(matchDF)
  
  
# inputPw: intake password as plain text and encode 
#          into SHA-1 as required by API
# password: plain text password 
# hashP: full SHA-1 hash 
def inputPw(password):
  hashP = hashlib.sha1(password.encode())  # Encode to UTF-8 
  return hashP.hexdigest()


# pwned: access API, find password info 
# hash: first 5 characters of password, hashed 
def pwned(hash):
  try:
    response = requests.get(API + hash)
    logging.debug(response.status_code)
  except:
    logging.error("Uh-oh! " + response.status_code)
  
  return response.content


# pretty: print out string  
# df: input dataframe 
def pretty(df):
  if df == None:
    print("Congrats! Your password has not been leaked!")



if __name__=='__main__':
  main()