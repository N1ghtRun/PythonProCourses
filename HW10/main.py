import time
import threading
import multiprocessing


with open("text.txt", "r") as f:
    text = f.read()


def writing_file():
    start_time = time.time()
    with open("1.txt", "w") as f:
        f.write(text)
    end_time = time.time()
    result_time = end_time-start_time
    print(f"function 1: {result_time}")


def writing_file2():
    start_time = time.time()
    with open("2.txt", "w") as f:
        f.write(text)
    end_time = time.time()
    result_time = end_time-start_time
    print(f"function 2: {result_time}")


def writing_file3():
    start_time = time.time()
    with open("3.txt", "w") as f:
        f.write(text)
    end_time = time.time()
    result_time = end_time-start_time
    print(f"function 3: {result_time}")


def writing_file4():
    start_time = time.time()
    with open("4.txt", "w") as f:
        f.write(text)
    end_time = time.time()
    result_time = end_time-start_time
    print(f"function 4: {result_time}")


# several processes
if __name__ == "__main__":

    # 1 thread 1 process
    print("\n" + "\033[1m" + "1 thread 1 process" + "\033[0m")
    writing_file()

    # 4 threads
    print("\n" + "\033[1m" + "4 threads" + "\033[0m")
    t1 = threading.Thread(target=writing_file)
    t2 = threading.Thread(target=writing_file2)
    t3 = threading.Thread(target=writing_file3)
    t4 = threading.Thread(target=writing_file4)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    # 4 threads
    print("\n" + "\033[1m" + "4 processes" + "\033[0m")
    p1 = multiprocessing.Process(target=writing_file)
    p2 = multiprocessing.Process(target=writing_file2)
    p3 = multiprocessing.Process(target=writing_file3)
    p4 = multiprocessing.Process(target=writing_file4)

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
