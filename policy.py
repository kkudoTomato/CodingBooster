from datetime import date
from datetime import timedelta

"""
Last Finished Time : | Hardness | Problem Name | Tag | Failed Times | Solve Time |  

"""
class arrangement():

    def __init__(self,raw_data:dict) -> None:
        self.raw_data = raw_data
        self.calendar = dict()
        for i in range(1,31):
            today = date.today()
            dict[today + timedelta(days=i)] = []

    def normal_next_prac(self, prac_date:date, problem_number:int) -> list:
        next_1_day = prac_date + timedelta(days=1)
        next_2_day = prac_date + timedelta(days=2)
        next_4_day = prac_date + timedelta(days=4)
        next_week = prac_date + timedelta(days= 7)
        next_2_week = prac_date + timedelta(days= 15)
        next_month = prac_date + timedelta(days= 30)
        #next_3_month = prac_date + timedelta(days= 90)
        #next_6_month = prac_date + timedelta(days= 180)
        return [problem_number, next_1_day,next_2_day,next_4_day,next_week,
                next_2_week, next_month]

    def failed_next_prac(self, failed: int) -> list:
        pass

    def hardness_next_prac(self, hardness: int) -> list:
        pass
    def proficiency_next_prac(self, workingTime:int) -> list:
        pass

    def overall_next_prac(self) -> list:
        # self.raw_data = { date1: problem_num, d2: p4, ...}
        for t, p in enumerate(self.raw_data):
            print(t,p)
        # failed > normal > hardness and use solve time as a tie breaker

    def overall_sort_algo(self, input_list:list) ->list:

        pass






