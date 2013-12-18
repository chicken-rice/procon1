if __name__ == '__main__':
    in_file = open('ex1test.txt', 'r')
    line = in_file.readline()
    test_num = int(line[:-1].split(' ')[0])
    #print test_num

    for i in xrange(test_num):
        #in_file.readline()

        line  = in_file.readline()

        #if i == 17:
        #    print line
        # print line

        in_num = line[:-1].split(' ')[0]

        #print in_num, ' ',

        line  = in_file.readline()
        values = line[:-1].split(' ')
        #print values

        furi = []
        for j in xrange(9):
            furi.append([])

        for val in values:
            #val = int(val)
            furi[int(val[0])-1].append(int(val)) 

        max_set = 0
        for f in furi:
            if len(f) < 1:
                continue
            #elif len(f) == 1:
            #    if max_set < f[0]:
            #        max_set = f[0]
            #    continue

            #temp_max = max(f) 
            #print max(f), ' ',
            #f.remove(temp_max)
            #temp_max = temp_max + max(f)
            #print max(f), ' '

            if max_set < sum(f):
                max_set = sum(f)

        #print i, ':', max_set
        print max_set

        #print in_num
    #while line:
    #    itemList = line[:-1].split('\t')
    #    print itemList
