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
        if click.confirm("Обліковий запис {} існує.\n Підтвердити створення нової адреси?".format(username)):
            account = eth.create_account()
            db.add_user(username, password, account["address"], account["private_key"])
            click.echo("Рахунок додано до користувача: {}\nАдреса рахунку: {}".format(username, account["address"]))
        else:
            return

@click.command()
@click.option("--username", prompt=True, help="Ім'я користувача для нового облікового запису")
@click.option("--password", prompt=True, hide_input=True, confirmation_prompt=True, help="Пароль для нового облікового запису")
@click.option("--key", prompt=True, help="Приватний ключ існуючого рахунку в мережі")
def load_account(username, password, key):
    if db.user_unique(username):
        db.add_user(username, password, account["address"], account["private_key"])
        click.echo("Рахунок імпортовано до нового облікового запису:\nІм'я користувача: {}\nАдреса рахунку: {}".format(username, account["address"]))
    else:
        user = db.authenticate(username, password)
        if not user:
            click.echo("Неправильне ім'я або пароль")
            return
        else:
            account = eth.load_account(key)
            db.add_user(username, password, account["address"], account["private_key"])
            click.echo("Рахунок імпортовано до існуючого облікового запису:\nІм'я користувача: {}\nАдреса рахунку: {}".format(username, account["address"]))

@click.command()
@click.option("--username", prompt=True, help="Ім'я користувача існуючого облікового запису")
@click.option("--password", prompt=True, hide_input=True, help="Пароль існуючого облікового запису")
@click.option("--sender_address", prompt=False, default=None, help="Адреса відправника")
@click.option("--to_address", prompt=True, help="Адреса призначення")
@click.option("--value", prompt=True, type=float, help="Сума (ефіру) транзакції")
def send_transaction(username, password, sender_address, to_address, value):
    user = db.authenticate(username, password)
    if not user:
        click.echo("Неправильне ім'я або пароль")
        return
    if sender_address:
        private_key = db.get_private_key(sender_address)[0][0]
        tx_hash = eth.send_transaction(private_key, to_address, value)
    else:
        addresses = [row[0] for row in db.user_addresses(username)]
        click.echo("Оберіть вихідний рахунок:")

        for i, address in enumerate(addresses):
            click.echo("{}. {}".format(i+1, address))

        while True:
            try:
                choice = click.prompt("Введіть номер рахунку", type=int)
                if choice < 1 or choice > len(addresses):
                    raise ValueError("Неправильний номер рахунку. Спробуйте ще раз.")
                else:
                    selected_address = addresses[choice-1]
                    break
            except ValueError as e:
                click.echo(str(e))

        private_key = db.get_private_key(selected_address)[0][0]
        tx_hash = eth.send_transaction(private_key, to_address, value)
    click.echo("Транзакцію відправлено: {}\n Рахунок: {}\n Сума: {}".format(tx_hash, selected_address, value))

@click.command()
@click.option("--username", prompt=True, help="Ім'я користувача існуючого облікового запису")
@click.option("--password", prompt=True, hide_input=True, help="Пароль існуючого облікового запису")
def view_balance(username, password):
    user = db.authenticate(username, password)
    if not user:
        click.echo("Неправильне ім'я або пароль")
        return
    addresses = [row[0] for row in db.user_addresses(username)]
    click.echo("Поточний баланс рахунків")
    for address in addresses:
        balance = eth.get_balance(address)
        click.echo("{} : {} ETH".format(address, balance))

