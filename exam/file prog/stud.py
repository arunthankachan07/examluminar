def printStud(**kwargs):
    studdata = open("student.txt", "r")
    stud_det = []

    if 'id' in kwargs and 'property' in kwargs:
        roll=kwargs['id']
        prop=kwargs['property']
        # print(prop)
        for data in studdata:
            row = data.rstrip("\n").split(",")
            # print(row)
            if roll==int(row[0]):
                stud_det.append(row[1])
                print(stud_det)
                if prop=="total":
                    stud_det.append(row[3])
                    print(stud_det)
    studdata.close()
def max_marks():
    studdata = open("student.txt", "r")
    max_mark=[]
    for data in studdata:
        row = data.rstrip("\n").split(",")
        max_mark.append(row[3])
    if max(max_mark)==row[3]:
        print("Highest mark student details")
        print(row[0],row[1],row[2],row[3])


printStud(id=100)
printStud(id=100,property="total")
max_marks()