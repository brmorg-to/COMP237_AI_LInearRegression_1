#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 12:45:57 2021

@author: brunomorgado
"""


#Import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt


#Set the seed to the pseudo-random generator
np.random.seed(98)

#Sample 100 numbers from a uniform distribution
x = np.random.uniform(-10, 10.1, 100)
print(x)

#Predicted variable whose value is given by ythe linear equation below
y = [12*i-4 for i in x]
print(y)

#Plot a Scatter plot of X vs Y
plt.scatter(x, y, alpha=0.5)
plt.title("Scatter Plot (X vs Y)")
plt.xlabel("X")
plt.ylabel("y")


#Generate noise from standard normal distribution
np.random.seed(98)
noise = np.random.normal(50, 10, 100)

print(noise)

#Creating a new list of predicted variables based on lists y and noise
y_noise = [a + b for a, b in zip(y, noise)]

#Print lists
print(y)
print()
print(noise)
print()
print(y_noise)

#Scatter plot of X vs Y_noise
plt.scatter(x, y_noise, alpha=0.5)
plt.title("Scatter Plot (X vs Y_noise)")
plt.xlabel("X")
plt.ylabel("y_noise")
