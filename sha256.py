# 1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad
# 3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b
# 74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f
import hashlib
import itertools
from multiprocessing import Process

MY_ALPHABET = "qwertyuiopasdfghjklzxcvbnm"


def bruteForce(first_bits, hash):
    for let in itertools.product(first_bits, MY_ALPHABET, MY_ALPHABET, MY_ALPHABET, MY_ALPHABET):
        # print(let)
        password_try = ''.join(let)
        if hashlib.sha256(password_try.encode()).hexdigest() == hash:
            print("Brute-force result: ", password_try)


def multiThread(hash, countThread):
    part_size = len(MY_ALPHABET) // countThread
    threads = []
    for thread in range(countThread):
        if thread == countThread - 1:
            first_bit = MY_ALPHABET[part_size * thread:]
            print("-1  ", first_bit)
        else:
            first_bit = MY_ALPHABET[part_size *
                                    thread: part_size * (thread + 1)]
            print(first_bit)
        p = Process(target=bruteForce, args=(first_bit, hash))
        threads.append(p)
        p.start()
    for p in threads:
        p.join()


if __name__ == '__main__':
    countThread = 4
    input_hash = input("Введите HASH > ")
    input_thread = int(
        input("Выберите режим\n1 - Однопоточный\n2 - Многопоточный\n"))
    if input_thread == 1:
        countThread = 1
    elif input_thread == 2:
        countThread = int(input("Введите количество потоков > "))
    print("Hash: ", input_hash)
    print("count Threads: ", countThread)
    print("Brute-forcing...")
    multiThread(input_hash, countThread)
