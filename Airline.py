import json
file1 = open('airlines.csv', 'r') 
strng = ""
li = []
cou = []
dics = {}
while True: 
    list1 = []
    # Get next line from file 
    line = file1.readline() 
    if not line: 
        break
    #spliting line as it is seprated by ','
    list1 = line.split (",")
    
    strng = list1[1] + list1[2] 
    
    li.append(strng)
    #print(strng)
  
file1.close()
#removing first name which is "Airport.Name"
li.pop(0)
#geting unique airport names from list by conveting it to set
my_set = set(li)
my_new_list = list(my_set)
for x in range(len(my_new_list)):
               count = 0
               for y in range(len(li)):
                              if my_new_list[x] == li[y]:
                                    # cheking repiting count
                                    count = count + 1 
                                    
               cou.append(count)
               dics[my_new_list[x]] = count

# converting dictinary to json format               
y = json.dumps(dics) 
loaded_r = json.loads(y)
#First output:- Get list of unique airport names and number of times it is repeated in a json format
print(loaded_r)  
print("\n")
# second thired output
print("{} :{} \n\n {} :{}".format(my_new_list[cou.index(max(cou))], max(cou), my_new_list[cou.index(min(cou))], min(cou)))
