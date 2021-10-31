# Михаил составляет 5-буквенные коды. В кодах разрешается использовать только буквы А, Б, В, Г, Д,
# при этом код не может начинаться с гласной и не может содержать двух одинаковых букв подряд.
# Сколько различных кодов может составить Михаил?

import itertools
words = list(itertools.product("АБВГД", repeat=5))
forbiddens = ["АА", "ББ", "ВВ", "ГГ", "ДД"]

count = 0
for word in words:
  word = "".join(word)
  if (word[0] != "А"):
    for forbidden in forbiddens:
      if (forbidden in word):
        break
    
    else:
      count += 1

print(count)