import random
 
#生成随机列表 start和stop分别代表所需要列表元素的大小范围，length代表列表的长度
def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list
 
def main():
    N = 1000
    A = random_int_list(-20, 20, N)
    # print(A)
    maxsum = MAXSUBSEQSUM1(A, N)
    maxsum2= MAXSUBSEQSUM2(A, N)
    maxsum3= MAXSUBSEQSUM3(A, N)
    #分别用三种算法实现并输出结果
    print(maxsum)
    print(maxsum2)
    print(maxsum3)
 
#用最基础的方法来实现最大子列和，算法复杂度O（N*N*N）
def MAXSUBSEQSUM1(A, N):
    ThisSum, MaxSum = 0, 0
    for i in range(N): #i代表子列的左端位置
        for j in range(i, N):#j代表子列的左端位置
            ThisSum = 0   #ThisSum是从A[I]到A[J]的子列和
            for k in range(i, j+1):
                ThisSum += A[k]
                if ThisSum > MaxSum: #如果刚得到的这个子列和更大
                    MaxSum = ThisSum  #则更新结果
    return MaxSum
#在上面那个算法做了一些修改使算法复杂度降低，算法复杂度O（N*N）
def MAXSUBSEQSUM2(A, N):
    ThisSum, MaxSum = 0, 0
    for i in range(N):
        ThisSum = 0
        for j in range(i, N):
            ThisSum += A[j] #只在前一个和上增加一个元素得到新的和
            if ThisSum > MaxSum:
                MaxSum = ThisSum
    return MaxSum
 
#在线处理算法 复杂度O（N*logN）
def MAXSUBSEQSUM3(A, N):
    ThisSum, MaxSum = 0, 0
    for i in range(N):
        ThisSum += A[i]  #向右累加
        if ThisSum > MaxSum:
             MaxSum = ThisSum  #发现更大和则更新当前结果
        elif ThisSum<0:   #如果当前子列和为负数
            ThisSum=0     #则不可能使后面的部分和增大，则该抛弃掉
    return MaxSum
 
main()