import click
import cli
import db

@click.group()
def main():
	db.create_table()

# додання команди з cli.py
main.add_command(cli.create_account)
main.add_command(cli.load_account)
if __name__ == '__main__':
    main()
