if __name__ == '__main__':

    in_file = open('ex4_in.txt', 'r')
    line = in_file.readline()
    test_num = int(line[:-1].split(' ')[0])

    for i in xrange(test_num):
        line = in_file.readline()
        rect_num = int(line[:-1].split(' ')[0])
        rect_list = []
        
        #print '---------------------------------------'

        for j in xrange(rect_num):
            rect_list.append([])
            line = in_file.readline()
            rect = line[:-1].split(' ')
            rect = map(int, rect)
            flag = False;
            #print rect

            for x in range(rect[1], rect[1]+rect[3]):
                rect_list[j].extend(map(lambda y: x*1000+y, range(rect[0], rect[0]+rect[2])))

            rect_list[j] = set(rect_list[j])

        for j in xrange(rect_num):
            kasanari = set()
            for k in xrange(rect_num):
                if k == j:
                    continue
                kasanari = kasanari | rect_list[k]

            sabun = rect_list[j] - kasanari
            #print 'rect', rect_list[j]
            #print 'kasanari', kasanari

            if len(sabun) == 0:
                flag = True
                break


        if flag:
            print 'TRUE'
        else:
            print 'FALSE'
        #print rect_list