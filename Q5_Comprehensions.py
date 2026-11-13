import random, sys, time
def loop(a):
    c=[]; f=[]
    for x in a:
        if -50<=x<=50: c.append(x); f.append(x*9/5+32)
    alarms=[i for i,x in enumerate(a) if x<2 or x>8]
    return c,f,alarms
def comprehension(a):
    c=[x for x in a if -50<=x<=50]
    f=[x*9/5+32 for x in a if -50<=x<=50]
    alarms=[i for i,x in enumerate(a) if x<2 or x>8]
    return c,f,alarms
def map_filter(a):
    c=list(filter(lambda x:-50<=x<=50,a))
    f=list(map(lambda x:x*9/5+32,c))
    alarms=list(map(lambda p:p[0],filter(lambda p:p[1]<2 or p[1]>8,enumerate(a))))
    return c,f,alarms
sample=[4,9,3,55,-60,7,1]
print("Loop:",loop(sample)); print("Comprehension:",comprehension(sample)); print("Map/filter:",map_filter(sample))
print("All valid:",comprehension([4,5,6])); print("All invalid:",comprehension([80,-90]))
print("List size:",sys.getsizeof([x for x in sample]),"Generator size:",sys.getsizeof((x for x in sample)))
for n in (10000,100000,1000000):
    a=[random.uniform(-60,60) for _ in range(n)]; times=[]; results=[]
    for fn in (loop,comprehension,map_filter):
        t=time.perf_counter(); results.append(fn(a)); times.append(time.perf_counter()-t)
    print(n,"loop",times[0],"comprehension",times[1],"map/filter",times[2],"same",results[0]==results[1]==results[2])
