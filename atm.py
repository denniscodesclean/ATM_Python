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
    if balance > 0:
      self.balance = balance
    else:
      self.balance = 0
      print("Invalid Balance! \nBalance needs to be greater than 0.")

  # Timer
  def get_time(self):
    return datetime.now(local_timezone).strftime("%Y-%m-%d %H:%M:%S")

  # Number Validator, reject non-positive numebrs, reject invalid datatype
  def num_validate(self, amount):
    if isinstance(amount, bool):  # Check if the input is a boolean, cuz boolean can be converted to float and pass the check below.
        print(f"{self.get_time()}"
              "\nPlease enter a positive number.")
        return False
    try:
      amount = float(amount)
      if amount <= 0:
        print(f"{self.get_time()}"
              "\nPlease enter a positive number.")
        return False
      else:
        self.validated = amount
        return True
    except (ValueError, NameError):
      print(f"{self.get_time()}"
            "\nPlease Enter a Valid Number, loh!")
      return False

  # define Deposit function
  def deposit(self, amount=0, auto_message = True):
    if self.num_validate(amount):
      self.balance += self.validated
      if auto_message:
        print(f"{self.get_time()}"
              f"\nWecome Back, {self.account_holder}!"
              f"\nDeposit Completed."
              f"\nDeposit: {self.validated}. Here's your Remaining Balance: {self.balance}")

  # define Withdraw function
  def withdraw(self, amount=0, auto_message = True):
    if self.num_validate(amount):
      if self.balance < self.validated:
        print(f"{self.get_time()}"
              f"\nWecome Back, {self.account_holder}!"
              f" \nTrasaction Failed."
              f"\nLow Balance, Remaining Balance: {self.balance}")
      else:
        self.balance -= self.validated
        if auto_message:
          print(f"{self.get_time()}"
                f"\nWecome Back, {self.account_holder}!"
                f"\nWithdraw Completed."
                f"\nWithdraw: {self.validated}. Here's your remaining balance: {self.balance}")

  #define Transfer
  def transfer(self, recipient, transfer_amount):
    if self.num_validate(transfer_amount):
      if self.balance < self.validated: # Insufficient Balance
        print(f"{self.get_time()}"
              f"\nWecome Back, {self.account_holder}!"
              f"\nTransfer Failed;"
              f"\nRemaining Balance: {self.balance}")
      elif self == recipient: # Block Transfer to own Account
        print(f"{self.get_time()}"
              f"\nWecome Back, {self.account_holder}!"
              f"\nTransfer Failed;"
              f"\nCannot Transfer to Yourself :)")
      else:
        self.withdraw(self.validated, auto_message = False)
        recipient.deposit(self.validated, auto_message = False)
        print(f"{self.get_time()}"
              f"\nWecome Back, {self.account_holder}!"
              f"\nTransfer Completed."
              f"\nTransferred {self.validated} FROM [{self.account_holder}] TO [{recipient.account_holder}]."
              f"\nYour Remaining Balance: {self.balance}")