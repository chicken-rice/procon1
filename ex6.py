if __name__ == '__main__':
    in_file = open('ex6test.txt', 'r')
    test_num = int(in_file.readline().strip())

    

    for i in xrange(test_num):
        word_num = int(in_file.readline().strip())
        assems = []

        for j in xrange(word_num):
            word = in_file.readline().strip()
            first_assem = []


            for ass in assems:
                if word[0] in ass:
                    first_assem = ass

            if not first_assem:
                assems.append([word[0]])
                first_assem = assems[-1]


            for c in word[1:]:
                exist_flag = False

                for ass in assems:
                    if c in ass:
                        if first_assem != ass:
                            first_assem.extend(ass)
                            assems.remove(ass)

                        exist_flag = True
                        break

                if not exist_flag:
                    first_assem.append(c)


        print assems



