#!-*- conding: utf8 -*-
import random

while True:
    for x in range(1):
        print (random.randint(1,6))

    resp = input("Voce quer ir de novo? s/n  ")

    if resp == 'n':
        
        print("Obrigado Por Jogar Comigo :Dn")
        break
    