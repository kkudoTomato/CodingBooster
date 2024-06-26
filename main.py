from RW_Utils import rw_utils
from policy import arrangement
from datetime import date
from datetime import timedelta
from Data_Process import data_process
from Test_Utils import test_utils
from Applications import application


quick_test = test_utils()
utils = rw_utils()
utils.import_data()
raw_data = utils.problem_raw_data
#quick_test.quick_print_list_dict(raw_data)
dp = data_process(raw_data)
#quick_test.quick_print_list_dict(dp.problems_raw_data)

#dp.done_time_id_sort()
#quick_test.quick_print_list_dict(dp.done_time_id_dict)
#dp.id_title_sort()
#quick_test.quick_print_list_dict(dp.id_title_dict)
#quick_test.quick_print_list_dict(dp.id_content_dict)
#quick_test.quick_print_list_dict(dp.working_time_id_dict)
#quick_test.quick_print_list_dict(dp.passrate_id_dict)
#quick_test.quick_print_list_dict(dp.done_time_id_dict)
#quick_test.check_problem_number(dp.passrate_id_dict)
#quick_test.check_problem_number(dp.working_time_id_dict)
#quick_test.check_problem_number(dp.failed_times_id_dict)
#quick_test.quick_print_list_dict(dp.working_time_id_dict)
#quick_test.check_problem_number(dp.working_time_id_dict)
#dp.tag_id_sort()
#print(len(dp.id_content_dict))
#quick_test.quick_print_list_dict(dp.tag_id_dict)




#problem_review_plan = utils.genPracticePlan(dp.done_time_id_dict)
missed_q = []
for key in dp.passrate_id_dict:
    if key > 0.3:
        for i in dp.passrate_id_dict[key]:
            missed_q.append(i)
    
app = application(dp.done_time_id_dict,missed_q)
#quick_test.quick_print_list_dict(app.problem_review_plan)
today_prob = app.get_today_problems()
tmr_prob = app.get_tmr_problems()
print(tmr_prob)
utils.write_md(today_prob,dp.id_title_dict)
utils.write_md(tmr_prob,dp.id_title_dict)
#quick_test.quick_print_list_dict(today_prob)
#quick_test.quick_print_list_dict(tmr_prob)




#thisWeekProb = app.get_this_week_problems()
#quick_test.quick_print_list_dict(thisWeekProb)
#print(thisWeekProb)
#quick_test.quick_print_list_dict(problem_review_plan)
#tmr = date.today() + timedelta(days=1)
#tmr_problme = problem_review_plan[tmr]
#quick_test.quick_print_list_dict(tmr_problme)
#quick_test.quick_print_list_dict(dp.id_title_dict)
#utils.write_md(tmr_problme,dp.id_title_dict)




