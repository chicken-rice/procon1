if __name__ == '__main__':
    in_file = open('ex3test.txt', 'r')
    line = in_file.readline()
    test_num = int(line[:-1].split(' ')[0])

    for i in xrange(test_num):
        line  = in_file.readline()
        c_num = int(line[:-1].split(' ')[0])

        #if i == 8:
        #    print line
        line  = in_file.readline()
        cards = line[:-1]

        #if i == 8:
         #   print line

        score = []

        for j in xrange(c_num):
            score.append(0)

        turn = 0;
        flag = 'N'
        last_score = score[:]

        for card in cards:
            if card.isdigit():
                if flag == 'N':
                    score[turn] = score[turn] + int(card)
                elif flag == 'X':
                    score[turn] = score[turn] * int(card)
                elif flag == 'D':
                    score[turn] = int(float(score[turn]) / int(card))
                elif flag == 'S':
                    score[turn] = score[turn] - int(card)
                if (turn + 1) / c_num == 1:
                    last_score = score[:]
                turn = (turn + 1) % c_num
                flag = 'N';

            elif flag == 'N':
                flag = card

        print max(last_score)