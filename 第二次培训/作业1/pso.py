# -*- coding:utf-8 -*-
#https://github.com/EddyGao/PSO
import numpy as np
import matplotlib.pyplot as plt
import math

def getweight():
    # 惯性权重
    weight = 1
    return weight

def getlearningrate():
    # 分别是粒子的个体和社会的学习因子，也称为加速常数
    lr = (0.49445,1.49445)
    return lr

def getmaxgen():
    # 最大迭代次数
    maxgen = 300 # 最多迭代300次
    return maxgen

def getsizepop():
    # 种群规模
    sizepop = 50 #派出50个粒子
    return sizepop

def getrangepop():
    # 粒子的位置的范围限制,x、y方向的限制相同
    rangepop = (-2*math.pi , 2*math.pi) #粒子允许的活动范围
    #rangepop = (-2,2)
    return rangepop

def getrangespeed():
    # 粒子的速度范围限制
    rangespeed = (-0.5,0.5) 
    return rangespeed

def func(x):
    """
    计算粒子的目标函数值
    - x : 当前粒子的位置坐标 [x, y]。
    - y : 计算出的适应度值。
    """
    # x输入粒子位置
    # y 粒子适应度值
    if (x[0]==0)&(x[1]==0):
        y = np.exp((np.cos(2*np.pi*x[0])+np.cos(2*np.pi*x[1]))/2)-2.71289
    else:
        y = np.sin(np.sqrt(x[0]**2+x[1]**2))/np.sqrt(x[0]**2+x[1]**2)+np.exp((np.cos(2*np.pi*x[0])+np.cos(2*np.pi*x[1]))/2)-2.71289
    return y

def initpopvfit(sizepop):
    """
    负责生成初始的粒子群位置、速度，并计算目标函数值。
    运作流程：
      创建全零矩阵 pop(位置), v(速度), fitness(得分)。
      遍历每一个粒子，随机生成位置和速度。
      将生成的粒子传入 func() 计算得分。
    依赖关系：
      依赖全局变量 rangepop 来确定随机范围。
      依赖外部函数 func() 来计算适应度。
    """
    pop = np.zeros((sizepop,2))
    v = np.zeros((sizepop,2))
    fitness = np.zeros(sizepop)

    for i in range(sizepop):
        pop[i] = [(np.random.rand()-0.5)*rangepop[0]*2,(np.random.rand()-0.5)*rangepop[1]*2]
        v[i] = [(np.random.rand()-0.5)*rangepop[0]*2,(np.random.rand()-0.5)*rangepop[1]*2]
        fitness[i] = func(pop[i])
    return pop,v,fitness

def getinitbest(fitness,pop):
    """
    找出全局最优，以及个体最优。
    运作流程：
      找出 fitness 数组中最大的值及其索引，确定全局最优 gbest。
      将当前的 fitness 数组复制给 pbestfitness（因为是第一代，当前就是历史最好）。
      将当前的 pop 位置矩阵复制给 pbestpop。
    依赖关系：
      依赖输入参数 fitness 和 pop。
    重要变量：
      gbestpop, gbestfitness:局部函数，它们存储的是全局最优状态，后续会被主循环更新。
      pbestpop, pbestfitness:局部函数，作为容器返回，主循环会将它们转化为全局状态持续追踪。
    """
    # 群体最优的粒子位置及其适应度值
    gbestpop,gbestfitness = pop[fitness.argmax()].copy(),fitness.max()
    #个体最优的粒子位置及其适应度值,使用copy()使得对pop的改变不影响pbestpop，pbestfitness类似
    pbestpop,pbestfitness = pop.copy(),fitness.copy()

    return gbestpop,gbestfitness,pbestpop,pbestfitness  

w = getweight()
lr = getlearningrate()
maxgen = getmaxgen()
sizepop = getsizepop()
rangepop = getrangepop()
rangespeed = getrangespeed()

pop,v,fitness = initpopvfit(sizepop)
gbestpop,gbestfitness,pbestpop,pbestfitness = getinitbest(fitness,pop)

result = np.zeros(maxgen)
for i in range(maxgen):
        t=0.5
        #速度更新
        for j in range(sizepop):
            v[j] += lr[0]*np.random.rand()*(pbestpop[j]-pop[j])+lr[1]*np.random.rand()*(gbestpop-pop[j])
        v[v<rangespeed[0]] = rangespeed[0]
        v[v>rangespeed[1]] = rangespeed[1]

        #粒子位置更新
        for j in range(sizepop):
            #pop[j] += 0.5*v[j]
            pop[j] = t*(0.5*v[j])+(1-t)*pop[j]
        pop[pop<rangepop[0]] = rangepop[0]
        pop[pop>rangepop[1]] = rangepop[1]

        #适应度更新
        for j in range(sizepop):
            fitness[j] = func(pop[j])

        for j in range(sizepop):
            if fitness[j] > pbestfitness[j]:
                pbestfitness[j] = fitness[j]
                pbestpop[j] = pop[j].copy()

        if pbestfitness.max() > gbestfitness : #更新pbest and gbest
            gbestfitness = pbestfitness.max()
            gbestpop = pop[pbestfitness.argmax()].copy()

        result[i] = gbestfitness


plt.plot(result)
plt.show()