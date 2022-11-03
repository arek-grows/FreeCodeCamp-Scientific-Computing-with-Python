from __future__ import annotations


class Category:
    """A class that represents a financial account of a specific spending category aka category account"""
    def __init__(self, budget_type: str):
        """Initializes the object's attributes

        :param budget_type: a string specifying the category of the account
        """
        # balance: the balance of the category account
        # ledger: a list of strings that describe the deposits, withdrawals, and transfers of the category
        # total_withdrawn: tracks how much has been withdrawn from the category
        self.budget_type = budget_type.title()
        self.balance = 0
        self.ledger = []
        self.total_withdrawn = 0

    def check_funds(self, amount: int):
        """Returns whether or not the category account balance is greater or equal to the amount param"""
        return amount <= self.balance

    def deposit(self, amount: int, description=''):
        """Deposits an amount into the category account and adds a description of the deposit to the ledger

        :param amount: how much money to deposit
        :param description: the description of the deposit
        """
        self.balance += amount
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount: int, description=''):
        """Withdraws an amount out of the category account and adds a description of the withdrawal to the ledger

        :param amount: how much money to withdraw
        :param description: the description of the withdrawal"""
        if self.check_funds(amount):
            self.total_withdrawn += amount
            amount *= -1
            self.balance += amount
            self.ledger.append({"amount": amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        """Returns the category account balance"""
        return self.balance

    def transfer(self, amount: int, budget_obj: Category):
        """Transfers an amount of money from this Category object to another category object and appends the
        description of the transfer to each object's ledger

        :param amount: the amount to transfer
        :param budget_obj: the object the money should be transferred to
        :return: True if the transfer succeeded, False otherwise
        """
        if self.withdraw(amount, f"Transfer to {budget_obj.budget_type}"):
            budget_obj.deposit(amount, f"Transfer from {self.budget_type}")
            return True
        else:
            return False

    def __str__(self):
        """Returns a specially formatted string of the object's ledger when print() is called on the object"""
        bstr_len = len(self.budget_type)
        asts = 30 - bstr_len
        remove_asts = bstr_len % 2
        return_string = ''
        return_string += f"{'*' * (asts // 2)}{self.budget_type}{'*' * ((asts // 2) + remove_asts)}\n"
        for ll in self.ledger:
            new_desc = ll["description"]
            if len(new_desc) > 23:
                new_desc = new_desc[:23]
            else:
                new_desc += " " * (23 - len(new_desc))
            new_amo = '{:.2f}'.format(ll["amount"])
            new_amo = str(new_amo)
            if len(new_amo) > 7:
                new_amo = new_amo[:7]
            else:
                new_amo = f"{' ' * (7 - len(new_amo))}{new_amo}"
            return_string += new_desc + new_amo + "\n"
        return_string += f"Total: {round(self.balance, 2)}"
        return return_string


def create_spend_chart(categories):
    """Returns a string of a bar chart that shows percentage spent by category, based on multiple
    Category objects (x axis) and the amount of money they've spent (y axis)

    :type categories: list[Category]
    """
    string_percent_list = []
    for ii in range(100, -1, -10):
        ii = str(ii)
        string_percent_list.append(f"{' ' * (3 - len(ii))}{ii}| ")

    total_spent = 0
    for cc in categories:
        total_spent += cc.total_withdrawn
    dis_list = []
    for cc in categories:
        dis_list.append(round(cc.total_withdrawn / total_spent * 100))

    for ii, rr in enumerate(range(100, -1, -10)):
        for dd in dis_list:
            if dd >= rr:
                string_percent_list[ii] += "o  "
            else:
                string_percent_list[ii] += "   "
        string_percent_list[ii] += "\n"

    end_string = 'Percentage spent by category\n'
    for ss in string_percent_list:
        end_string += ss
    end_string += f"    {'---' * len(categories)}-\n"

    x_labels = []
    largest_str_len = 0
    for cc in categories:
        if len(cc.budget_type) > largest_str_len:
            largest_str_len = len(cc.budget_type)
    for cc in categories:
        x_labels.append(f'{cc.budget_type}{" " * (largest_str_len - len(cc.budget_type))}')
    for ii in range(0, largest_str_len):
        end_string += "    "
        for xx in x_labels:
            end_string += f" {xx[ii]} "
        if ii != largest_str_len - 1:
            end_string += " \n"
        else:
            end_string += " "

    return end_string


# me = Category("Fordd")
# me.deposit(932, "deposit")
# me.withdraw(78.82, "withdraw")
# me.deposit(2, "new deposit")
#
#
#
# food = Category("Food")
# food.deposit(900, "deposit")
# food.transfer(80, me)
# food.withdraw(34, "test")
#
#
#
# print(create_spend_chart([me, food]))
