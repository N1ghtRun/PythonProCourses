import time
import threading
import multiprocessing


with open("text.txt", "r") as f:
    text = f.read()


def writing_file(num):
    start_time = time.time()
    with open("1.txt", "w") as f:
        f.write(text)
    end_time = time.time()
    result_time = end_time-start_time
    print(f"function {num}: {result_time}")


if __name__ == "__main__":

    # 1 thread 1 process
    print("\n" + "\033[1m" + "1 thread 1 process" + "\033[0m")
    writing_file(1)

    # 4 threads
    print("\n" + "\033[1m" + "4 threads" + "\033[0m")
    t1 = threading.Thread(target=writing_file, args=(1,))
    t2 = threading.Thread(target=writing_file, args=(2,))
    t3 = threading.Thread(target=writing_file, args=(3,))
    t4 = threading.Thread(target=writing_file, args=(4,))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    print('\nIn this case GIL (Global Interpreter Lock) is used. Python performs one thread at the time, therefore '
          'true parallelism is not achieved, execution takes extra time.')


    # 4 processes
    print("\n" + "\033[1m" + "4 processes" + "\033[0m")
    p1 = multiprocessing.Process(target=writing_file, args=(1,))
    p2 = multiprocessing.Process(target=writing_file, args=(2,))
    p3 = multiprocessing.Process(target=writing_file, args=(3,))
    p4 = multiprocessing.Process(target=writing_file, args=(4,))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    print('\n In this case we use multiple processes instead of using several threads within single process. '
          'Each process has it\'s own memory space and interpreter, each process running on it\'s own core. In this'
          ' case each thread executed within it\'s own process, therefore there is no need for executing only one'
          'thread at the time.')
