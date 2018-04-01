#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 18:58:02 2017

@author: ewen
"""

A = [[2,2,-3],[-2,-1,-3],[6,4,4]]
Y = [[2],[-5],[16]]

def recherchePivot(A,j):
    n = len(A)
    imax = j
    maxx = abs(A[j][j])
    for k in range(j+1,n):
        maxx = abs(A[k][j])
        imax = k
    return imax

def echange(A,i,j):
    nc = len(A[0])
    for k in range(nc):
        tmp = A[j][k]
        A[j][k] = A[i][k]
        A[i][k] = tmp

def transvect(A,i,j,mu):
    nc = len(A[0])
    for k in range(nc):
        A[i][k] = A[i][k] + mu*A[j][k]

def resolve(A,Y):
    n = len(A)
    for j in range(n):
        imax = recherchePivot(A, j)
        echange(A,j,imax)
        echange(Y,j,imax)
        for k in range(j+1,n):
            mu = -A[k][j]/A[j][j]
            transvect(A,k,j,mu)
            transvect(Y,k,j,mu)
    X = [0]*n
    for i in range(n-1,-1,-1):
        for k in range(i+1,n):
            Y[i][0] = Y[i][0] - A[i][k]*X[k]
        X[i] = round(Y[i][0]/A[i][i])
    return X

print("Les solutions du systeme sont:",resolve(A,Y))