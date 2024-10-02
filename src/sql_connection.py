import os
import sqlite3
from pathlib import Path
import json

def create_data_base():
    expense_manage_dir = Path.cwd() / Path("db")
    if not Path.exists(expense_manage_dir):
        os.mkdir("db")

    expense_manage_file = Path.cwd() / Path("db/data.db")
    if not Path.exists(expense_manage_file):
        with open(expense_manage_file, "w") as file:
            json.dump({}, file)


# def id_creator():
#     with open("db/data.db", "r+") as file:
#         json_data = json.load(file)
#     if bool(json_data):
#         max_id = int(max(json_data.keys()))
#         return str(max_id + 1)
#     else:
#         return "0"


def add_expense(currently_data, description, cash_expense):
    # create_data_base()
    con = sqlite3.Connection("db/data.db")
    con.cursor()




    # with open("db/data.db", "r+") as file:
    #     json_data = json.load(file)
    #
    #     expense_id = id_creator()
    #
    #     expense_info = {
    #         str(expense_id): {"currently_date": currently_data, "description": description, "expense": cash_expense,
    #                           "id": expense_id}}
    #     json_data.update(expense_info)
    #     file.seek(0)
    #     json.dump(json_data, file, indent=4)


def update_expense(expense_id, updated_cash_expense):
    create_data_base()
    with open("db/data.db", "r+") as file:
        json_data = json.load(file)

        for key, value in json_data.items():
            if key == expense_id:
                json_data[expense_id]["expense"] = updated_cash_expense
                file.seek(0)
                json.dump(json_data, file, indent=4)
                return print(f"{expense_id} was updated")

        return print("We dont have expense with this id")


def list_expense(expense_description):
    create_data_base()
    sum_of_expense = 0
    with open("db/data.db", "r+") as file:
        json_data = json.load(file)
        if expense_description == "all":
            for key, value in json_data.items():
                print(f"{value['id']}. {value['description']}: {str(value['expense'])} PLN")
                sum_of_expense += value['expense']
            print(f"__________ \n TOTAL EXPENSES: {sum_of_expense} PLN")

        else:
            for key, value in json_data.items():
                if value['description'] == expense_description:
                    print(f"{value['id']}. {value['description']}: {str(value['expense'])} PLN")
                    sum_of_expense += value['expense']
            print(f"__________ \n TOTAL EXPENSES: {sum_of_expense} PLN")


def summary_expense(expense_month):
    create_data_base()
    sum_of_expense = 0
    with open("db/data.db", "r+") as file:
        json_data = json.load(file)

        if expense_month == "all":
            for key, value in json_data.items():
                sum_of_expense += value['expense']
            print(f"__________ \n TOTAL EXPENSES: {sum_of_expense} PLN")

        elif int(expense_month) >= 1 and int(expense_month) <= 9:
            for key, value in json_data.items():
                search_month = f"-0{expense_month}-"
                if search_month in value["currently_date"]:
                    sum_of_expense += value['expense']
            print(f"__________ \n TOTAL EXPENSES: {sum_of_expense} PLN")

        elif int(expense_month) >= 10 and int(expense_month) <= 12:
            for key, value in json_data.items():
                search_month = f"-{expense_month}-"
                if search_month in value["currently_date"]:
                    sum_of_expense += value['expense']
            print(f"__________ \n TOTAL EXPENSES: {sum_of_expense} PLN")


def delete_expense(expense_id):
    create_data_base()
    with open("db/data.db", "r") as file:
        json_data = json.load(file)

        del json_data[expense_id]
        with open("db/data.db", "w") as file:
            file.seek(0)
            json.dump(json_data, file, indent=4)