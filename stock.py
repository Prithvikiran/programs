from qu import Queue
st=Queue()
no=Queue()
k=1
cap=0
t=int(input("Enter number of transactions :"))
print('\n-------Enter the stock price and the cost price------')
for i in range(t):
 i=int(input(f"\nEnter stock price for trade number {k}:"))
 j=int(input(f"\nEnter the number of stocks for trade number {k}: "))
 st.enqueue(i)
 no.enqueue(j)
 k=k+1
s=int(input("\nEnter the selling price :"))
n=int(input("\nEnter the number of stock for the sale:"))
while(n>0):
    
    y=st.dequeue()
    x=no.dequeue()
    
    if(n>=x): 
      cap=cap+(x*(s-y))
      n=n-x
    else:
        cap=cap+(n*(s-y))
        break
print("\nThe capital gains of the transaction is:",cap)





  