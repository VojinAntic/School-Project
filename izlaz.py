import threading
import time

def write_even_numbers(filename):
    with open(filename, 'a') as file:
        for i in range(2, 22, 2):
            semaphore.acquire()
            file.write(str(i) + '\n')
            semaphore.release()
            time.sleep(1)

def  write_odd_numbers(filename):
    with open(filename, 'a') as file:
        for i in range(1, 21, 2):
            semaphore.acquire()
            file.write(str(i) + '\n')
            semaphore.release()
            time.sleep(1)

if __name__ == '__main__':
    semaphore = threading.Semaphore(1)
    filename = 'izlaz.txt'

    t1 = threading.Thread(target=write_even_numbers, args=(filename,))
    t2 = threading.Thread(target=write_odd_numbers, args=(filename,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
