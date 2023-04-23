import pandas as pd


columns=['Date', 'Name', 'Surname']

data = [
['06-29', 'Oleg', 'Gnedov'],
['10-10', 'Egor', 'Celousov'],
['10-19', 'Nariman', 'Nebiev'],
['04-26','Test','User5'],
['04-25','Test','User4'],
['04-24','Test','User3'],
['04-23','Test','User2'],
['04-22','Test','User1'],
['04-26','Test','User55'],
['04-23','Test','User444']
]

df = pd.DataFrame(data, columns=columns)
df.to_csv(r'C:/Users/GnedovOO/PycharmProjects/tgbot/birthdays.csv')