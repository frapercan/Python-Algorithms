# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 17:03:20 2017

@author: frapercan
"""
def solve(grades):
    for grade in grades:
        print (roundedGrade(grade))

def roundedGrade(grade):
    return (grade - (grade % 5) + 5) if needToRound(grade)  else grade 
       
def needToRound(grade):
    return True if (grade % 5 >= 3 and grade >= 38) else False