# python3
# Linards Tomass Beķeris 221RDB161

def parallel_processing(n, m, data):

    output = []

    pabeigsanas_laiki = [0] * n
    threads_drb = [[] for _ in range(n)]

    # for cikls
    for i in range(m):
        min_laiks = min(pabeigsanas_laiki)
        min_thread = pabeigsanas_laiki.index(min_laiks)
        threads_drb[min_thread].append(i)
        starta_laiks = pabeigsanas_laiki[min_thread]
        pabeigsanas_laiki[min_thread] += data[i]
        output.append((min_thread, starta_laiks))
    return output


def main():
    
    # pieprasa n un m vertibas aka thread count un job count
    n, m = map(int, input("Ievadi thread count un job count: ").split())

    # pieprasa ievadit datus (2 linija)
    data = list(map(int, input("Ievadi datus: ").split()))

    # izsauc funkciju un printe rezultatu
    result = parallel_processing(n, m, data)
    for thread, starta_laiks in result:
        print(thread, starta_laiks)


if __name__ == "__main__":
    main()