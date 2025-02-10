from personal_account import PersonalAccount


def test_account():
    account = PersonalAccount(account_number=123456, account_holder="Madina")

    account.deposit(500)
    print(account)

    account.withdraw(200)
    print(account)

    account.withdraw(400)
    print(account)

    print(f"Current balance: {account.get_balance()}")

    account.print_transaction_history()


if __name__ == "__main__":
    test_account()
