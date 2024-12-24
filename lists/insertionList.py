def insertionList(lst):
    for i in range(1, len(lst)):
        current = lst[i]
        k = i - 1
        while k >= 0 and lst[k] > current:
            lst[k + 1] = lst[k]
            k -= 1
        lst[k+1] = current

def main():
    lst = [5,6,8,7,9,1,3,4,2]
    insertionList(lst)
    for v in lst:
        print(v, end = " ")
    import time
    start_time = time.time()
    print(" %s seconds" % (time.time() - start_time))
main()