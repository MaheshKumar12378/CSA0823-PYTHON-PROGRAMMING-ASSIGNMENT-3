import time
def norm_phone(p):
    d="".join(ch for ch in str(p) if ch.isdigit())
    if len(d)==12 and d.startswith("91"): d=d[2:]
    return d
def norm_name(n): return " ".join(str(n or "").lower().split())
def merge(sources):
    by_phone={}
    no_phone=[]
    for source in sources:
        for c in source:
            name=str(c.get("name") or "").strip()
            email=str(c.get("email") or "").strip().lower()
            numbers={norm_phone(p) for p in (c.get("phones") or [])}
            numbers={p for p in numbers if len(p)==10}
            if not numbers:
                no_phone.append({"names":{name} if name else set(),"phones":set(),"emails":{email} if email else set()})
                continue
            existing={id(by_phone[p]):by_phone[p] for p in numbers if p in by_phone}
            if existing:
                target=next(iter(existing.values()))
                for other in existing.values():
                    if other is not target:
                        target["names"].update(other["names"]); target["phones"].update(other["phones"]); target["emails"].update(other["emails"])
                target["names"].update({name} if name else set()); target["phones"].update(numbers); target["emails"].update({email} if email else set())
            else:
                target={"names":{name} if name else set(),"phones":set(numbers),"emails":{email} if email else set()}
            for p in numbers: by_phone[p]=target
    unique=[]; seen=set()
    for value in list(by_phone.values())+no_phone:
        if id(value) not in seen:
            seen.add(id(value)); unique.append({"names":sorted(value["names"]),"phones":sorted(value["phones"]),"emails":sorted(value["emails"])})
    return unique
a=[{"name":"Dr. Ravi","phones":["+91 98400 12345"],"email":"RAVI@example.com"},{"name":"Anu","phones":["9876543210"],"email":""}]
b=[{"name":"ravi kumar","phones":["9840012345","9000011111"],"email":"ravi.work@example.com"},{"name":"No Number","phones":[],"email":"none@example.com"}]
print("Merged:",merge([a,b]))
for n in (1000,100000):
    data=[{"name":f"Person{i}","phones":[f"{9000000000+i:010d}"],"email":""} for i in range(n)]
    t=time.perf_counter(); result=merge([data]); elapsed=time.perf_counter()-t
    print(n,"contacts:",elapsed,"seconds; merged:",len(result))
