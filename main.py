from RW_Utils import rw_utils

utils = rw_utils()
utils.import_data()
utils.categorized_by_time()
utils.categorized_by_problem()
utils.genPracticePlan()
problems = utils.get_reduced_prob_data()
time_problems = utils.get_reduced_time_data()
todayProb = utils.getTodayProb()
pracPlan = utils.getPracticePlan()

#for i in todayProb:
    #print(i)

#for i,v in problems.items():
    #print(i,v)

# for i,v in time_problems.items():
    # print(i,v)

for i,v in pracPlan.items():
    print(i,v)

#print(len(problems))
