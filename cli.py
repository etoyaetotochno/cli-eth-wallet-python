import click
import db
import eth
import auth

cli = click.Group()

@click.command()
@click.option("--username", prompt=True, help="Ім'я користувача для нового облікового запису")
@click.option("--password", prompt=True, hide_input=True, confirmation_prompt=True, help="Пароль для нового облікового запису")
def create_account(username, password):
    if db.user_unique(username):
        account = eth.create_account()
        db.add_user(username, password, account["address"], account["private_key"])
        click.echo("Обліковий запис створено:\nІм'я користувача: {}\nАдреса рахунку: {}".format(username, account["address"]))
    else:
        click.echo("Помилка! Обліковий запис {} вже існує.".format(username))

@click.command()
@click.option("--username", prompt=True, help="Ім'я користувача для нового облікового запису")
@click.option("--password", prompt=True, hide_input=True, confirmation_prompt=True, help="Пароль для нового облікового запису")
@click.option("--key", prompt=True, help="Приватний ключ існуючого рахунку в мережі")
def load_account(username, password, key):
    account = eth.load_account(key)
    db.add_user(username, password, account["address"], account["private_key"])
    click.echo("Рахунок імпортовано:\nІм'я користувача: {}\nАдреса рахунку: {}".format(username, account["address"]))

@click.command()
@click.option("--username", prompt=True, help="Ім'я користувача існуючого облікового запису")
@click.option("--password", prompt=True, hide_input=True, help="Пароль існуючого облікового запису")
@click.option("--to", prompt=True, help="Адреса призначення")
@click.option("--value", prompt=True, type=float, help="Сума (ефіру) транзакції")
def send_transaction(username, password, to, value):
    user = auth.authenticate(username, password)
    if not user:
        click.echo("Неправильне ім'я або пароль")
        return
    tx_hash = eth.send_transaction(user["private_key"], to, value)
    click.echo("Транзакцію відправлено: {}".format(tx_hash))

@click.command()
@click.option("--username", prompt=True, help="Ім'я користувача існуючого облікового запису")
@click.option("--password", prompt=True, hide_input=True, help="Пароль існуючого облікового запису")
def view_balance(username, password):
    user = auth.authenticate(username, password)
    if not user:
        click.echo("Неправильне ім'я або пароль")
        return
    balance = eth.get_balance(user["address"])
    click.echo("Поточний баланс {}: {} ETH".format(user["address"], balance))

