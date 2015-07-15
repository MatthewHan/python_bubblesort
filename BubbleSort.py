__author__ = 'MatthewHan'
import random
import time

def bubble_sort(list):
    start = time.time()
    #Set swapped to true to start the loop
    swapped = True
    while swapped:
        #Set swapped to False at the start of every loop
        swapped = False
        for i in range(len(list)-1):
            if list[i]>list[i+1]:
                #tuple swap accomplishes same result as using a temp variable in other languages to swap two values
                list[i],list[i+1] = list[i+1],list[i]
                #if an item has been swapped set swapped to true and restart the loop until no values are swapped
                swapped = True
    end = time.time()
    elapsed = end - start
    print 'This sort took', elapsed,'seconds'
    return list

def test_sort(testamt):
    my_rand = [None]*testamt
    my_sort = [None]*testamt
    for i in range(testamt):
        randnum = random.randint(50,1000)
        randlen = random.randint(1,25)
        my_rand[i] = random.sample(xrange(randnum),randlen)
        print 'Unsorted myrand'+str(i), my_rand[i]
        my_sort[i] = bubble_sort(my_rand[i])
        print 'Sorted mysort'+str(i), my_sort[i]
test_sort(2)



