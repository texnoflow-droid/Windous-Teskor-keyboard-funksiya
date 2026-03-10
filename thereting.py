
# 1

# import threading
# import multiprocessing
# import math

# def multithreading_tasks():
#     print("MultiThreading (Oqimlar) boshlandi")
#     def f1(s, e): print(f"M1: {list(range(s, e+1))}")
#     threading.Thread(target=f1, args=(1, 50)).start()
#     threading.Thread(target=f1, args=(51, 100)).start()

    
# if __name__ == "__main__":
#     multithreading_tasks()

# import threading
# import multiprocessing
# import math



# 2
# import threading
# import time

# lock = threading.Lock()

# def juft_sonlar():
#     for i in range(1, 101):
#         if i % 2 == 0:
#             with lock:
#                 print(f"Juft son: {i}")
#             time.sleep(2)

# def toq_sonlar():
#     for i in range(1, 101):
#         if i % 2 != 0:
#             with lock:
#                 print(f"Toq son: {i}")
#             time.sleep(2)

# thread1 = threading.Thread(target=juft_sonlar)
# thread2 = threading.Thread(target=toq_sonlar)

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()


# 3

# import threading
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# umumiy_yigindi = 0
# def birinchi_yarim_yigindi():
#     global umumiy_yigindi
#     yigindi = sum(nums[:len(nums)//2])
#     umumiy_yigindi += yigindi
# def ikkinchi_yarim_yigindi():
#     global umumiy_yigindi
#     yigindi = sum(nums[len(nums)//2:])
#     umumiy_yigindi += yigindi
# thread1 = threading.Thread(target=birinchi_yarim_yigindi)
# thread2 = threading.Thread(target=ikkinchi_yarim_yigindi)
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print("Umumiy yig'indisi:", umumiy_yigindi)


# 5
import threading
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in text if char in vowels)
    print(f"Unli harflar soni: {count}")

def count_consonants(text):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in text if char.isalpha() and char not in vowels)
    print(f"Undosh harflar soni: {count}")

if __name__ == "__main__":
    text = "python multithreading"
    thread1 = threading.Thread(target=count_vowels, args=(text,))
    thread2 = threading.Thread(target=count_consonants, args=(text,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Hisoblash yakunlandi.")


import threading

# 6. Listdagi eng katta son
nums6 = [23, 54, 12, 76, 89, 33, 45, 90]
results6 = []

def find_max(sub_list):
    results6.append(max(sub_list))

t1 = threading.Thread(target=find_max, args=(nums6[:4],))
t2 = threading.Thread(target=find_max, args=(nums6[4:],))
t1.start(); t2.start(); t1.join(); t2.join()
print(f"6. Eng katta son: {max(results6)}")

# 7. Kvadratlar hisoblash
nums7 = [1, 2, 3, 4, 5, 6, 7, 8]
res7 = [0] * len(nums7)

def calc_square(start, end):
    for i in range(start, end):
        res7[i] = nums7[i] ** 2

t1 = threading.Thread(target=calc_square, args=(0, 4))
t2 = threading.Thread(target=calc_square, args=(4, 8))
t1.start(); t2.start(); t1.join(); t2.join()
print(f"7. Kvadratlar: {res7}")

# 8. Tub sonlar (1-100)
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def find_primes(start, end):
    primes = [n for n in range(start, end+1) if is_prime(n)]
    print(f"8. Tub sonlar ({start}-{end}): {primes}")

threading.Thread(target=find_primes, args=(1, 50)).start()
threading.Thread(target=find_primes, args=(51, 100)).start()

# 9. Stringlarni katta harfga o'tkazish
words9 = ["python", "django", "fastapi", "backend"]
def to_upper(sub_list):
    print(f"9. Upper: {[w.upper() for w in sub_list]}")

threading.Thread(target=to_upper, args=(words9[:2],)).start()
threading.Thread(target=to_upper, args=(words9[2:],)).start()

# 10. Palindrom tekshirish
words10 = ["level", "python", "radar", "hello"]
def check_palin(sub_list):
    res = {w: (w == w[::-1]) for w in sub_list}
    print(f"10. Palindrom: {res}")

threading.Thread(target=check_palin, args=(words10[:2],)).start()
threading.Thread(target=check_palin, args=(words10[2:],)).start()









import multiprocessing
import math

# 1. 1 dan N gacha yig'indi
def sum_range(start, end, queue):
    queue.put(sum(range(start, end + 1)))

# 2. Faktorial
def calc_fact(n):
    print(f"2. {n}! = {math.factorial(n)}")

# 3. Tub sonlar (1-10000)
def find_primes_mp(start, end):
    primes = [n for n in range(start, end+1) if is_prime(n)]
    print(f"3. Tub sonlar ({start}-{end}) topildi.")

# 4. Fibonacci
def fib(n):
    a, b = 0, 1
    for _ in range(n): a, b = b, a + b
    print(f"4. Fibonacci({n}) = {a}")

# 5. Eng katta son
def find_max_mp(sub_list, queue):
    queue.put(max(sub_list))

if __name__ == "__main__":
    # 1-masala uchun Queue
    q1 = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=sum_range, args=(1, 500000, q1))
    p2 = multiprocessing.Process(target=sum_range, args=(500001, 1000000, q1))
    p1.start(); p2.start(); p1.join(); p2.join()
    print(f"1. Umumiy yig'indi: {q1.get() + q1.get()}")

    # 2-masala
    multiprocessing.Process(target=calc_fact, args=(10,)).start()
    multiprocessing.Process(target=calc_fact, args=(12,)).start()

    # 4-masala
    multiprocessing.Process(target=fib, args=(30,)).start()
    multiprocessing.Process(target=fib, args=(35,)).start()

    # 7. Listni sort qilish (Logic)
    def sort_part(sub_list, queue):
        queue.put(sorted(sub_list))
    
    nums7 = [34, 12, 76, 23, 89, 11, 90, 45]
    q7 = multiprocessing.Queue()
    multiprocessing.Process(target=sort_part, args=(nums7[:4], q7)).start()
    multiprocessing.Process(target=sort_part, args=(nums7[4:], q7)).start()
    # Keyin natijalar merge qilinadi...