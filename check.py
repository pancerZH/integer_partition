def pentagonal_number(x):
        """使用五边形数定理计算拆分数，速度快，占用空间小"""
        num = x
        # 构建辅助数组
        assist = []
        for i in range(1, num):
            assist.append(int(i*(i*3-1)/2))
            assist.append(int(i*(i*3+1)/2))

        # 构建由1~num的拆分数列表
        p_list = [1, 1, 2]
        for i in range(3, num+1):
            count = 0
            p = 0
            for j in range(0, i):
                if assist[j] > i:
                    break
                count %= 4
                if count is 0 or count is 1:
                    p += p_list[i-assist[j]]
                else:
                    p -= p_list[i-assist[j]]
                count += 1
            p_list.append(p)
        
        return p_list[num]


def main():
    for m in range(0, 101):
        p = pentagonal_number(5*m+4)
        assert p % 5 == 0, '5*{}+4 failed!'.format(m)
        p = pentagonal_number(7*m+5)
        assert p % 7 == 0, '7*{}+5 failed!'.format(m)
        p = pentagonal_number(11*m+6)
        assert p % 11 == 0, '11*{}+6 failed!'.format(m)

        print('m={} checked'.format(m))
    print('{} to {} all checked!'.format(0, 100))

if __name__ == '__main__':
    main()