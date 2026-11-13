import random, re, time
from collections import Counter
calls=["seeds not received seeds delayed","fertiliser price high","seeds price high subsidy not received"]
STOP={"not","high"}
def words(text): return re.findall(r"[a-z]+",text.lower())
def frequencies(texts,stop):
    counts={}
    for text in texts:
        for word in words(text):
            if word not in stop: counts[word]=counts.get(word,0)+1
    return counts
def group_by_district(records):
    grouped={}
    for district, complaint in records:
        grouped.setdefault(district,[]).append(complaint)
    return grouped
def top(counts,k):
    return sorted(counts.items(),key=lambda item:(-item[1],item[0]))[:k]
print(top(frequencies(calls,STOP),3))
print(group_by_district([("Salem","Seeds delayed"),("Madurai","Water issue"),("Salem","Fertiliser problem")]))
for n in (1000,10000,100000):
    data=[random.choice(calls) for _ in range(n)]
    token_list=[w for text in data for w in words(text) if w not in STOP]
    t=time.perf_counter(); d={}
    for w in token_list: d[w]=d.get(w,0)+1
    td=time.perf_counter()-t
    t=time.perf_counter(); lc={w:token_list.count(w) for w in set(token_list)}
    tl=time.perf_counter()-t
    t=time.perf_counter(); c=Counter(token_list); tc=time.perf_counter()-t
    print(n,"dict",td,"list.count",tl,"Counter",tc,"same",d==lc==dict(c))
print("Empty:",frequencies([""],STOP))
print("Case/punctuation:",frequencies(["SEEDS, seeds! NOT received."],STOP))
