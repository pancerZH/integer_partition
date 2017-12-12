import time

class Integer_Partition(object):
    """
    这是一个整数拆分类，提供不同的拆分方法\n
    具体关系式为：
        q(n, m) = {  
            1  n=1 or m=1\n
            q(n, n)  n<m\n
            1+q(n, n-1)  n=m\n
            q(n, m-1)+1(n-m, m)  n>m  
        }
    """
    def __init__(self, x):
        self.x = x

    def recursion_drive(self):
        """使用递归的方法找到拆分数，速度慢，占用栈空间大"""
        num = self.x
        return self.recursion(num, num)

    def recursion(self, n, m):
        """具体的递归函数"""
        if n is 1 or m is 1:
            return 1
        elif n <= m:
            return self.recursion(n, n-1)+1
        else:
            return self.recursion(n, m-1)+self.recursion(n-m, m)
    
    def dynamic(self):
        """使用动态规划的方法找到拆分数，速度快，占用空间大"""
        num = self.x
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

    def generating(self):
        """使用母函数的方法找到拆分数，速度快，占用空间小"""
        num = self.x
        poly1 = [1 for i in range(num+1)]
        poly2 = [0 for i in range(num+1)]
        for i in range(2, num+1): # 多项式代表的数字范围：[2, num]
            for j in range(num+1): # 遍历poly1中每个项的幂j
                for k in range(0, num+1-j, i):
                    # 对于poly1中给定的幂j，poly2中提供的幂不得超过num-j
                    poly2[k+j] += poly1[j] # 幂为k+j的项的系数增加1*poly1[j]
            poly1 = poly2 # 将poly2中的计算结果转存到poly1中
            poly2 = [0 for i in range(num+1)]
        return poly1[num]

def main():
    while(1):
        x = input('Enter the target integer(0 to quit): ')
        if int(x) <= 0:
            break
        intPart = Integer_Partition(int(x))

        print('\nDealing way\t\tCPU time')
        if int(x) <= 80:
            start = time.clock()
            p = intPart.recursion_drive()
            end = time.clock()
            time1 = end-start
            print('Recursion:\t\t{} s'.format(time1))
        else:
            print('Recursion:\t\ttoo long!')
        
        start = time.clock()
        p1 = intPart.dynamic()
        end = time.clock()
        time2 = end-start
        print('Dynamic planning:\t{} s'.format(time2))

        start = time.clock()
        p2 = intPart.generating()
        end = time.clock()
        time3 = end-start
        print('Generating function:\t{} s'.format(time3))

        assert p1 == p2
        print('\np({}) = {}'.format(x, p1))

if __name__ == '__main__':
    main()