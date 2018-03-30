#-*- coding: UTF-8 -*-
from implement import *

root.title("Matrix Calculator")  #标题

#数字C
frame_number.config(width=30)
label_number.config(text="数字C")
#结果
label_result.config(text="结果")
result.config(width=30,height=20)
#按钮框架
frameA.config(width=10,height=10)
frameB.config(width=10,height=10)
frameC.config(width=10,height=10)

#矩阵A
labelA.config(text="矩阵A")
inputA.config(width=30)
outputA.config(width=30,height=20)
button_scalar_multiply_A.config(command=scalar_multiply_A,text="数乘",width=15)
button_transpose_A.config(command=transpose_A,text="转置",width=15)
button_inverse_A.config(command=inverse_A,text="逆矩阵",width=15)
button_determinant_A.config(command=determinant_A,text="行列式",width=15)
button_getTrace_A.config(command=getTrace_A,text="迹",width=15)
button_rank_A.config(command=rank_A,text="秩",width=15)
button_eigenvalue_A.config(command=eigenvalue_A,text="特征值",width=15)
button_view_A.config(command=view_A,text="查看",width=15)
button_reset_A.config(command=reset_A,text="重置",width=15)
button_companion_A.config(command=companion_A,text="伴随矩阵",width=15)

#矩阵B
labelB.config(text="矩阵B")
inputB.config(width=30)
outputB.config(width=30,height=20)
button_scalar_multiply_B.config(command=scalar_multiply_B,text="数乘",width=15)
button_transpose_B.config(command=transpose_B,text="转置",width=15)
button_inverse_B.config(command=inverse_B,text="逆矩阵",width=15)
button_determinant_B.config(command=determinant_B,text="行列式",width=15)
button_getTrace_B.config(command=getTrace_B,text="迹",width=15)
button_rank_B.config(command=rank_B,text="秩",width=15)
button_eigenvalue_B.config(command=eigenvalue_B,text="特征值",width=15)
button_view_B.config(command=view_B,text="查看",width=15)
button_reset_B.config(command=reset_B,text="重置",width=15)
button_companion_B.config(command=companion_B,text="伴随矩阵",width=15)

#矩阵A和B之间的操作
button_add.config(command=add,text="+",width=15)
button_subtract.config(command=subtract,text="-",width=15)
button_matrix_multiply.config(command=matrix_multiply,text="矩阵乘",width=15)
button_dot_multiply.config(command=dot_multiply,text="点乘",width=15)
button_distance.config(command=distance,text="距离",width=15)

#结果操作
button_result_as_A.config(command=result_as_A,text="结果输入A",width=15)
button_result_as_B.config(command=result_as_B,text="结果输入B",width=15)
button_result_as_C.config(command=result_as_C,text="结果输入C",width=15)