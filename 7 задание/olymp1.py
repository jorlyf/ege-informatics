# Музыкальный фрагмент был оцифрован и записан в виде файла без использования сжатия данных.
# Получившийся файл был передан в город А по каналу связи за 96 секунд.
# Затем тот же музыкальный фрагмент был оцифрован повторно
# с разрешением в 4 раза выше и частотой дискретизации в 3 раза ниже
# чем в первый раз. Сжатие данных не производилось.
# Полученный файл был передан в город Б за 16 секунд.
# Во сколько раз скорость пропускная способность канала в город Б больше пропускной способности канала в город А?

t_в_город_А = 96
# V = длина * частота * разрешение
t_в_город_В = 16

V1 = 100
V2 = V1 * 4 / 3

u1 = V1 / t_в_город_А
u2 = V2 / t_в_город_В

print(u1, u2)

# скорость В / скорость А
print(u2 / u1)