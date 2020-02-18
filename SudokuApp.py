import random
from copy import deepcopy
from tkinter import * 
import time


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



def get_row_correct(game,row):
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
    rows_correct = get_row_correct(game,row)
    col_correct = get_col_correct(game,col)
    square_correct = get_square_correct(game,row,col)
    all_correct = list(set(rows_correct) & set(col_correct) & set(square_correct)) 
    return all_correct

def solve_recursive(game,row,col,viewCanvas):
    correct = get_correct(game,row,col)
    solved = False
    section_x = get_section(row)
    section_y = get_section(col)
    my_game = list(game)
    start = False
    #if col == 8:
        #update(viewCanvas)
    if my_game[section_x][row%3][section_y][col%3] != 0:
        correct = [my_game[section_x][row%3][section_y][col%3]]
        start = True
       
    if correct == []:
        return my_game, False

    else:
        for i in range(len(correct)):
            #viewCanvas.itemconfig("text"+str(row+1)+':'+str(col+1), text=str(correct[i]))
            #viewCanvas.itemconfig(str(row+1)+ ':' + str(col+1),fill='green')
            if not start:
                myBoard[row][col][0] = str(correct[i])
                
                '''if len(correct) == 1:
                                                                    myBoard[row][col][1] = 'purple'
                                                                else:'''
                myBoard[row][col][1] = 'green'
            #viewCanvas.update_idletasks()
            answer = []
            my_game[section_x][row%3][section_y][col%3] = correct[i]
            if row == 8 and col == 8:
                return my_game, True
            elif col != 8:
                answer, solved = solve_recursive(my_game,row,col+1,viewCanvas)
            elif row != 8:
                answer, solved = solve_recursive(my_game,row+1,0,viewCanvas)
            if solved == False:
                if i == len(correct)-1:
                    if not start:
                        my_game[section_x][row%3][section_y][col%3] = 0 
                        myBoard[row][col][0] = ''
                        myBoard[row][col][1] = '#ccc'
                    return my_game, False

                next
            if solved == True:
                myBoard[i][j][2] = True
                update(viewCanvas)
                return my_game, True
        

def update(viewCanvas):
    for i in range(9):
        for j in range(9):
            viewCanvas.itemconfig("text"+str(i+1)+':'+str(j+1), text=myBoard[i][j][0])
            viewCanvas.itemconfig(str(i+1)+ ':' + str(j+1),fill=myBoard[i][j][1])

    viewCanvas.update_idletasks()

game = [[
         [[5 ,0 ,0 ],[4 ,0 ,0 ],[0 ,0 ,0 ]],  
		 [[0 ,0 ,2 ],[0 ,0 ,0 ],[0 ,0 ,6 ]],
		 [[0 ,0 ,7 ],[0 ,8 ,3 ],[0 ,5 ,0 ]]
        ],
		
		[
         [[0 ,0 ,5 ],[0 ,0 ,0 ],[0 ,7 ,0 ]],  
		 [[0 ,0 ,0 ],[0 ,6 ,0 ],[8 ,3 ,0 ]],
		 [[0 ,0 ,0 ],[5 ,9 ,0 ],[0 ,6 ,0 ]]
        ],

		[
         [[9 ,2 ,0 ],[0 ,7 ,0 ],[0 ,0 ,0 ]],  
		 [[8 ,0 ,0 ],[0 ,0 ,0 ],[0 ,0 ,0 ]],
		 [[4 ,0 ,3 ],[0 ,0 ,0 ],[1 ,0 ,0 ]]
        ]]

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

#finished_game ,solved = solve_recursive(game,0,0)


print('-------------Before--------------')
for i in range(3):
	for j in range(3):
		print(start_game[i][j])
print('---------------------------------')
print('------------Completed------------')


#for i in range(3):
#	for j in range(3):
#		print(finished_game[i][j])
#print('---------------------------------')

myBoard = []


#-------------- SET UP THE WINDOW FRAME --------------------------------
class launchScreen(Frame):
    #set the initial size of the window please change width and height
    #it uses these values to determine the window size
    #if you are on a resolution that is not 1920x1080

    def __init__(self, master=None, width=0.5, height=0.4):
        Frame.__init__(self, master)
        #pack the frame to cover the whole window
        self.pack(side=TOP, fill=BOTH, expand=YES)

        # get screen width and height
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()

        w = ws*width
        h = ws*height
        # calculate position x, y
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))

        #Make the screen appear on top of everything.
        self.master.overrideredirect(True)
        self.lift()

#Once it has launched do everything in Main
if __name__ == '__main__':
    root = Tk()
    #set the title of the applicaton window
    root.title('Sudoku')


#--------------------- GAME STARTED ----------------------------------------
    def gameStart():

        print("Game Started")
        #get rid of the launch screen elemenets and show the game board
        LaunchScrn.pack_forget()

        #this is where the 20x20 grid is made
        #set up the view of the game board
        def board(view):
            w=view.winfo_width()
            h=view.winfo_height()
            gridWidth = w / 11
            gridHeight = h / 11
            rowNumber = 0
            rect_quit = view.create_rectangle(0,
                         0,
                         gridWidth ,
                         gridHeight,
                         fill = '#ff0000')
                         #Sets row, column
            view.itemconfig(rect_quit, tags="quit")
            rect_solve = view.create_rectangle(2*gridWidth,10 * gridHeight,(0 ) * gridWidth ,(10 + 1) * gridHeight,
                         fill = 'green')
                         #Sets row, column
            view.itemconfig(rect_solve, tags="solve")
            mylabel = view.create_text((  gridWidth  , 10 * gridHeight+ gridHeight/2),tags="solvetext",text="Solve")
                	

            for row in range(1,10):
                columnNumber = 0
                rowNumber = rowNumber + 1
                section_x = get_section(row-1)
                row_nums = []
                for col in range(1,10):
                    
                    fill = '#ccc'
                    text = ""
                    solved = False
                    section_y = get_section(col-1)
                    #print(start_game[section_x][(row-1)%3][section_y][(col-1)%3])
                    if start_game[section_x][(row-1)%3][section_y][(col-1)%3] != 0:
                        text = str(start_game[section_x][(row-1)%3][section_y][(col-1)%3])
                        fill = 'yellow'
                        solved = True
                    columnNumber = columnNumber + 1
                    #print(text,section_x,(row-1)%3,section_y,(col-1)%3)
                    view.create_rectangle(col * gridWidth,row * gridHeight,(col + 1) * gridWidth ,(row + 1) * gridHeight,fill = fill,tags=str(rowNumber)+":"+str(columnNumber))
                    rect = [text,fill,solved]

                    row_nums.append(rect)
                    #print(type(rect))
                    view.create_text((col * gridWidth + gridWidth/2 , row * gridHeight+ gridHeight/2),tags="text"+str(row)+':'+str(col),text=text)
                    #view.itemconfig(rect, )
                myBoard.append(row_nums)
        viewCanvas = Canvas(root, width=root.winfo_width(), height=root.winfo_height(),bg="#ddd")
        viewCanvas.pack(side=TOP, fill=BOTH,padx=1,pady=1)

        def clickOnGameBoard(event):
        	if viewCanvas.find_withtag(CURRENT):
        		if (viewCanvas.gettags(CURRENT)[0] == 'quit'):
        			root.destroy()
        			quit()
        		elif (viewCanvas.gettags(CURRENT)[0] == 'solvetext') or (viewCanvas.gettags(CURRENT)[0] == 'solve'):
        			solve_recursive(game,0,0,viewCanvas)
        		#else:
        			#viewCanvas.itemconfig(ALL, fill="#ccc")
        			#viewCanvas.itemconfig("quit", fill="#ff0000")
        			#viewCanvas.itemconfig(CURRENT, fill="yellow")
        			#viewCanvas.itemconfig("solve", fill="green")
        			#viewCanvas.itemconfig("solvetext", fill="#000000")
        			#for i in range(1,10):
        			#	for j in range(1,10):
        			#		viewCanvas.itemconfig("text"+str(i)+':'+str(j), fill="#000000")
        		viewCanvas.update_idletasks()
        #bind an event when you click on the game board
        viewCanvas.bind("<Button-1>", clickOnGameBoard)

        #update the game board after it is done being drawn.
        root.update_idletasks()
        board(viewCanvas)

        #when you click the quit button it returns you to the launch screen
        def clickToQuit(event):
        	viewCanvas.destroy()
        	label.pack_forget()
        	LaunchScrn.pack(side=TOP, fill=BOTH, expand=YES)

        
    def gameEnd():
    	def quitGame():
    		print("Game Ended")
    		LaunchScrn.after(3000,root.destroy())
    	quitGame()

#---------------------------- LAUNCH SCREEN --------------------------------------------
    LaunchScrn = launchScreen(root)
    LaunchScrn.config(bg="#eee")

    b=Button(LaunchScrn, command=gameStart)
    b.config(width="300", height="50")
    b.pack(side=RIGHT, fill=X, padx=10, pady=10)

    b=Button(LaunchScrn, command=gameEnd)
    b.config(width="300", height="50")
    b.pack(side=RIGHT, fill=X, padx=10, pady=10)

    root.mainloop()





