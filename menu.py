import os
import click
from cli import create_account, view_balance, send_transaction, load_account

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


if __name__ == '__main__':
    menu()