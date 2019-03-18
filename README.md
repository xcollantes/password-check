# password-check
Check your password against Troy Hunt's https://haveibeenpwned.com/  <br>
7.7 billion passwords have been consolidated and accessible to the public. 
# Why
You wouldn't want to stick your password as is into the website; this script fufills your privacy by using k-Anonymity algorithm.  
## k-Anonymity Algorithm Implementation
1) Receive your plain text password and turn into SHA-1 hash.  
_Example:_ `password123` -> `cbfdac6008f9cab4083784cbd1874f76618d2a97`
2) Submit the first 5 characters of hash or `cbfda` to PwnedPasswords API. 
3) API will return 400 to 500 hashes beginning with input or `cbfda` and respective number of instances that password has been breached.  
_Example:_ 
API Return is `c6008f9cab4083784cbd1874f76618d2a97:116847`; 116847 number of instances breached.  


4) Use hash calculated at Step 1 to determine correct hash.  
