data = input()
i=0 #계속 헤맸던 부분의 
vowels=['a','e','i','o','u']
while i<len(data):
    print(data[i],end="")
    if data[i] in vowels:
        i+=2 
    i+=1
