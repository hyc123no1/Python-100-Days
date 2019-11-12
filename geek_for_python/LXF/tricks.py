from collections import Counter
a = [1,2,3,1,2,3,2,2,4,5,1]

print(max(set(a),key=a.count))

cnt = Counter(a)
print(cnt.most_common(4))

#checking if tow words are anagrams
str1='abc'
str2='cba'
if Counter(str1) == Counter(str2):
    print("hello")

# reverse a string 
a = 'abcdefghijklmnopqrstuvwxyz'
print(a[::-1])

for char in reversed(a):
    print(char)

#reverse a list 
a = [ 5,4,3,2,1]
print(a[::-1])

for ele in reversed(a):
    print(ele)


