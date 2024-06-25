class test_utils():

    def __init__(self) -> None:
        pass
        
        
    
    def quick_print_list_dict(self,aList):
        if type(aList) == list:
            for i,v in enumerate(aList):
                print(i,v)
        elif type(aList) == dict:
            for i in aList:
                print(i,aList[i])

    def check_problem_number(self,aList):
        summ = 0
        if type(aList) == list:
            print(len(aList))
        elif type(aList) == dict:
            for i in aList:
                summ += len(aList[i])
            print(summ)