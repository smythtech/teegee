#!/usr/bin/python

import sys
from random import randint

def main():
  lowerCaseAlpha = "abcdefghijklmnopqrstuvwxyz"
  upperCaseAlpha = lowerCaseAlpha.upper()
  numbers = "0123456789"
  symbols = "!\"$*(){}[]<>~"
  tokenLength = 0
  repeat = 1
  selection = ""
  preappend = ""
  append = "" 
  groupSize = 0
  divider = " "
  numRange = 0

  try:
    if("-t" in sys.argv):
      t = int(sys.argv[sys.argv.index("-t")+1])
      tokenLength = t
    if("-l" in sys.argv):
      selection += lowerCaseAlpha
    if("-u" in sys.argv):
      selection += upperCaseAlpha
    if("-n" in sys.argv):
      selection += numbers
    if("-s" in sys.argv):
      selection += symbols
    if("-c" in sys.argv):
      selection += sys.argv[sys.argv.index("-c")+1]
    if("-r" in sys.argv):
      repeat = int(sys.argv[sys.argv.index("-r")+1])
    if("-p" in sys.argv):
      preappend = sys.argv[sys.argv.index("-p")+1]
    if("-a" in sys.argv):
      append = sys.argv[sys.argv.index("-a")+1]
    if("-g" in sys.argv):
      groupSize = int(sys.argv[sys.argv.index("-g")+1])
    if("-d" in sys.argv):
      divider = sys.argv[sys.argv.index("-d")+1]
    if("-z" in sys.argv):
      numRange = sys.argv[sys.argv.index("-z")+1]

    if(groupSize == 0):
      groupSize = tokenLength

  except:
      printHelp()
      exit(0) 
      
  if(selection == "" and numRange == 0):
    printHelp()
    exit(0)
  
  for i in range(0, int(repeat)):
      print(preappend + generateToken(selection, tokenLength, groupSize, divider, numRange) + append)

def generateToken(alph, length, groupSize, div, numRange):
  token = ""
  t = 0
  for i in range(0, int(length)):
    if(t == groupSize):
       t = 0
       token = token + div
    if(numRange is not 0):
      token = token + str(getRangedNumber(numRange))
    else:
      token = token + alph[randint(0,len(alph)-1)]
    t+=1

  return token

def getRangedNumber(numRange):
  return randint(int(numRange.split("-")[0]), int(numRange.split("-")[1]))
  
def printHelp():
  print("TeeGee: Token Generator\n\n-t\tLength of token\n-l\tInclude lowercase letters\n-u\tInclude uppercase letters\n-n\tInclude numbers\n-s\tInclude symbols(!\"$*(){}[]<>~)\n-c\tInclude custom characters\n-r\tRepeat x times\n-p\tPreappend to token\n-a\tAppend to token\n-g\tSeperate token into groups of x size\n-d\tDivider for groups (Default is a space)\n-z\tNumber range")
  print("\nExample usage:\n1) teegee.py -l -u -n -t 13 -c %#=+\n2) teegee.py  -l -u -t 5\n3) teegee.py -t 4 -n")
if __name__=='__main__':
  main()
