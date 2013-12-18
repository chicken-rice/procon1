from collections import Counter

if __name__ == '__main__':
    in_file = open('ex9test.txt', 'r')
    line = in_file.readline()
    test_num = int(line[:-1].split(' ')[0])

    alpha_max = ord('z') - ord('a') + 1

    for i in xrange(test_num):
        src  = list(in_file.readline()[:-1])
        dist = list(in_file.readline()[:-1])
        impossible = False
        count = 0

        src_dup = [key for key,val in Counter(src).items() if val > 1]
        dist_dup = [key for key,val in Counter(dist).items() if val > 1]


        for s_dup in src_dup:
            for j in xrange(len(src)):
                if src[j] == s_dup and dist[j] != dist[src.index(s_dup)]:
                    impossible = True

        for d_dup in dist_dup:
            for j in xrange(len(src)):
                if dist[j] == d_dup and src[j] != src[dist.index(d_dup)]:
                    src[j] = src[dist.index(d_dup)]
                    count += 1

        if len(set(src)) == alpha_max:
            impossible = True

        check = [False] * alpha_max

        for j in set(src):
            if j == dist[src.index(j)]:
                continue

            mark = j
            loop_flag = False
            while dist[src.index(mark)] in src:
                if check[ord(mark)-ord('a')]:
                    if loop_flag:
                        count += 1
                    break
                else:
                    check[ord(mark)-ord('a')] = True
                    count += 1
                    mark = dist[src.index(mark)]
                    loop_flag = True

            if dist[src.index(mark)] not in src:
                check[ord(mark)-ord('a')] = True
                count += 1

        if impossible:
            print 'impossible'
        else:
            print count