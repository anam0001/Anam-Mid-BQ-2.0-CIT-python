# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-1B9plblg5VPv2ihZFrHfd0q_ynuTbUR
"""

print("Simple Calculator")
num1=int(input("\n\nEnter a First number:  "))
num2=int(input("Enter another number:  "))
print("Enter a operator (+,-,*,/) to perform operation")
opr=input("Enter a operator: \n")

if opr=="+":
  sum=num1+num2
  print(f"Your answer is \"{sum}\"")

if opr=="-":
  diff=num1-num2
  print(f"Your answer is \"{diff}\"")

if opr=="*":
  prod=num1*num2
  print(f"Your answer is \"{prod}\"")

if opr=="/":
  div=num1/num2
  print(f"Your answer is \"{div}\"")