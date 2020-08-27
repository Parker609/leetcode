class Entity(object):
  '''数据实体，假设这是一种数据存储的结构'''
  def __init__(self, key, value):
    self.key = key
    self.value = value

entity1 = Entity(2,2)
entity2 = Entity(6,6)
entity3 = Entity(4,4)
entity4 = Entity(3,3)

tempDict = [entity1,entity2,entity3,entity4]
print(tempDict.find())
# for i,e in enumerate(tempDict):
#   print(i,e)

point = {"a":123}
tempList = []
tempList.append(point)
point = {"b":455}
tempList.append(point)
for i in tempList:
  print(i)

# print(tempDict.sort(key=lambda x:x.key))