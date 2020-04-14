import requests
import sys
import os
import hashlib
def reponse_gen(first5):
    res = requests.get('https://api.pwnedpasswords.com/range/' + first5)
    return res
def hasher(password):
    Hashed = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    return Hashed

def pass_checker(password):
    HashedValue = hasher(password)
    first5 , tail = HashedValue[:5] , HashedValue[5:]
    # print(first5,tail)
    response = reponse_gen(first5)
    hashes = []
    for lines in response.text.splitlines():
         hashes.append(tuple(lines.split(":")))

    for H , count in hashes:
        if tail == H:
            print(f'{password} has been used {count} times as password..please use different password')
            return count
    print(f'U are good to go with {password}')
    return 0


if os.path.exists(sys.argv[1]):
    passwordsLIST = []
    with open(sys.argv[1],mode="r") as passfile:
        for words in passfile.read().split(" "):
            passwordsLIST.append(words)

    for i in passwordsLIST:
        pass_checker(i)
else:
    print('file not found')