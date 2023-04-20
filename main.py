import click
import cli
import db

@click.group()
def main():
	db.create_table()

if __name__ == '__main__':
    main()
