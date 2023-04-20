import pandas as pd

columns=['Date', 'Name', 'Surname']

data = [
['06-29', 'Oleg', 'Gnedov'],
['10-10', 'Egor', 'Celousov'],
['10-19', 'Nariman', 'Nebiev']
]

df = pd.DataFrame(data, columns=columns)
df.to_csv(r'C:/Users/GnedovOO/PycharmProjects/tgbot/birthdays.csv')