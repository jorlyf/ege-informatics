len_id = 19
symbols_count_id = 15
# =>
symbols_bit_id = 4
id_bit = len_id * symbols_bit_id
id_byte = id_bit // 8 + 1 # 10
object = 36 + id_byte
print(8192 * object / 1024)