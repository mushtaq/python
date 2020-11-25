import requests
from account import Account

class CheckingAccount:
    def __init__(self, name: str, balance: int):
        self.name = name
        self.balance = balance

    def deposit(self, amount: int, date: str):
        self.balance += amount

def main():
    names = ['Sarah', 'David', 'Jessica']
    for name in names:
        account = CheckingAccount(name, 1000)
