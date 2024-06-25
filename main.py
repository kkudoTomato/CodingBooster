from RW_Utils import rw_utils
from policy import arrangement
from datetime import date
from Data_Process import data_process
def quick_print(aList):
    if type(aList) == list:
        for i,v in enumerate(aList):
            print(i,v)
    elif type(aList) == dict:
        for i in aList:
            print(i,aList[i])

def check_num(aList):
    summ = 0
    if type(aList) == list:
        print(len(aList))
    elif type(aList) == dict:
        for i in aList:
            summ += len(aList[i])
        print(summ)

utils = rw_utils()
utils.import_data()
raw_data = utils.get_raw_data()
#quick_print(raw_data)
dp = data_process(raw_data)
#dp.done_time_id_sort()
#quick_print(dp.done_time_id_dict)
#dp.id_title_sort()
#quick_print(dp.id_title_dict)
#quick_print(dp.id_content_dict)
#quick_print(dp.working_time_id_dict)
#quick_print(dp.failed_times_id_dict)
#check_num(dp.failed_times_id_dict)
#quick_print(dp.working_time_id_dict)
#check_num(dp.working_time_id_dict)
#dp.tag_id_sort()
#print(len(dp.id_content_dict))
quick_print(dp.tag_id_dict)






#utils.categorized_by_time()
#utils.categorized_by_problem()
#utils.genPracticePlan()
#problems = utils.get_reduced_prob_data()
#time_problems = utils.get_reduced_time_data()
#todayProb = utils.getTodayProb()
#pracPlan = utils.getPracticePlan()
#
#policy = arrangement(problems)

#betterPlan = policy.distribute_work(pracPlan)
#today_task = betterPlan[date.today()]

#utils.write_md(today_task)
#for day,task in betterPlan.items():
   #print(day,task)

#for i in todayProb:
    #print(i)

#for i,v in problems.items():
#    print(i,v)

# for i,v in time_problems.items():
    # print(i,v)

#for i,v in pracPlan.items():
    #print(i,v)

# summ = 0
# for i in time_problems:
    # summ += len(time_problems[i])
# print(summ)

#print(len(problems))

