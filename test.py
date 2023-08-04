from rubix_cube import rubix_cube
from rubix_cube import clockwise
from rubix_cube import counter_clockwise

# print out rubix_cube array
def print_rubix_cube(rubix_cube):
    temp = 1
    for i in range(len(rubix_cube)):
        for j in range(len(rubix_cube[i])):
            print(rubix_cube[i][j])
            if temp%3 == 0:        
                print("---------------")
            temp+=1
            
# enter scramble
def enter_scramble_auto():
    scramble_list = []
    x = 0
    while (True):      
        scramble_list.append(input())
        if len(scramble_list[x]) > 2:
            del scramble_list[x]
            break
        x+=1
    print(scramble_list)
    for i in range(len(scramble_list)):
        clockwise(scramble_list[i], rubix_cube)
    return rubix_cube

clockwise(1, rubix_cube)
print_rubix_cube(rubix_cube)