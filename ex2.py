if __name__ == '__main__':
    in_file = open('ex2test.txt', 'r')
    line = in_file.readline()
    test_num = int(line[:-1].split(' ')[0])

    for i in xrange(test_num):
        line  = in_file.readline()
        test = '\xe2\x80\x99'
        #print test
        hannin = line[:-1].replace(test, 'a').split(' ')
        #print hannin
        #hannin = hannin.split(' ')
        #hannin.replace('\'', 'a')
        hannin_len = map(len, hannin)
        #print hannin_len
        #print hannin
        #print hannin_len
        hannin_ave = float(sum(hannin_len)) / len(hannin)

        line  = in_file.readline()
        yougi_num = int(line[:-1].split(' ')[0])
        yougi_dict = {}

        for j in xrange(yougi_num):
            line  = in_file.readline()

            yougi_set = line[:-1].replace(test, 'a').split(':')
            print yougi_set
            yougi_len = map(len, yougi_set[1].split(' ')[1:])
            print yougi_len
            yougi_ave = float(sum(yougi_len)) / len(yougi_len)

            yougi_dict[yougi_set[0]] = yougi_ave

        #print yougi_dict

        yougi = 'def'
        min_sub = 10
        for k, v in yougi_dict.iteritems():
            if min_sub > abs(v-hannin_ave):
                yougi = k
                min_nub = abs(v-hannin_ave)

        print yougi 