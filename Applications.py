from datetime import date
from datetime import timedelta

class application:
    def __init__(self,problem_review_plan) -> None:
        self.problem_review_plan = problem_review_plan

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


        