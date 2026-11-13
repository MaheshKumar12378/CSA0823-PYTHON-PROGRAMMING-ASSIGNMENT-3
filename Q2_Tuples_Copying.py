import copy, sys, time
rows,cols=3,4
bad=[[0]*cols]*rows
bad[0][1]=7
good=[[0 for _ in range(cols)] for _ in range(rows)]
good[0][1]=7
print("bad :",bad)
print("good:",good)
print(bad[0] is bad[1],good[0] is good[1])
stops={(13.0827,80.2707):"Chennai Central",(13.0418,80.2341):"T. Nagar"}
print(stops[(13.0418,80.2341)])
try: stops[[13.0418,80.2341]]="Invalid"
except TypeError as e: print("List key error:",e)
original=[[1,2],[3,4]]
alias=original; shallow=copy.copy(original); sliced=original[:]; deep=copy.deepcopy(original)
original[0][0]=99
print("Alias:",alias,"Shallow:",shallow,"Slice:",sliced,"Deep:",deep)
tuple_data=("Stop A",[10,20]); tuple_data[1].append(30); print(tuple_data)
a=list(range(1000000)); b=tuple(a)
print("List size:",sys.getsizeof(a),"Tuple size:",sys.getsizeof(b))
for name, maker in (("list",list),("tuple",tuple)):
    t=time.perf_counter(); obj=maker(range(1000000)); create=time.perf_counter()-t
    t=time.perf_counter(); obj[500000]; access=time.perf_counter()-t
    print(name,"creation",create,"index",access)
