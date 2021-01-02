import time

# q is the number of queries to be inputted
num = int(input())
q_container = [] # To hold entries
final_data = {} # To hold final results
for qe in range(num):
    q_container.append(input().split()) # taking and splitting inputs
    
for i in q_container:
    final_data[i[0]] = []


def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
then = time.time()
    
# first we take the f(n) the sum of its digits factorials: f(342) = 3!+4!+2! = 32
def f(n):
    f_result = 0
    num = list(str(n).split(','))
    #print(num)
    for i in num[0]:
        f_result += factorial(int(i))
    return f_result
#f(nn) just a test
#f_returned = f(nn) just a test
#print(f_returned) just a test


# second take the sf(n) = sum of f(n) results digits sf(342) = 3 + 2 = 5
def sf(n):
    sf_result = 0
    fresulted = f(n)
    num = list(str(fresulted).split(',')) # we should include the f function first
    for i in num[0]:
        sf_result += int(i)
    return sf_result
# sf_returned = sf(nn) just a test
# print(sf_returned) just a test
# third chech for g(i)
##  the g(i) is the smallest positive nn where sf(nn) == i
### so we shall loop every nn from 1 untill sg(nn) == i
#i = input()
def g(i, given):
    # loops
    g_result = 0
    for x in range(1, given):
        loop_res = sf(x)
        if loop_res != i:
            continue
        else:
            g_result = x
            break
        
    return g_result

## Since we have the g(i) then sg(i) will be the sum of results's digits just like sf(n)
def sg(i, given):
    # first we need th g(i)
    g_res = list(str(g(i, given)).split())
    sg_res = 0
    for y in g_res[0]:
        sg_res += int(y)
    return sg_res



for q in q_container:
    for x in range(1, int(q[0])+1):
        final_data[q[0]].append(sg(x, int(q[1])))

for value in final_data:
    print(sum(final_data[value]))
    
fine = time.time()
print(fine-then)