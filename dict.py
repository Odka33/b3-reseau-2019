#!/usr/bin/python3.4

# -*- coding: utf-8-*-

# ==============================================================================
# title           :brute.py .                                                  #
# description     :Dictionnary /etc/shadow                                     #
# author          :Odka33 - Elie BEN AYOUN                                     #
# date            :14/01/2019                                                  #
# version         :0.1                                                         #
# usage           :python3 dict.py                                            #
# python_version  :3.4.3                                                       #
# ==============================================================================

from hashlib import md5

def dictionnaryAttack():

    dictpath = "/Users/eliebenayoun/Desktop/TP1/dico_mini_fr.txt"
    shadowpath = "/Users/eliebenayoun/Desktop/TP1/shadow.txt"
    matchfound = "/Users/eliebenayoun/Desktop/TP1/matchfound.txt"

    with open(shadowpath) as f:
        shadowfile = f.readlines()
        users = []
        shadowfile = [x.strip() for x in shadowfile]
        for line in shadowfile:
            splited_line = line.split(':')
            users.append({
                "login": splited_line[0],
                "hash": splited_line[1]
            })
    with open(dictpath) as f:
        passwords = f.readlines()
        passwords = [x.strip() for x in passwords]

        for pwd in passwords:
            pwdhash = md5(str.encode(pwd)).hexdigest()
            for user in users:
                if pwdhash in user["hash"]:
                    print("Match found for user: "+user["login"])
                    print("password: "+pwd)
                    mf = open(matchfound, "a")
                    mf.write("Match found for user: " + user["login"]+"\n")
                    mf.write("password: "+pwd+"\n")

if __name__ == '__main__':
    dictionnaryAttack()
