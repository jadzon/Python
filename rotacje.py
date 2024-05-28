import warnings
import math
import sys
import numpy as np

def rotX(a):
    return np.array([
        [1,0,0],
        [0,math.cos(a),-math.sin(a)],
        [0,math.sin(a),math.cos(a)]
    
    ])
def rotY(a):
    return np.array([
        [math.cos(a),0,math.sin(a)],
        [0,1,0],
        [-math.sin(a),0,math.cos(a)]
    
    ])
def rotZ(a):
    return np.array([
        [math.cos(a),-math.sin(a),0],
        [math.sin(a),math.cos(a),0],
        [0,0,1]
    
    ])