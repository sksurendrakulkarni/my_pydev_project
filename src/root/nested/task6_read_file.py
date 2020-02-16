infile = open('T6_inpt.txt')
lst = []
total_multiplications = []
total_count = 0
line = infile.readline()
while line != '':
    lst = line.split()
    if (len(lst) == 2):
        #print(lst)
        total_multiplications.append(float(lst[0]) * float(lst[1]))
        total_count += 1

    #print(line, end='')
    line = infile.readline()
#avg = float(total_sum / total_count)
total_multiplications.sort(key=None, reverse=False)
#print("total multiplications =", total_multiplications)
print("Maximum multiplication =" , total_multiplications[total_count - 1])
print("Minimum multiplication =" , total_multiplications[0])
#print("total_count =", total_count)
#print("Average =", avg)