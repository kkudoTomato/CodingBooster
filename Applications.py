from datetime import date
from datetime import timedelta
from policy import arrangement
from Data_Process import data_process

class application:
    def __init__(self,time_id_dict,missed_q) -> None:
        self.problem_review_plan = dict()
        self.time_id_dict = time_id_dict
        self.missed_q =missed_q
        self.genPracticePlan()

    def genPracticePlan(self):
        policys = arrangement(self.time_id_dict)
        policys.arrange_base_on_date()
        self.problem_review_plan = policys.calendar
        policys.distribute_work(self.problem_review_plan)
        policys.add_in_freq_miss_questions(self.missed_q,self.problem_review_plan)

    def get_tmr_problems(self):
        tmr = date.today() + timedelta(days=1)
        tmr_problem = self.problem_review_plan[tmr]
        return tmr_problem
        

    def get_today_problems(self):
        today = date.today()
        today_problem = self.problem_review_plan[today]
        return today_problem

    def get_this_week_problems(self):
        this_week_prob = []
        for i in range(7):
            day = date.today() + timedelta(days=i) 
            for id in self.problem_review_plan[day]:
                this_week_prob.append(id)

        return this_week_prob


        