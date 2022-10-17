import math 

def find(getter, much):
    global my_dict
    
    my_dict[getter][1] += much - math.trunc(much*0.1)
    if my_dict[getter][0] != '-' and much*0.1 >= 1 : 
        find(my_dict[getter][0],math.trunc(much*0.1))
    
        
my_dict = {}
def solution(enroll, referral, seller, amount):
    answer = []
    
    for i in range(len(enroll)):
        my_dict[enroll[i]] = [referral[i],0]
    
    for i in range(len(seller)):
        my_dict[seller[i]][1] += amount[i]*90

        if my_dict[seller[i]][0] != '-' and amount[i]*10 >= 1 :
            find(my_dict[seller[i]][0],amount[i]*10)
        
    
    for i in enroll:
         answer.append(my_dict[i][1])
    
    return answer