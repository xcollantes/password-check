
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
  print("FULLHASH: ", hashPass)
  firstFive = hashPass[:5]
  
  resData = pwned(firstFive)
  df = pandas.Series(resData.decode('utf-8').split('\r\n'), name='sha1')
  print(df)
  hashPassTail = hashPass[-20:].upper()
  print(hashPassTail)

  matchDF = df[df.str.contains(hashPassTail)]
  
  matchDF = matchDF.str.rsplit(pat=':')
  print("MATCH DF ****")
  print(matchDF)
  print(matchDF.describe())

  
  #boolDF = df.str.contains(hashPass, regex=False).describe()
  #print(boolDF)
  
  #print(df.apply(matchCase, key=hashPass[-10:]))
  
  END = time.time()
  print("TIME ELAPSED: %s" % str(END - START))
  
  
# matchCase: find hash match against API return in Panda 
def matchCase(cell, key):
  print("KEY: ", key, " ", "cell: ", cell)
  if cell.find(key):
    print("WE GOT HIM")  
  
  
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
def pretty():  
  print()



if __name__=='__main__':
  main()