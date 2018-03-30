#-*- coding: UTF-8 -*-

from numpy import *
from component import *

result_content=0

def getInput(input,output):
	output.delete(0.0,END)
	try: 
		matrix=mat(input.get()) #获得输入
		output.insert(0.0,matrix)
	except:
		output.insert(0.0,"输入的类型不是矩阵")
	return matrix
	
def getInputs():
	matrix1=getInput(inputA,outputA)
	matrix2=getInput(inputB,outputB)
	return matrix1,matrix2

def getInputNumber():
	try:
		number=float32(inputC.get())
	except:
		result.delete(0.0,END)
		result.insert(0.0,"输入的类型不是数字")
	return number

#单矩阵操作
#数乘
def scalar_multiply(input,output):
	matrix=getInput(input,output)
	number=getInputNumber()
	global result_content
	result_content=number*matrix
	result.delete(0.0,END)
	result.insert(0.0,result_content)
		
def scalar_multiply_A():
	scalar_multiply(inputA,outputA)
	
def scalar_multiply_B():
	scalar_multiply(inputB,outputB)
	
#矩阵转置
def transpose(input,output):
	matrix=getInput(input,output)
	global result_content
	result_content=matrix.T
	result.delete(0.0,END)
	result.insert(0.0,result_content)

def transpose_A():
	transpose(inputA,outputA)

def transpose_B():
	transpose(inputB,outputB)

#逆矩阵
def inverse(input,output):
	matrix=getInput(input,output)
	result.delete(0.0,END)
	m,n=shape(matrix)
	if(m!=n):
		result.insert(0.0,"这不是一个方阵")
	elif(linalg.det(matrix)==0):
		result.insert(0.0,"这是一个奇异矩阵")
	else:
		global result_content
		result_content=matrix.I
		result.insert(0.0,result_content)

def inverse_A():
	inverse(inputA,outputA)
	
def inverse_B():
	inverse(inputB,outputB)
	
#行列式
def determinant(input,output):
	matrix=getInput(input,output)
	result.delete(0.0,END)
	m,n=shape(matrix)
	if(m!=n):
		result.insert(0.0,"这不是一个方阵")
	else:
		global result_content
		result_content=float32(linalg.det(matrix))
		result.insert(0.0,result_content)

def determinant_A():
	determinant(inputA,outputA)
	
def determinant_B():
	determinant(inputB,outputB)
	
#迹
def getTrace(input,output):
	matrix=getInput(input,output)
	result.delete(0.0,END)
	m,n=shape(matrix)
	if(m!=n):
		result.insert(0.0,"这不是一个方阵")
	else:
		global result_content
		result_content=trace(matrix)
		result.insert(0.0,result_content)

def getTrace_A():
	getTrace(inputA,outputA)

def getTrace_B():
	getTrace(inputB,outputB)

#秩
def rank(input,output):
	matrix=getInput(input,output)
	result.delete(0.0,END)
	global result_content
	result_content=linalg.matrix_rank(matrix)
	result.insert(0.0,result_content)

def rank_A():
	rank(inputA,outputA)

def rank_B():
	rank(inputB,outputB)

#特征值
def eigenvalue(input,output):
	matrix=getInput(input,output)
	result.delete(0.0,END)
	m,n=shape(matrix)
	if(m!=n):
		result.insert(0.0,"这不是一个方阵")
	else:
		global result_content
		result_content=real(linalg.eigvals(matrix))
		result.insert(0.0,result_content)

def eigenvalue_A():
	eigenvalue(inputA,outputA)

def eigenvalue_B():
	eigenvalue(inputB,outputB)
	
#查看输入
def view(input,output):
	matrix=getInput(input,output)
	output.delete(0.0,END)
	output.insert(0.0,matrix)

def view_A():
	view(inputA,outputA)

def view_B():
	view(inputB,outputB)

def reset_A():
	inputA.delete(0,END)
	outputA.delete(0.0,END)

def reset_B():
	inputB.delete(0,END)
	outputB.delete(0.0,END)

#矩阵A和B之间的操作		
#加法
def add():
	matrix1,matrix2=getInputs()
	result.delete(0.0,END)
	if(shape(matrix1)!=shape(matrix2)):
		result.insert(0.0,"矩阵A和B的大小不一样")
	else:
		global result_content
		result_content=matrix1+matrix2
		result.insert(0.0,result_content)
	
#减法
def subtract():
	matrix1,matrix2=getInputs()
	result.delete(0.0,END)
	if(shape(matrix1)!=shape(matrix2)):
		result.insert(0.0,"矩阵A和B的大小不一样")
	else:
		global result_content
		result_content=matrix1-matrix2
		result.insert(0.0,result_content)

#矩阵乘法
def matrix_multiply():
	matrix1,matrix2=getInputs()
	result.delete(0.0,END)
	if(shape(matrix1)[1]!=shape(matrix2)[0]):
		result.insert(0.0,"矩阵A和B无法相乘")
	else:
		global result_content
		result_content=matrix1*matrix2
		result.insert(0.0,result_content)

#点乘
def dot_multiply():
	matrix1,matrix2=getInputs()
	result.delete(0.0,END)
	if(shape(matrix1)!=shape(matrix2)):
		result.insert(0.0,"矩阵A和B的大小不一样")
	else:
		global result_content
		result_content=multiply(matrix1,matrix2)
		result.insert(0.0,result_content)

#欧氏距离
def distance():
	matrix1,matrix2=getInputs()
	result.delete(0.0,END)
	if(shape(matrix1)!=shape(matrix2)):
		result.insert(0.0,"矩阵A和B的大小不一样")
	else:
		global result_content
		result_content=linalg.norm(matrix1-matrix2)
		result.insert(0.0,result_content)

#结果操作
def result_as_input(input):
	try:
		matrix=mat(result_content)
	except:
		result.delete(0.0,END)
		result.insert(0.0,"结果不是矩阵")
	else:
		m,n=shape(matrix)
		input.delete(0,END)
		for i in range(m):
			for j in range(n):
				input.insert(END,matrix[i,j])
				if j!=n-1: input.insert(END," ")
			if i!=m-1: input.insert(END,";")
		
def result_as_A():
	result_as_input(inputA)
	
def result_as_B():
	result_as_input(inputB)
	
def result_as_C():
	if isinstance(result_content,int) or isinstance(result_content,float32):
		inputC.delete(0,END)
		inputC.insert(0,result_content)
	else:
		result.delete(0.0,END)	
		result.insert(0.0,"结果不是数字")

#伴随矩阵
def companion(input,output):
	matrix=getInput(input,output)
	m,n=shape(matrix)
	result.delete(0.0,END)
	if m!=n:
		result.insert(0.0,"这不是一个方阵")
	else:
		comp=[]
		for i in range(m):
			temp_comp=[]
			temp_matrix=delete(matrix,i,axis=0)  #删除行
			for j in range(n):
				Mij=delete(temp_matrix,j,axis=1) #删除列
				Mij_det=linalg.det(Mij)
				sign=(i+j)&1
				if sign==0: temp_comp.append(Mij_det)
				else: temp_comp.append(-Mij_det)
			comp.append(temp_comp)
		global result_content
		result_content=mat(comp)
		result.insert(0.0,result_content)

def companion_A():
	companion(inputA,outputA)

def companion_B():
	companion(inputB,outputB)

