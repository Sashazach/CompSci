"""
Python Classes Introduction

Objects are variables that contain data and functions that can be used to manipulate the data

Functions contained in an object are called methods

Variable Stored in an object are called attributes


"""
import random as r
import math


class ball:
    # init function runs with class is created
    # self argument is always needed and automatically passed 
    def __init__(self, color, deltaTime, springConstant, mass, initialVelocity, initialPosition, startX = 2, startY = 2):
        
        # Defines the class attributes Xs and Ys
        # An attribute is a variable specific to a class
        self.Xs = [startX]
        self.Ys = [startY]

        self.deltaTime = deltaTime
        self.springConstant = springConstant
        self.mass = mass
        self.initialVelocity = initialVelocity
        self.initialPosition = initialPosition
        
        # Defines the class attribute for the color
        self.color = color
    
    # Unnecessary function that can be used to modify the class attribute "color"
    def setColor(self, color):
        self.color = color

    # Unnecessary function that can be used to get the class attribute "color"
    def getColor(self):
        return self.color

    def step(self, minVelo=5, maxVelo=100):
        deltaPosition = self.Ys[-1] - self.initialPosition

        acceleration = -self.springConstant * deltaPosition / self.mass
        self.initialVelocity += acceleration * self.deltaTime

        newYPos = self.Ys[-1] + self.initialVelocity * self.deltaTime

        self.Xs.append(self.Xs[-1] + self.deltaTime)
        self.Ys.append(newYPos)
