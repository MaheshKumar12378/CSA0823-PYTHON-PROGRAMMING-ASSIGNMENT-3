import time, sys
trains={
"12601":{"name":"Chennai Express","stops":[("Chennai","06:00","06:10"),("Vijayawada","12:00","12:05"),("Howrah","22:00","22:10")],"days":{"Mon","Wed","Fri"}},
"12602":{"name":"Coastal Express","stops":[("Chennai","07:00","07:15"),("Nellore","10:00","10:05"),("Vijayawada","13:00","13:10")],"days":{"Tue","Thu","Sat"}},
"12603":{"name":"Southern Mail","stops":[("Bengaluru","05:00","05:10"),("Chennai","09:00","09:20"),("Vijayawada","15:00","15:05")],"days":{"Mon","Tue","Wed","Thu","Fri","Sat","Sun"}},
"12604":{"name":"Delta Passenger","stops":[("Thanjavur","06:30","06:35"),("Chennai","11:00","11:10"),("Nellore","14:00","14:05")],"days":{"Sun"}},
"12605":{"name":"Eastern Link","stops":[("Chennai","08:00","08:05"),("Vijayawada","14:00","14:10"),("Howrah","23:00","23:05")],"days":{"Mon","Thu","Sat"}}}
def query(data,station,day):
    found=[]
    for no,d in data.items():
        if day in d["days"]:
            for st,arr,dep in d["stops"]:
                if st==station: found.append((dep,no,d["name"],arr))
    return sorted(found,key=lambda x:x[0])
def make_index(data):
    idx={}
    for no,d in data.items():
        for st,arr,dep in d["stops"]: idx.setdefault(st,[]).append((no,arr,dep))
    return idx
def indexed_query(data,idx,station,day):
    out=[]
    for no,arr,dep in idx.get(station,[]):
        if day in data[no]["days"]: out.append((dep,no,data[no]["name"],arr))
    return sorted(out,key=lambda x:x[0])
for no,d in trains.items():
    print(no,d["name"],d["days"])
    for stop in d["stops"]: print(" ",stop)
idx=make_index(trains)
print("Chennai on Mon:",query(trains,"Chennai","Mon"))
print("Indexed:",indexed_query(trains,idx,"Chennai","Mon"))
print("Unknown:",query(trains,"Unknown","Mon"))
for n in (100,1000,10000):
    data={str(i):{"name":f"Train{i}","stops":[(f"Station{j%50}","08:00","08:05") for j in range(10)],"days":{"Mon","Wed"}} for i in range(n)}
    t=time.perf_counter(); query(data,"Station3","Mon"); scan=time.perf_counter()-t
    t=time.perf_counter(); ix=make_index(data); build=time.perf_counter()-t
    t=time.perf_counter(); indexed_query(data,ix,"Station3","Mon"); fast=time.perf_counter()-t
    print(n,"scan",scan,"index-build",build,"indexed query",fast,"index container bytes",sys.getsizeof(ix))
