from os import walk
import re
from datetime import date
from datetime import timedelta
from policy import arrangement

"""
class read_data_utils provides utilities to read data, clean data, and sort data

"""

class rw_utils():

    def __init__(self) -> None:
        #problem contains raw data from the file
        self.problem_raw_data = list()
        #reduced dict contains time as the key and problem numbers as the value. Format like {time: [p1,p2,...]}
        self.reducedTimeProbNum = dict()
        self.reducedProblemTitle = dict()
        self.practicePlan = dict()
        self.pathList = []

        self.path_dir = '/Users/door3/Documents/Obsidian Vault/一花一世界/1 工作学习/1 算法题总结/Leedcode Review'
        self.not_want_list= ['\n','','==START==']

    """
    import_data grab data from target markdown files and add them into problem_raw_data list
    """
    def find_all_file_path(self):
        for (dirpath, dirnames, filenames) in walk(self.path_dir):
            for filename in filenames:
                if re.search('(?i)Log',filename):
                    self.pathList.append(f'{dirpath}/{filename}')
        
        #print(self.pathList)

    def import_data(self):
        self.find_all_file_path()
        for path in self.pathList:
            with open(path) as practice_log:
                n = 0
                for line in practice_log:
                    #clean up inputs
                    list_current_line = self.clean_input(line)

                    n += 1
                    if len(list_current_line)> 0 and list_current_line[1] not in self.not_want_list :
                        if list_current_line[0] != 'f':
                            self.problem_raw_data.append(list_current_line)

    """
    clean input get rid of unwanted symbols and emojis
    """
    def clean_input(self,line):
        list_line = line.split('|')
        """
        TBU
        this can be updated with a single for loop
        """
        #get rid of unwanted symbols such as '\n','', and '==START=='
        list_line = [i.strip() for i in list_line if i not in self.not_want_list]
        #get rid of the .md table formatter 
        list_line = [i for i in list_line if not re.search('----+',i)]
        #get rid of empty rows 
        list_line = [list_line[i] for i in range(len(list_line)) if i != 4 ]
        #update working time if I don't solve the problem replace 'X' with 59min
        if len(list_line) > 0:
            list_line[-1] = '59min' if list_line[-1] != '' and not re.search('\d\d?min',list_line[-1]) else list_line[-1]
            list_line[0] = list_line[0][3:]
        return list_line

    def genPracticePlan(self,time_id_dict):
        policys = arrangement(time_id_dict)
        policys.arrange_base_on_date()
        self.practicePlan = policys.get()
        return policys.distribute_work(self.practicePlan)


    def write_md(self,problem_list,content_dict):
        tmr = date.today() + timedelta(days=1)
        full_path=f'{self.path_dir}/REVIEW-PROBLEMS.md'

        with open(full_path,'a') as f:
            f.write(f'## {str(tmr)} problems\n')
            for line in problem_list:
                content = content_dict[line]
                f.write('- [ ] ' + content+ '\n')
                print(content)
        


