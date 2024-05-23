map = {'apple':'사과', 'banana':'바나나', 'cherry':'체리'}

for e in map:
    print("%s => %s"%(e,map[e]))

map['grape'] = '포도'
print(map)

map.update({'orange':'오렌지','mandarin':'귤'})
print(map)

print(map.keys())
print(map.values()) 