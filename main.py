# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from config.settings import Settings
from db.db_manager import DBConn


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("db_url: ", Settings.ENV_NAME)
    print_hi('PyCharm')
    db = DBConn()
    print("db: ", db)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
