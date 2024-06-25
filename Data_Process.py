from datetime import date
from Data_Process_Utils import data_process_utils
class data_process():

    def __init__(self,problems_raw_data) -> None:

        self.problems_raw_data = problems_raw_data

        self.done_time_id_dict = dict()
        self.id_content_dict = dict()
        self.id_title_dict = dict()
        self.failed_times_id_dict = dict()
        self.working_time_id_dict = dict()
        self.tag_id_dict = dict()

        self.utils = data_process_utils()
        self.id_content_sort()
        self.done_time_id_sort()
        self.failed_times_id_sort()
        self.working_time_id_sort()
        self.tag_id_sort()
        self.id_title_sort()

    """
    categorized_by_time function return a dict which key is the date, and the 
    values are the problem number that I have done that day
    eg: {2024-06-19: [18,19,11] }
    """
    def done_time_id_sort(self):
        for i in range(len(self.problems_raw_data)):
            x = self.utils.done_time_find(self.problems_raw_data[i][1])
            if x:
                prev_match = date.fromisoformat(x.group(0))
                if prev_match not in self.done_time_id_dict:
                    self.done_time_id_dict[prev_match] = []
            else:
                prob_num = self.utils.prob_num_find(self.problems_raw_data[i][1])
                self.done_time_id_dict[prev_match].append(prob_num)


    """
    fill in the id_content_sort dict which key = problem number and values are 
    the rest of contents of this problem
    """
    def id_content_sort(self):
        for problem in self.problems_raw_data:
            problem_title = self.utils.prob_title_find(problem[1])
            if problem_title:
                problem_number = self.utils.prob_num_find(problem[1])
                self.id_content_dict[problem_number] = problem[1:]

    """
    categorized_by_problem function return a dict which key is the problem number, and the 
    values are the name and the link of the problems
    eg: {88 : [[88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) }
    """
    def id_title_sort(self):
        for problem in self.id_content_dict:
            self.id_title_dict[problem] = self.id_content_dict[problem][0]


    """
    fill in the failed_times_id dict which key = failed times and values are a list of 
    problems that has this failed time
    """
    def failed_times_id_sort(self):
        for problem in self.id_content_dict:
            failed_times = self.utils.failed_times_find(self.id_content_dict[problem][2])
            if failed_times not in self.failed_times_id_dict:
                self.failed_times_id_dict[failed_times] = [] 
                self.failed_times_id_dict[failed_times].append(problem)
            else:
                self.failed_times_id_dict[failed_times].append(problem)


    """
    fill in the working time id dict which key = working times and values are a list of 
    problems that has this working time
    """
    def working_time_id_sort(self):
        for problem in self.id_content_dict:
            working_time = self.utils.working_time_find(self.id_content_dict[problem][-1])
            if working_time not in self.working_time_id_dict:
                self.working_time_id_dict[working_time] = [] 
                self.working_time_id_dict[working_time].append(problem)
            else:
                self.working_time_id_dict[working_time].append(problem)
        

    """
    fill in the working time id dict which key = tags and values are a list of 
    problems that has this tag
    """
    def tag_id_sort(self):
       for problem in self.id_content_dict:
            tag_list = self.id_content_dict[problem][1].split('#')
            tag_list = [tag.strip() for tag in tag_list if tag != '']
        
            for tag in tag_list:
                if tag not in self.tag_id_dict:
                    self.tag_id_dict[tag] = [] 
                    self.tag_id_dict[tag].append(problem)
                else:
                    self.tag_id_dict[tag].append(problem)
        