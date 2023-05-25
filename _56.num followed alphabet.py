s=input("enter string:")
alpha=[]
digit=[]
for i in s:
    if s.isalpha():
        alpha.append(i)
    else:
        digit.append(i)
ans=''.join(sorted(digit)+sorted(alpha))
print(ans)