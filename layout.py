#-*- coding: UTF-8 -*-
#标题
from component import *

#矩阵A
labelA.grid(row=0,column=0)  #标签
inputA.grid(row=1,column=0)  #输入
outputA.grid(row=2,column=0) #输出
#矩阵B
labelB.grid(row=0,column=1)  #标签
inputB.grid(row=1,column=1)  #输入
outputB.grid(row=2,column=1) #输出
#数字C
frame_number.grid(row=0,column=2)
label_number.grid(row=0,column=0)
inputC.grid(row=0,column=1)
#结果
label_result.grid(row=1,column=2)
result.grid(row=2,column=2)

#按钮框架
frameA.grid(row=3,column=0)
frameB.grid(row=3,column=1)
frameC.grid(row=3,column=2)

#矩阵A的按钮
button_view_A.grid(row=0,column=0)
button_reset_A.grid(row=0,column=1)
button_scalar_multiply_A.grid(row=1,column=0)
button_transpose_A.grid(row=1,column=1)
button_inverse_A.grid(row=2,column=0)
button_companion_A.grid(row=2,column=1)
button_determinant_A.grid(row=4,column=0)
button_getTrace_A.grid(row=3,column=0)
button_rank_A.grid(row=3,column=1)
button_eigenvalue_A.grid(row=4,column=1)

#矩阵B的按钮
button_view_B.grid(row=0,column=0)
button_reset_B.grid(row=0,column=1)
button_scalar_multiply_B.grid(row=1,column=0)
button_transpose_B.grid(row=1,column=1)
button_inverse_B.grid(row=2,column=0)
button_companion_B.grid(row=2,column=1)
button_determinant_B.grid(row=4,column=0)
button_getTrace_B.grid(row=3,column=0)
button_rank_B.grid(row=3,column=1)
button_eigenvalue_B.grid(row=4,column=1)

#矩阵A和B之间的操作按钮
button_add.grid(row=0,column=0)
button_subtract.grid(row=0,column=1)
button_matrix_multiply.grid(row=1,column=0)
button_dot_multiply.grid(row=1,column=1)
button_distance.grid(row=2,column=0)

#结果按钮
button_result_as_A.grid(row=3,column=0)
button_result_as_B.grid(row=3,column=1)
button_result_as_C.grid(row=4,column=0)