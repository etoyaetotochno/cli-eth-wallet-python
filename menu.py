import os
import click
from cli import create_account, view_balance, send_transaction, load_account

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while True:
        choice = main_menu()
        handle_choice(choice)

def main_menu():
    click.echo("1. Створити новий обліковий запис")
    click.echo("2. Переглянути баланс")
    click.echo("3. Відправити транзакцію")
    click.echo("4. Імпортувати рахунок")
    click.echo("0. Вихід")
    choice = click.prompt('Обрати', type=int)
    return choice

def handle_choice(choice):
    if choice == 1:
        create_account()
    elif choice == 2:
        view_balance()
    elif choice == 3:
        send_transaction()
    elif choice == 4:
        load_account()
    if choice == 0:
        quit()
    else:
        print("Неправильний номер меню.")
    input("Натисніть Enter для продовження...")
    clear_screen()

if __name__ == '__main__':
    menu()