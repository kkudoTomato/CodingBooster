import re
class data_process_utils():

    def __init__(self) -> None:
        pass

    def done_time_find(self,problem_info) -> str:
        x = re.search('\d{4}-\d\d?-\d\d?',problem_info)
        return x
    def prob_num_find(self, problem_info) -> int:
        problem_num = re.search('\d+.',problem_info)
        int_problem_num = int(problem_num.group(0)[:-1])
        return int_problem_num
    
    def prob_title_find(self,problem_info) -> str:
        #reduceToTile = [i[1] for i in self.problem_set if re.search('[.*]',i[1])]
        problem_title = problem_info if re.search('[.*]',problem_info) else None
        return problem_title


    def working_time_find(self,working_time) -> int:
        working_time = re.search('\d\d*',working_time)
        return working_time.group(0) if working_time else '???'

    def failed_times_find(self,failed_times) -> int:
        failed_times = re.search('\d\d*',failed_times)
        return failed_times.group(0) if failed_times else '???'

    def practice_times_find(self,practice_times) -> int:
        practice_times = re.search('\d\d*',practice_times)
        return practice_times.group(0) if practice_times else '???'

    def pass_rate_cal(self,failed_times,practice_times) -> float:
        if failed_times.isdigit() and practice_times.isdigit():
            pass_rate = round(float(failed_times)/float(practice_times),1) 
            return pass_rate
        else:
            return '???'
