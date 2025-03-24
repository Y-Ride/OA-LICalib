import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation as R

os.chdir(os.path.dirname(__file__))
data = pd.read_csv("take2/calib_result.csv", header=0, delimiter=',')

# print(data['iteration_step'].values)
# print(data.iloc[-1:])

t_vect = data.iloc[-1][['p_IinL.x', 'p_IinL.y', 'p_IinL.z']].values
print("Translation vector:")
print(t_vect)

q_vect = data.iloc[-1][['q_ItoL.x', 'q_ItoL.y', 'q_ItoL.z', 'q_ItoL.w']].values
print("Quaternion vector:")
print(q_vect)

r = R.from_quat(q_vect)
print("Rotation matrix:")
print(r.as_matrix())
