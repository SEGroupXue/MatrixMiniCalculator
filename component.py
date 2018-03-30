#-*- coding: UTF-8 -*-

from Tkinter import *
root = Tk()

#矩阵A
labelA=Label(root)             #标签
inputA=Entry(root)             #输入框
outputA=Text(root)             #输出


#矩阵B
labelB=Label(root)             #标签
inputB=Entry(root)             #输入框
outputB=Text(root)             #输出


#数字C
frame_number=Frame(root)
label_number=Label(frame_number)
inputC=Entry(frame_number)


#结果
label_result=Label(root)
result=Text(root)


#按钮
frameA=Frame(root)
frameB=Frame(root)
frameC=Frame(root)

#矩阵A的操作
button_view_A=Button(frameA)
button_reset_A=Button(frameA)
button_scalar_multiply_A=Button(frameA)
button_transpose_A=Button(frameA)
button_inverse_A=Button(frameA)
button_determinant_A=Button(frameA)
button_getTrace_A=Button(frameA)
button_rank_A=Button(frameA)
button_eigenvalue_A=Button(frameA)
button_companion_A=Button(frameA)

#矩阵B的操作
button_view_B=Button(frameB)
button_reset_B=Button(frameB)
button_scalar_multiply_B=Button(frameB)
button_transpose_B=Button(frameB)
button_inverse_B=Button(frameB)
button_determinant_B=Button(frameB)
button_getTrace_B=Button(frameB)
button_rank_B=Button(frameB)
button_eigenvalue_B=Button(frameB)
button_companion_B=Button(frameB)

#矩阵A和B之间的操作
button_add=Button(frameC)
button_subtract=Button(frameC)
button_matrix_multiply=Button(frameC)
button_dot_multiply=Button(frameC)
button_distance=Button(frameC)

#结果操作
button_result_as_A=Button(frameC)
button_result_as_B=Button(frameC)
button_result_as_C=Button(frameC)
