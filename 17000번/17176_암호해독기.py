chk_dic = {0:" ",1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K",12:"L",13:"M",14:"N",15:"O",16:"P",17:"Q",18:"R",19:"S",20:"T",21:"U",22:"V",23:"W",24:"X",25:"Y",26:"Z",
27:"a",28:"b",29:"c",30:"d",31:"e",32:"f",33:"g",34:"h",35:"i",36:"j",37:"k",38:"l",39:"m",40:"n",41:"o",42:"p",43:"q",44:"r",45:"s",46:"t",47:"u",48:"v",49:"w",50:"x",51:"y",52:"z"}
t = int(input())
a = list(map(int,input().split()))
compare_str = list(input())
ans = []
for i in a:
    ans.append(chk_dic[i])
if sorted(compare_str) == sorted(ans):
    print("y")
else:
    print("n")
