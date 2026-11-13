import time
ai={"192311001","192311004","192311007","192311009"}
iot={"192311002","192311004","192311009","192311010"}
all_students={f"1923110{i:02d}" for i in range(1,11)}
both=ai & iot
exactly_one=ai ^ iot
neither=all_students-(ai|iot)
print("clash :",sorted(both))
print("exactly one:",sorted(exactly_one))
print("neither :",sorted(neither))
print("Methods match:",both==ai.intersection(iot) and exactly_one==ai.symmetric_difference(iot) and neither==all_students.difference(ai.union(iot)))
print("Empty:",set()&set(),"Identical symmetric difference:",ai^ai)
for n in (10000,100000,1000000):
    values=[str(i) for i in range(n)]; s=set(values); target=str(n-1)
    t=time.perf_counter(); _=target in values; tl=time.perf_counter()-t
    t=time.perf_counter(); _=target in s; ts=time.perf_counter()-t
    print(n,"list membership",tl,"set membership",ts)
