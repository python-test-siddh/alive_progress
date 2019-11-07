from alive_progress import alive_bar
items = range(1000)                  # retrieve your set of items
with alive_bar(len(items)) as bar:   # declare your expected total
    for item in items:               # iterate as usual
        # process each item
        bar() 

        
import time
with alive_bar(1000) as bar:
    for i in range(1000):
        if i%100==0:
            print('100')
        time.sleep(0.01)
        bar()
