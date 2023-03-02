import multiprocessing


with open("data.txt", "r") as f:
    tickets = f.read().split()


def three_digits_sum(start, end, result_queue):
    counter = 0
    for i in tickets[start:end]:
        if sum([int(j) for j in i[:3]]) == sum([int(j) for j in i[3:]]):
            counter += 1

    result_queue.put(counter)


if __name__ == "__main__":

    mid = int(len(tickets)/2)
    end = len(tickets)

    result_queue = multiprocessing.Queue()
    result_queue2 = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=three_digits_sum, args=(0, mid, result_queue))
    p2 = multiprocessing.Process(target=three_digits_sum, args=(mid, end, result_queue2))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    tickets_sum = result_queue.get() + result_queue2.get()
    print("Number of lucky tickets: ", tickets_sum)
