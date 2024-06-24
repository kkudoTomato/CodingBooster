import os
from os import path
import re
import datetime
from datetime import date
from policy import arrangement
from problems import sort_by_prob_num

"""
class read_data_utils provides utilities to read data, clean data, and sort data

"""
path = '/Users/door3/Documents/Obsidian Vault/一花一世界/1 工作学习/1 算法题总结/Leedcode Review/1st 50 Problems/1st 50 Leedcode Algos Log.md'
not_want_list= ['\n','','==START==']

class rw_utils():

    def __init__(self) -> None:
        #problem contains raw data from the file
        self.problem_set = list()
        #reduced dict contains time as the key and problem numbers as the value. Format like {time: [p1,p2,...]}
        self.reducedTimeProbNum = dict()
        self.reducedProblemTitle = dict()
        self.practicePlan = dict()

    def get_raw_data(self)->list:
        return self.problem_set

    def get_reduced_time_data(self)->list:
        return self.reducedTimeProbNum

    def get_reduced_prob_data(self)->list:
        return self.reducedProblemTitle

    def getTodayProb(self):
        return self.practicePlan[date.today()]

    def getPracticePlan(self):
        return self.practicePlan
    """
    import_data grab data from target markdown files and add them into problem_set list
    """
    def import_data(self):
        with open(path) as practice_log:
            n = 0
            for line in practice_log:
                #clean up inputs
                list_current_line = self.clean_input(line)

                n += 1
                if len(list_current_line)> 0 and list_current_line[1] not in not_want_list :
                    self.problem_set.append(list_current_line)

    """
    clean input get rid of unwanted symbols and emojis
    """
    def clean_input(self,line):
        not_want_list= ['\n','','==START==']
        list_line = line.split('|')
        """
        TBU
        this can be updated with a single for loop
        """
        #get rid of unwanted symbols such as '\n','', and '==START=='
        list_line = [i.strip() for i in list_line if i not in not_want_list]
        #get rid of the .md table formatter 
        list_line = [i for i in list_line if not re.search('----+',i)]
        #get rid of empty rows 
        list_line = [list_line[i] for i in range(len(list_line)) if i not in range(3,5) ]
        #update working time if I don't solve the problem replace 'X' with 59min
        if len(list_line) > 0:
            list_line[-1] = '59min' if list_line[-1] != '' and not re.search('\d\d?min',list_line[-1]) else list_line[-1]
            list_line[0] = list_line[0][3:]
        return list_line


    """
    find_prob_num return the problem number in the target line 
    """
    def find_prob_num(self, problem_info) -> int:
        problem_num = re.search('\d+.',problem_info[1])
        int_problem_num = int(problem_num.group(0)[:-1])
        return int_problem_num


    """
    categorized_by_time function return a dict which key is the date, and the 
    values are the problem number that I have done that day
    eg: {2024-06-19: [18,19,11] }
    """
    def categorized_by_time(self):
        for i in range(1,len(self.problem_set)):
            x = re.search('\d{4}-\d\d?-\d\d?',self.problem_set[i][1])
            if x:
                prev_match = date.fromisoformat(x.group(0))
                self.reducedTimeProbNum[prev_match] = []
            else:
                prob_num = self.find_prob_num(self.problem_set[i])
                self.reducedTimeProbNum[prev_match].append(prob_num)

    

    """
    categorized_by_problem function return a dict which key is the problem number, and the 
    values are the name and the link of the problems
    eg: {88 : [[88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) }
    """
    def categorized_by_problem(self):
        reduceToTile = [i[1] for i in self.problem_set if re.search('[.*]',i[1])]
        for line in range(1,len(self.problem_set)):
            if re.search('[.*]',self.problem_set[line][1]):
                prob_num = self.find_prob_num(self.problem_set[line])
                self.reducedProblemTitle[prob_num] = f'- [ ] {self.problem_set[line][1]}'


    def genPracticePlan(self):
        policys = arrangement(self.reducedTimeProbNum)
        policys.arrange_base_on_date()
        self.practicePlan = policys.get()


    def write_md(self):
        pass
        


