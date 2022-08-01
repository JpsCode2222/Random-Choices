Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
S='JAYAD PRATHMESH MANGESH RUSHIKESH SAHIL KRISHNA'
S=S.split()
print(S)
['JAYAD', 'PRATHMESH', 'MANGESH', 'RUSHIKESH', 'SAHIL', 'KRISHNA']
import random
print(f"{random.choices(S)} pay the bill")
['SAHIL'] pay the bill
print(f"{random.choices(S)} pay the bill")
['PRATHMESH'] pay the bill
print(f"{random.choices(S)} pay the bill")
['SAHIL'] pay the bill
print(f"{random.choices(S)} pay the bill")
['RUSHIKESH'] pay the bill
