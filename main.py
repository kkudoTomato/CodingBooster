from RW_Utils import rw_utils
from policy import arrangement
from datetime import date
utils = rw_utils()
utils.import_data()
utils.categorized_by_time()
utils.categorized_by_problem()
utils.genPracticePlan()
problems = utils.get_reduced_prob_data()
time_problems = utils.get_reduced_time_data()
todayProb = utils.getTodayProb()
pracPlan = utils.getPracticePlan()

policy = arrangement(problems)

betterPlan = policy.distribute_work(pracPlan)
today_task = betterPlan[date.today()]

utils.write_md(today_task)
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

