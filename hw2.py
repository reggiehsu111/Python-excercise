s = input("請輸入字串: ")
ans=False
n=0;
while n < len(s):
    list1=s[:n+1]
    list2=s[n+1:len(s)]
    if list1==list1[::-1] and list2==list2[::-1]:
        ans=True
        print(s +"是雙回文字串, "+ s + " = " + s[:n+1] + " + " + s[n+1:])
    n+=1
if ans == False :
    print(s + "不是雙回文字串")
