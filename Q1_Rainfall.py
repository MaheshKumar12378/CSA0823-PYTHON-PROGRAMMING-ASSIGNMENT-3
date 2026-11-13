import random, time

def naive_avg(a, w=7):
    return [sum(a[i:i+w])/w for i in range(len(a)-w+1)] if len(a)>=w else []

def running_avg(a, w=7):
    if len(a)<w: return []
    s=sum(a[:w]); out=[s/w]
    for i in range(w,len(a)):
        s += a[i]-a[i-w]
        out.append(s/w)
    return out

def analyse(readings):
    if not readings:
        print("No readings"); return
    weeks=[sum(readings[i:i+7]) for i in range(0,len(readings),7)]
    print("Weekly totals:", weeks)
    print("Wettest week:", weeks.index(max(weeks))+1)
    print("Driest week:", weeks.index(min(weeks))+1)
    print("Maximum:", max(readings), "Day:", readings.index(max(readings))+1)
    print("Minimum:", min(readings), "Day:", readings.index(min(readings))+1)
    print("7-day averages:", running_avg(readings))
    print("Dry days:", [i+1 for i,x in enumerate(readings) if x==0])

if __name__=="__main__":
    sample=[0,2,5,0,10,4,3,8,0,1,2,6,7,0]
    analyse(sample)
    for n in (365,36500,365000):
        a=[random.uniform(0,80) for _ in range(n)]
        t=time.perf_counter(); x=naive_avg(a); tn=time.perf_counter()-t
        t=time.perf_counter(); y=running_avg(a); tr=time.perf_counter()-t
        print(n, "naive",tn,"running",tr,"same",x==y)
    print("Empty:",running_avg([]),"Short:",running_avg([1,2,3]))
