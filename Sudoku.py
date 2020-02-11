import random
from copy import deepcopy
from tkinter import * 
def get_section(row):
	"""
	Reurns: int representing list palcement
	Parms: row - int representing row
	"""
	if (row<=2):
		return 0
	elif (row<=5):
		return 1
	else:
		return 2

def check_row(game,row,number):
	"""
	Returns: true if number not already in row
			 false if number is already in row 
	Params: game - the game board
			row - the row to check
			number - the number to check against the row
	"""
	section = get_section(row)
	for i in range(3):
		#print(game[section][row%3][i])
		if number in game[section][row%3][i]:
			return False		
	return True

def check_col(game,col,number):
	"""
	Returns: true if number not already in col
			 false if number is already in col 
	Params: game - the game board
			col - the col to check
			number - the number to check against the col
	"""
	section = get_section(col)
	for i in range(3):
		for j in range(3):
			#print(game[i][j][section][col%3])
			if number == game[i][j][section][col%3]:
				return False
	return True

def check_square(game,row,col,number):
	"""
	Returns: true if number not already in square
			 false if number is already in square 
	Params: game - the game board
			square - the square to check
			number - the number to check against the square
	"""
	section_row = get_section(row)
	section_col = get_section(col)
	for i in range(3):
		#print(game[section_row][i][section_col])
		if number in game[section_row][i][section_col]:
			return False
	return True
		
def check_number(game,row,col,number):
	"""
	Returns: true if number satisfies row,col, and square
			 false if number does not satisfy
	Params: game - the game board
			row - the row to check
			col - the col to check
			number - the number to check against
	"""
	if check_row(game,row,number) and check_col(game,col,number) and check_square(game,row,col,number):
		return True
	return False

def get_row_correct(game,row):
	"""
	Returns: list with all correct number choices
	Params: game - the game board
			row - the row to check
	"""
	section = get_section(row)
	correct = []
	row_numbers = []
	for i in range(3):
		for j in range(3):
			row_numbers.append(game[section][row%3][i][j])
	for number in range(1,10):
		if number not in row_numbers:
			correct.append(number)		
	return correct

def get_col_correct(game,col):
	"""
	Returns: list with all correct number choices
	Params: game - the game board
			col - the col to check
	"""
	section = get_section(col)
	correct = []
	col_numbers = []
	for i in range(3):
			for j in range(3):
				#print(game[i][j][section][col%3])
				col_numbers.append(game[i][j][section][col%3])
	for number in range(1,10):
		if number not in col_numbers:
			correct.append(number)
	return correct

def get_square_correct(game,row,col):
	"""
	Returns: list with all correct number choices
	Params: game - the game board
			row - the row to check
			col - the col to check
	"""
	section_row = get_section(row)
	section_col = get_section(col)
	correct = []
	square_numbers = []
	for i in range(3):
		for j in range(3):
			square_numbers.append(game[section_row][i][section_col][j])
	for number in range(1,10):
		if number not in square_numbers:
			correct.append(number)
	return correct

def get_correct(game,row,col):
	"""
	Returns: list with the union of all correct number choices 
	Params: game - the game board
			row - the row to check
			col - the col to check
	"""
	rows_correct = get_row_correct(game,row)
	col_correct = get_col_correct(game,col)
	square_correct = get_square_correct(game,row,col)
	all_correct = list(set(rows_correct) & set(col_correct) & set(square_correct)) 
	return all_correct


def solve_recursive(game,row,col):
	"""
	Returns: the solved board
	Params: game - the game board
			row - the row to check
			col - the col to check
	"""
	correct = get_correct(game,row,col)
	solved = False
	section_x = get_section(row)
	section_y = get_section(col)
	my_game = list(game)
	start = False
	if my_game[section_x][row%3][section_y][col%3] != 0:
		correct = [my_game[section_x][row%3][section_y][col%3]]
		start = True


	if correct == []:
		return my_game, False
	else:
		for i in range(len(correct)):
			answer = []
			my_game[section_x][row%3][section_y][col%3] = correct[i]
			if row == 8 and col == 8:
				return my_game, True
			elif col != 8:
				answer, solved = solve_recursive(my_game,row,col+1)
			elif row != 8:
				answer, solved = solve_recursive(my_game,row+1,0)
			if solved == False:
				if i == len(correct)-1:
					if not start:
						my_game[section_x][row%3][section_y][col%3] = 0 
					return my_game, False			
				next
			if solved == True:
				return my_game, True

game = [[[[5 ,0 ,0 ],[4 ,0 ,0 ],[0 ,0 ,0 ]],  
		 [[0 ,0 ,2 ],[0 ,0 ,0 ],[0 ,0 ,6 ]],
		 [[0 ,0 ,7 ],[0 ,8 ,3 ],[0 ,5 ,0 ]]],
		
		[[[0 ,0 ,5 ],[0 ,0 ,0 ],[0 ,7 ,0 ]],  
		 [[0 ,0 ,0 ],[0 ,6 ,0 ],[8 ,3 ,0 ]],
		 [[0 ,0 ,0 ],[5 ,9 ,0 ],[0 ,6 ,0 ]]],

		[[[9 ,2 ,0 ],[0 ,7 ,0 ],[0 ,0 ,0 ]],  
		 [[8 ,0 ,0 ],[0 ,0 ,0 ],[0 ,0 ,0 ]],
		 [[4 ,0 ,3 ],[0 ,0 ,0 ],[1 ,0 ,0 ]]]]

start_game = deepcopy(game)

'''game = [[[[1 ,2 ,3 ],[4 ,5 ,6 ],[7 ,8 ,9 ]],  
		 [[10,11,12],[13,14,15],[16,17,18]],
		 [[19,20,21],[22,23,24],[25,26,27]]],
		
		[[[28,29,30],[31,32,33],[34,35,36]],  
		 [[37,38,39],[40,41,42],[43,44,45]],  
		 [[46,47,48],[49,50,51],[52,53,54]]],

		[[[55,56,57],[58,59,60],[61,62,63]],  
		 [[64,65,66],[67,68,69],[70,71,72]],  
		 [[73,74,75],[76,77,78],[79,80,81]]]]'''

finished_game ,solved = solve_recursive(game,0,0)


print('-------------Before--------------')
for i in range(3):
	for j in range(3):
		print(start_game[i][j])
print('---------------------------------')
print('------------Completed------------')


for i in range(3):
	for j in range(3):
		print(finished_game[i][j])
print('---------------------------------')


