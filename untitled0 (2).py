# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/113mKJAgBgSokjXL5yuJY5lAMVCfRbD_f
"""

i1=float(input("Enter the price of i1: $"))
i2=float(input("Enter the price of i2: $"))
i3=float(input("Enter the price of i3: $"))
total_cost=i1+i2+i3
if total_cost>50:
  discount=total_cost*0.10
  total_cost-=discount
  print(f"A 10% discount has been applied:{discount:.2f}")
  print(f"Total cost after discount:{total_cost:.2f}")