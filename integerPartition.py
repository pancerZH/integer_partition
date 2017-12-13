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
        # 两个多项式相乘，poly1存放最终结果，poly2存放中间结果
        poly1 = [1 for i in range(num+1)]  # 现在代表g(x, 1)
        poly2 = [0 for i in range(num+1)]
        for i in range(2, num+1): # g(x, i)中i的范围：[2, num]
            for j in range(num+1): # 遍历poly1中的每个项
                for k in range(0, num+1-j, i):
                    # 对于poly1中给定的幂j，g(x, i)中提供的项的幂不得超过num-j
                    poly2[k+j] += poly1[j] # 幂为k+j的项的系数增加1*poly1[j]
            poly1 = poly2 # 将poly2中的计算结果转存到poly1中
            poly2 = [0 for i in range(num+1)]
        return poly1[num]

    def pentagonal_number(self):
        """使用五边形数定理计算拆分数，速度快，占用空间小"""
        num = self.x
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

        if int(x) <= 2000:
            start = time.clock()
            p2 = intPart.generating()
            end = time.clock()
            time3 = end-start
            print('Generating function:\t{} s'.format(time3))
            assert p1 == p2
        else:
            print('Generating function:\ttoo long!')

        start = time.clock()
        p3 = intPart.pentagonal_number()
        end = time.clock()
        time4 = end-start
        print('Pentagonal number:\t{} s'.format(time4))
        assert p3 == p1

        print('\np({}) = {}'.format(x, p1))

if __name__ == '__main__':
    main()