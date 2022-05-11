def ArtOperation(arg1, arg2):
    if type(arg1) != type(arg2):
        print ('Please enter the arguments of same type!')
        return

    return(arg1 + arg2)

#a = ArtOperation(25, 30)
#print(a)
#print(ArtOperation('Safdar', ' Jahan'))
#ArtOperation('Safdar', 20)

def students(name='Muhammad', age=2, DOB='19-April-2019', **marks):
    print('name', name)
    print('Age', age)
    print('DateOfBirth', DOB)
    #print(marks)
    #for x in marks:
     #   print(x)
    for key, value in marks.items():
        print(key, ' ', value)


#students('safdar', 34,'01-January-1986')
students('Safdar', 34, '01-January-1986',english=77, math=89, physics=87,chemistry=59)
    