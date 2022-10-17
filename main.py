#!/usr/bin/env python3

from cgi import print_form
from src import adress
import sys
import os
import re

class Completion:
    def __init__(self):
        self.f = str
        self._adress = str()
        self._city = str()
        self._number = int(0)
        self._street_type = list()
        self._street_name = str()
        self._firstletter = list()
        self._secondletter = list()
        
    def print_first_letter(self):
        if len(self._firstletter) < 6:
            for k in range(len(self._firstletter)):
                    print("{" + self._firstletter[k].lower() + "}", end=' ')

    def get_first_letter(self, i):
        letter = str(self._adress[0])
        if ("0" < letter < "9") == False:
            self._firstletter.insert(i, letter)

    def get_second_letter(self, i):
        letters = str(self._adress[0] + self._adress[1])
        if ("0" < letters < "9") == False:
            self._secondletter.insert(i, letters)

    def suggest_start_city(self, user_input):
        for j in range(len(self._secondletter)):
            if user_input.upper() == self._secondletter[j][0]:
                       # print(user_input)
                print("{" + self._secondletter[j] + "}", end=' ')
        print("")
    
    def suggest_whole_city(self, user_input):
        for j in range(len(self._city)):
            if user_input.upper() == self._secondletter[j][0]:
                if self._secondletter[j][1] == self._city[1]:
                    if self._adress.count(self._city) == 1:
                        print("=> " + self._adress, end='')
                        exit(0)
                    else:
                        print("{" + self._city.upper() + "}")
                #print("second letter " + self._secondletter[j][1])
                #print("city " + self._city[1])


    def fill_class(self):
        if self._adress.count(',') == 0:
            print(self._adress  + "Unknown address", file = sys.stderr)
            #exit(84)
        self._city = self._adress.split(',')[0]
        try:
            self._number = int(self._adress.split(' ')[1])
        except ValueError:
            print(self._adress  + "Unknown address", file = sys.stderr)
            exit(84)
        self._street_type = self._adress.split(' ')[2]
        if self._street_type not in adress.streetType:
            print(self._adress  + "Unknown address", file = sys.stderr)
            #exit(84)
        self._street_name = self._adress.split(' ', 3)[3]

    def get_input(self):
        while True:
            try:
                user_input = input()
            except EOFError as e:
                break
                #exit(84)
            if user_input.strip() == "ABORT":
                #print("aborted")
                exit(0)
            else:
                self.suggest_start_city(user_input)
                self.suggest_whole_city(user_input)
                
    def _count_generator(self,reader):
        b = reader(1024 * 1024)
        while b:
            yield b
            b = reader(1024 * 1024)

    def nb_lines(self, x):
        with open(sys.argv[1], 'rb') as fp:
            c_generator = self._count_generator(fp.raw.read)
            count = sum(buffer.count(b'\n') for buffer in c_generator)
            if (count + 1) == 1:
                print("=> " + x)
                exit(0)
    
    def check_file(self):
        file_path = sys.argv[1]
        try:
            self._f = open(sys.argv[1], 'r')
        except OSError:
            print("Invalid argument")
            sys.exit(84)
        if os.stat(file_path).st_size == 0:
            print("Invalid argument")
            exit(84)
        i = 0        
        for x in self._f:
            self.nb_lines(x)
            self._adress = x
            self.fill_class()
            self.get_first_letter(i)
            self.get_second_letter(i)
            i += 1
       # print("city =" + self._city[0])
       # print("city =" + self._city[1])
        self._firstletter = list(dict.fromkeys(self._firstletter))
        self._firstletter = [x.lower() for x in self._firstletter]
        self.print_first_letter()
        print("")
        #self._firstletter.sort()
        self._secondletter = list(dict.fromkeys(self._secondletter))
        
    def ac_error_handling(self):
        if len(sys.argv) != 2:
            print("Invalid argument")
            exit(84)

    def main(self):
        self.ac_error_handling()
        self.check_file()
        self.get_input()

def autocompletion():
    completion = Completion()
    completion.main()

if __name__ == '__main__':
       autocompletion()
    #print(adress.streetType)
