def powoft(n):
    if n>0 and n&(n-1)==0:
        print("2")
def powoff(n):
    m=0xAAAAAAAAAAA
    if n>0 and n&(n-1)==0 and m&n==0:
        print("4")
n=int(input())
print('1')
powoft(n)
powoff(n)
