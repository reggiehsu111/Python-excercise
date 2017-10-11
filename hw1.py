input_data=input("請輸入數字序列:")
input_data=list(map(int,input_data.split()))
size=input_data[0]
List=input_data[1:size+1]
List.sort()
for i in input_data[size+1:]:
    if i == 0:
        break
    else:
        print ("第{}大的數是: {}".format (i,List[-i]))
