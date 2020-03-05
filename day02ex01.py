#
str1 = """$#@#aa<img src="aaa">@@@<img src="bbb">@@@<img src="ccc">@@@"""
srcList=["img/aa.jpg","img/bb.jpb","img/cc.jpg"]

newList=[]

findWord='src"'
str2=str1
i=0
while str2.find(findWord) !=-1:
    startIdx=str1.find(findWord)+len(findWord); # start
    str2=str2[startIdx:]
    newList.append(str2[:startIdx])
    newList.append(srcList[i])
    str2=str2[startIdx:]
    endIdx=str2.find('"'); # end
    str2=str2[endIdx:]
    i+=1

newList.append(str2)

return "".join(newList)