# for loops
# for Loop will run to a fixed ranges

obj = [2, 3, 4, 5, 6, 7]  # List taken for example

for i in obj:
    print(i)

for i in obj:  # it will multiple by 2
    print(i * 2)

# print sum of the first natural numbers

for j in range(1, 6):  # It will consider from 1,2,3,4,5
    print(j)

summation = 0
for j in range(1, 6):  # It will consider from 1,2,3,4,5, # same way in java for i=o,i<5,i++
    summation = summation + j
print(summation)  # it will sum up the first 5 natural numbers

for k in range(6):  # It will consider from 0,1,2,3,4,5
    print(k)

for l in range(1, 6, 2):  # It will consider from 3,5 (1+2, 3+2)
    print(l)

##########################################################################################################

# while Loop

# while Loop will run, if the condition is true
# while Loop will stop , if the condition is false


it = 10

# while it > 9:
# print(it)  # it will run infinite loop, because the condition is never false

nt = 10
while nt > 9:
    print(nt)
    nt = nt - 1
print("while loop is done ok")

tt = 4

while tt > 1:
    if tt != 3:  # If you want no.3 is not printed in console (not equal too)
        print(tt)

    tt = tt - 1
print("while loop is done")

qt = 4

while qt > 1:
    if qt == 3:
        break  # break the loop as per the condition you want
    print(qt)

    qt = qt - 1
print("while loop is done almost")

at = 4

while at > 1:
    if at == 3:
        at = at - 1
        continue  # continue will skip the current iteration , will continue the loop
    print(at)

    at = at - 1
print("while loop is done almost all")

ab = 10

while ab > 1:
    if ab == 5:
        ab = ab - 1
        continue

    print(ab)
    ab = ab - 1

print("No. 5 is skipped")
