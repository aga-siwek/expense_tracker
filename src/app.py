import sys
import datetime
import json_connection as db_connection


def commend_manage():
    currently_date = str(datetime.date.today())

    if len(sys.argv) > 1:

        if sys.argv[1] == "add":
            if len(sys.argv) == 4:
                description = sys.argv[2]
                cash_expense = int(sys.argv[3])
                db_connection.add_expense(currently_date, description, cash_expense)
            else:
                print("You can use: "
                      "\n ADD: python app.py add 'expense description'")

        elif sys.argv[1] == "update":
            if len(sys.argv) == 4:
                expense_id = sys.argv[2]
                updated_cash_expense = int(sys.argv[3])
                db_connection.update_expense(expense_id, updated_cash_expense)
            else:
                print("You can use: "
                      "\n UPDATE: python app.py update 'expense id' 'update expense'")

        elif sys.argv[1] == "list":
            if len(sys.argv) == 2:
                expense_description = "all"
                db_connection.list_expense(expense_description)
            elif len(sys.argv) == 3:
                expense_description = sys.argv[2]
                db_connection.list_expense(expense_description)
            else:
                print("You can use:"
                      "\n LIST: python app.py list for all or python app.py list 'description'")

        elif sys.argv[1] == "summary":
            if len(sys.argv) == 2:
                expense_month = "all"
                db_connection.summary_expense(expense_month)

            elif len(sys.argv) == 3:
                expense_month = sys.argv[2]
                db_connection.summary_expense(expense_month)
            else:
                print("You can use a few commends: "
                      "\n SUMMARY: python app.py summary for all or python app.py summary 1-12 for chosen month")

        elif sys.argv[1] == "delete":
            if len(sys.argv) == 3:
                expense_id = sys.argv[2]
                db_connection.delete_expense(expense_id)
            else:
                print("You can use:"
                      "\n DELETE: python app.py delete 'expense id'")
        else:
            print("commend not found"
                  "\n You can use a few commends: "
                  "\n ADD: python app.py add 'expense description'"
                  "\n UPDATE: python app.py update 'expense id' 'update expense'"
                  "\n LIST: python app.py list for all or python expense.py list 'description'"
                  "\n SUMMARY: python app.py summary for all or python app.py summary 1-12 for chosen month"
                  "\n DELETE: python app.py delete 'expense id'")

    else:
        print("Add comment."
              "\n You can use a few commends: "
              "\n ADD: python app.py add 'expense description'"
              "\n UPDATE: python app.py update 'expense id' 'update expense'"
              "\n LIST: python app.py list for all or python app.py list 'description'"
              "\n SUMMARY: python app.py summary for all or python app.py summary 1-12 for chosen month"
              "\n DELETE: python app.py delete 'expense id'")


if __name__ == "__main__":
    commend_manage()
