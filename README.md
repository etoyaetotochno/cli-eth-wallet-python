# cli-eth-wallet-python

Встановлення: <br>
``pip install -r requirements.txt`` - встановлення залежностей <br>

Використання: <br>
``python menu.py`` - виклик функцій через інтерфейс меню

``python main.py COMMAND [ARGS]`` - виклик функцій як команд терміналу <br>
  Команди: <br>
  create-account --username --password - додання нового акаунту, або нового рахунку до існуючого акаунту <br>
  load-account --username --password --key - завантаження існуючого в мережі рахунку до акаунту <br>
  send-transaction --username --password --sender_address --to_address --value - відправлення транзакції <br>
  view-balance --username --password - баланс доступних рахунків в акаунті <br>
