#python 3.0
#coding:UTF-8
'''
@author Yongjun Chen 06/01/2017
'''
# Implement 3d version of Dense Transformer Layer

import numpy as np
import tensorflow as tf
from Image_show import *
from transformation_tests_func import *
import h5py

if __name__ == "__main__":
    test = Transformation_Tests()
    test.Affine_test(10,2,2,2,10,1,'Affine','default')
    test.TPS_test(10, 5, 5, 5, 3, 10, 1, 'Coordinates','default')