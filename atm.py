# -*- coding: utf-8 -*-
"""ATM.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VIEuw7wvvNCIQwurJL7pnwegE3PsLiqe
"""

from datetime import datetime
import pytz
import pandas as pd

local_timezone = pytz.timezone('America/Los_Angeles')

class BankAccount:
  """
  This Class serves as an ATM which support deposit and withdraw
  """
  def __init__(self, account_holder, balance = 0):
    self.account_holder = account_holder
    self.balance = balance

  # Timer
  def get_time(self):
    return datetime.now(local_timezone).strftime("%Y-%m-%d %H:%M:%S")

  # define Deposit function
  def deposit(self, amount, auto_message = True):
    self.balance += amount
    if auto_message:
      print(f"{self.get_time()}"
            f"\nWecome Back, {self.account_holder}!"
            f"\nDeposit Completed."
            f"\nDeposit: {amount}. Here's your Remaining Balance: {self.balance}")

  # define Withdraw function
  def withdraw(self, amount, auto_message = True):
    if self.balance < amount:
      print(f"{self.get_time()}"
            f"\nWecome Back, {self.account_holder}!"
            f" \nTrasaction Failed."
            f"\nLow Balance, Remaining Balance: {self.balance}")
    else:
      self.balance -= amount
      if auto_message:
        print(f"{self.get_time()}"
              f"\nWecome Back, {self.account_holder}!"
              f"\nWithdraw Completed."
              f"\nWithdraw: {amount}. Here's your remaining balance: {self.balance}")

  #define Transfer
  def transfer(self, recipient, transfer_amount):
    if self.balance < transfer_amount: # Insufficient Balance
      print(f"{self.get_time()}"
            f"\nWecome Back, {self.account_holder}!"
            f"\nTransfer Failed;"
            f"\nRemaining Balance: {self.balance}")
    elif self == recipient: # Block Transfer to own Account
      print(f"{self.get_time()}"
            f"\nWecome Back, {self.account_holder}!"
            f"\nTransfer Failed;"
            f"\nCannot Transfer to Yourself :)")
    elif transfer_amount <= 0: # Block Transfer Amount <= 0
      print(f"{self.get_time()}"
            "\nInvalid Transfer! Transfer Amount needs to be greater than 0")
    else:
      self.withdraw(transfer_amount, auto_message = False)
      recipient.deposit(transfer_amount, auto_message = False)
      print(f"{self.get_time()}"
            f"\nWecome Back, {self.account_holder}!"
            f"\nTransfer Completed."
            f"\nTransferred {transfer_amount} FROM [{self.account_holder}] TO [{recipient.account_holder}]."
            f"\nYour Remaining Balance: {self.balance}")