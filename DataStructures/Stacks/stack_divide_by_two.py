from DataStructures.Stacks.stack import Stack

def div_by_2(dec_num):
    s = Stack()

    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        print(s.items)
        dec_num = dec_num // 2
    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())
    return bin_num

# print(div_by_2(242))


#Listede sola ekleyerek yapılırsa
def in_to_bin(num):
    in_bin = ""
    while num > 0:
        print(in_bin)
        in_bin = str(num%2) + in_bin
        num //= 2
    return int(in_bin)

# print(f"ikinci fonksiyon dan çıktı {in_to_bin(242)}")