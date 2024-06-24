from datetime import date
from datetime import timedelta

"""
Last Finished Time : | Hardness | Problem Name | Tag | Failed Times | Solve Time |  

"""
class arrangement():

    def __init__(self,raw_data:dict) -> None:
        self.raw_data = raw_data
        self.calendar = dict()
        for i in range(0,31):
            today = date.today()
            target_date = today + timedelta(days=i)
            self.calendar[target_date] = []

    def get(self) -> dict:
        return self.calendar

    def arrange_base_on_date(self):
        #print(self.raw_data)
        for d,p in self.raw_data.items():
            #print(d,p)
            self.normal_next_prac(d,p)
        
        self.flatten()

    def flatten(self):
        for i in self.calendar:
            self.calendar[i] = [val for sublist in self.calendar[i] for val in sublist]



    def normal_next_prac(self, prac_date:date, problem_number:list) -> None:
        today = date.today()
        tmr = today + timedelta(days=1)
        next_1_day = prac_date + timedelta(days=1)
        next_2_day = prac_date + timedelta(days=2)
        next_4_day = prac_date + timedelta(days=4)
        next_week = prac_date + timedelta(days= 7)
        next_2_week = prac_date + timedelta(days= 15)
        next_month = prac_date + timedelta(days= 30)
        next_3_month = prac_date + timedelta(days= 90)
        next_6_month = prac_date + timedelta(days= 180)
        date_list = [next_1_day,next_2_day,next_4_day,next_week, next_2_week, next_month,next_3_month,next_6_month]
        #print(prac_date,problem_number)

        for i in date_list:
            if i in self.calendar:
                self.calendar[i].append(problem_number)
        

    """
    distribute_work will equally distribute problems to each day 
    """
    def distribute_work(self,timeProb_dict):
        temp_task = []
        num_task = 0
        for day in timeProb_dict:
            num_task += len(timeProb_dict[day])
        #find the average number of tasks per day
        average_task = num_task//(len(timeProb_dict.keys()))
        for day in timeProb_dict:
            task_diff = len(timeProb_dict[day]) - average_task
            if task_diff > 0:
                temp_task.extend(timeProb_dict[day][-task_diff:])
                timeProb_dict[day] = timeProb_dict[day][:average_task]
            elif task_diff < 0:
                task_diff = abs(task_diff)
                timeProb_dict[day].extend(temp_task[:task_diff]) 
                temp_task = temp_task[task_diff:]

        
        if temp_task:
            for i in range(len(temp_task)):
                timeProb_dict[list(timeProb_dict.keys())[i]].append(temp_task[i])

        return timeProb_dict




    def failed_next_prac(self, failed: int) -> list:
        pass

    def hardness_next_prac(self, hardness: int) -> list:
        pass
    def proficiency_next_prac(self, workingTime:int) -> list:
        pass

    def overall_next_prac(self) -> list:
        # self.raw_data = { date1: problem_num, d2: p4, ...}
        # failed > normal > hardness and use solve time as a tie breaker
        #tbu
        pass

        



    def advance_by(self, target_date:date, problem_num:int,advance_date:int) ->None:
        time_diff  = target_date - date.today()
        while time_diff.days >= 0:
            next_date = target_date - timedelta(days=advance_date)
            time_diff = next_date-target_date
            if problem_num not in self.calendar[next_date]:
                self.calendar[next_date].append(problem_num)
                self.calendar[target_date].remove(problem_num)
                return


    def delay_by(self, target_date:date, problem_num:int,delay_day:int) ->None:
        # failed * 0.5 + normal * 0.4 + hardness * 0.1 and solve problem is super low can remove one category <10min
        # category problems base on their normal date, and add problems base on that
        self.calendar[target_date].remove(problem_num)
        next_date = target_date + timedelta(days=delay_day)
        if problem_num not in self.calendar[next_date]:
            self.calendar[next_date].append(problem_num)
    






