import click
import cli
import db
import menu

@click.group()
def main():
	db.create_table()

# додання команди з cli.py
main.add_command(cli.create_account)
main.add_command(cli.load_account)
main.add_command(cli.send_transaction)
main.add_command(cli.view_balance)

if __name__ == '__main__':
    main()
