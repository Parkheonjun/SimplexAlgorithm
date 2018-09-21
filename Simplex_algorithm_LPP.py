# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 20:59:47 2018

@ author: Heonjun Park
@ Main  : Simplex method for LPP
@ Description : This is the module for simplex method of LPP.
    Input : 
        matrix : list or array type simplex tableau.
                - coefficients of the standard form of LPP)
        basic  : Subscript of basic variables of LPP.
    Output :
        maximum value and solution.
    

@ Example : 
    Consider the LPP:
        max     Z = 6x_1 + 5x_2
        sub to.     2x_1 - 3x_2 <= 5
                     x_1 + 3x_2 <= 11
                    4x_1 +  x_2 <= 15
                     x_1, x_2 >= 0.
                     
    Then the standard form of LPP is
        max     Z - 6x_1 - 5x_2 + 0x_3 + 0x_4 + 0x_5 = 0
        sub to.     2x_1 - 3x_2 + 1x_3 + 0x_4 + 0x_5 = 5
                     x_1 + 3x_2 + 0x_3 + 1x_4 + 0x_5 = 11
                    4x_1 +  x_2 + 0x_3 + 0x_4 + 1x_5 = 15
                     x_1, x_2, x_3, x_4, x_5 >= 0.
        The basic variables = x_3, x_4, x_5.
        
    Input : 
        Enter the number of rows of Simplex Tableau :
        4
        
        Enter the Simplex Tableau(list type) :
        -6 -5 0 0 0 0
        2 -3 1 0 0 5
        1 3 0 1 0 11
        4 1 0 0 1 15
        
        Enter the basic variables (list type) :
        3 4 5
        
    Output : 
        max Z = 349/11
        maximized at  
        x 1 = 34/11
        x 2 = 29/11
        x 3 = 74/11
        x 4 = 0
        x 5 = 0
"""
import numpy as np
from fractions import Fraction

def equiv_set_equations(matrix, entered_num, exited_num):
    m = matrix.shape[0]
    coef = [[0]*m]*m 
    coef = np.array(coef) + Fraction()
    for i in range(m):
        if i == exited_num:
            coef[i,i] = Fraction(1,1)/matrix[i,entered_num]
        else:
            coef[i,i] = Fraction(1,1)
            coef[i,exited_num] = -matrix[i,entered_num]/matrix[exited_num,entered_num]
    return(np.dot(coef + Fraction() ,matrix))


def simplex(matrix, basic):
    matrix = np.array(matrix)
    m,n = matrix.shape
    matrix = matrix + Fraction()
    while True:
        cost_min = min(matrix[0,:-1])
        if cost_min <0:
            entered_num = list(matrix[0,:-1]).index(cost_min)
            temp = np.where(matrix[:,entered_num]>=0)
            br_crs = matrix[temp[0],n-1]/matrix[temp[0],entered_num]
            exited_num = temp[0][np.argmin(br_crs)]
        
            basic[exited_num-1] = entered_num +1
        
            matrix = equiv_set_equations(matrix,entered_num, exited_num)
        else:
            break
    solution = [0]*(n-1)
    solution = np.array(solution) + Fraction()
    solution[np.array(basic)-1] = matrix[1:,-1] 
    
    print("max Z  =", matrix[0,-1])
    print("maxizied at ")
    j=1
    for i in solution:
        print("x",j,"=",i)
        j = j+1
    

if __name__ == '__main__':
    print("Enter the number of rows of Simplex Tableau :")
    m = int(input())
    print("Enter the Simplex Tableau(list type) :")    
    matrix=[]
    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))
    print("Enter the basic variables (list type) :")    
    basic = list(map(int, input().rstrip().split()))
    simplex(matrix,basic)
    
    
