cities = open("russian_cities.txt", "r", encoding="utf-8").read().split(", ")
cities = [city.strip() for city in cities if city.strip()]


def play_cities():
  used cities = set()
  availble_cities = [city.lower() for city in cities]
  last_letter = None
  While True:
    user_city = input('ваш город: ').strip().lower()
    if user_city == 'стоп':
      print('игра окончена')
      break
    if user_city in used_cities:
      print('этот город уже назван')
      break
    if user_city.title() not in cities:
      print(f'город должен начинаться на букву {last_letter}')
      break
