def bubbleSort(lst):
    needNextPass = True
    
    k = 1
    while k < len(lst) and needNextPass:
        needNextPass = False
        for i in range(len(lst) - k): 
            if lst[i] > lst[i + 1]:
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
          
                needNextPass = True

def main():
    lst = [5,6,8,7,9,1,3,4,2]
    bubbleSort(lst)
    for v in lst:
        print(v, end = " ")
    import time
    start_time = time.time()
    print(" %s seconds" % (time.time() - start_time))
main()