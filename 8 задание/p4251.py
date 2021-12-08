# Маша составляет 6-буквенные слова из букв З, Е, Р, К, А, Л, О,
# содержащие букву К, но не более 4 раз. Остальные буквы не могут повторяться.
# Сколько различных слов может составить Маша?

import itertools

words = list(itertools.product("ЗЕРКАЛО", repeat=6))
forbiddens = ["З", "Е", "Р", "А", "Л", "О"]
count = 0
for word in words:
  word = "".join(word)
  if word.count("К") > 0 and word.count("К") <= 4:
    for s in forbiddens:
      if word.count(s) > 1:
        break

    else:
      count += 1

print(count)