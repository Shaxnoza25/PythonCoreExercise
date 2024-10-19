a=int(input())
b=int(input())
result=(a & 1)==0 and (b & 1)==0
print("both are even"*result+"at least one is odd"*(not result))