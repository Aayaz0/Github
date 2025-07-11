'''
set1 = { 1, 2, 3, 4, 5 }
set2 = { 4, 5, 6, 7, 8 }
froset1 = frozenset(set1)
froset2 = frozenset(set2)
print(froset1)
print(froset2)
print(froset1.intersection( froset2 ) )  


from collection import deque
dq = deque([1, 2, 3, 4, 5])
dq.append(6)
dq.appendleft(0)
dq.remove(2) 
dq.extend([7, 8])
print(dq)
print(dq.pop())
print(dq.popleft())
print(dq)
print(dq.count(3))  
print(dq.index(4))  




#from collection import default


'''



















square = { x * 2 for x in range(5) }
for val in square:
    print(val)      
    

marks = [60, 70, 80, 90]

def s_grade(mark):
    if mark>= 90:
        return 'A'
    elif mark>= 80:
        return 'B'
    elif mark>= 70:
        return 'C'
    else:
        return 'D'

grade = { mark: s_grade(mark) for mark in marks}

print("Student Grades:", grade)


marks = [60,70,80,90]
def s_grade(marks):
   if marks >=90:
       return 'A'
   elif marks >=80:
       return 'B'
   elif marks >=70:
       return 'C'    
   else:
       return 'D'      

grade = { s_grade, marks }
print("Student marks:",marks)
print("Student Grades:", next(grade))


from collection import reduce 
num = [1, 2, 3, 4, 5]
def sum(x, y):
    return x + y
sum= reduce(sum, num)
print(sum)

class NegativeNumberError(Exception):
 pass
#exception handling
 try:
        num = int(input("Enter a number: "))
        result = 10 / num
        print(f"Result: {result}")
 except ZeroDivisionError:
                    print("Error: Division by zero is not allowed.")
 except ValueError:
        print("Error: Invalid input. Please enter a valid number.")
        