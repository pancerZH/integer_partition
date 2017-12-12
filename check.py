def dynamic(x):
    """使用动态规划的方法找到拆分数，速度快，占用空间大"""
    num = x
    table = [[0 for m in range(num)] for n in range(num)] # 构建动态规划表格
    for n in range(num):
        for m in range(num):
            if n is 0 or m is 0:
                table[n][m] = 1
            elif n <= m:
                table[n][m] = table[n][n-1]+1
            else:
                table[n][m] = table[n][m-1]+table[n-m-1][m]
    return table[-1][-1]


def main():
    for m in range(0, 101):
        p = dynamic(5*m+4)
        assert p % 5 == 0, '5*{}+4 failed!'.format(m)
        p = dynamic(7*m+5)
        assert p % 7 == 0, '7*{}+5 failed!'.format(m)
        p = dynamic(11*m+6)
        assert p % 11 == 0, '11*{}+6 failed!'.format(m)

        print('m={} checked'.format(m))
    print('{} to {} all checked!'.format(0, 100))

if __name__ == '__main__':
    main()