"""The function avgavg() takes as input a list whose items are list of three numbers.
Each three number list represent the three is an input.
list for a class of four students [(95,92,86),(66,75,64),(89,72,100) and (34,0,0)] """
def avgavg(grade_list):
    st_avg=[]
    for i in grade_list:
        student_avg=sum(i)/len(i)
        st_avg.append(student_avg)
    class_average=sum(st_avg)/len(st_avg)
    print(st_avg)
    print(class_average)
avgavg([[95,92,86],[66,75,54],[89,72,100],[34,0,0]])