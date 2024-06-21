import os
from os import path
import re
import datetime
from datetime import date

#path = '/Users/door3/Documents/Obsidian Vault/一花一世界/1 工作学习/1 算法题总结/Leedcode Review'
def cleanUpInput():
    path = '/Users/door3/Documents/Obsidian Vault/一花一世界/1 工作学习/1 算法题总结/Leedcode Review/Leedcode Algos Log.md'

    problem_set = []
    not_want_list= ['\n','','==START==']
    with open(path) as practice_log:
        n = 0
        for line in practice_log:
            list_line = line.split('|')
            list_line = [i.strip() for i in list_line if i not in not_want_list]
            list_line = [i for i in list_line if not re.search('----+',i)]
            if len(list_line) > 0:
                list_line[0] = list_line[0][3:]
                

            
        
            #if n in range(5):
                #print(list_line)

            
            
            n+= 1
            
            if len(list_line)> 0 and list_line[1] not in not_want_list :
                problem_set.append(list_line)


    #for i in problem_set:
        #print(i)
    return problem_set

def seperateByTime():
    time_dict = dict()
    problem_set = cleanUpInput() 
    for i in range(1,len(problem_set)):
        x = re.search('\d{4}-\d\d?-\d\d?',problem_set[i][1])
        if x:
            prev_match = date.fromisoformat(x.group(0))
            time_dict[prev_match] = []
        else:
            time_dict[prev_match].append(problem_set[i])


    
    for key,val in time_dict.items():
        print(f'{key} \n {val} \n')

seperateByTime()




