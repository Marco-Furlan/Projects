from game import *
import tkinter as tk
from functools import partial

# random.seed(32)
# random.seed(45)

c = 40 # cell size in pixel

H = int(c * n_row * 1.7)
W = int(c * n_col * 1.275)

root = tk.Tk()
IMG = tk.PhotoImage(width=1, height=1) # trick to set width and height in pixels
root.title("Minesweeper")
root.geometry(f"{W}x{H}")

game = Game()

def restart():
    global game
    del game
    game = Game()
    for x in range(n_row):
        for y in range(n_col):
            buttons[x][y].configure(bg = 'WHITE', text=" ")
    button_smily.configure(bg = 'GRAY', text = ':)')
    button_count.configure(text = f'0/{n_mines}')
    button_SAT_arrow.grid_forget()
    board_state('normal')
    button_SAT.configure(text=">SAT<", command = SAT_step)

def recolor(i,j):
    if game.marked[i][j]:
        None
    elif game.mine_count[i][j] == 'M':
        for x in range(n_row):
            for y in range(n_col):
                if game.mine_count[x][y] == 'M':
                    buttons[x][y].configure(bg = "RED", text = 'X')
    elif game.mine_count[i][j] == 0:
        for x in range(n_row):
            for y in range(n_col):
                if game.visited[x][y] == 1:
                    buttons[x][y].configure(bg = "GREEN", text = game.mine_count[x][y])
    
    else:
        buttons[i][j].configure(bg = 'GREEN', text = game.mine_count[i][j])

def LeftClick(i,j):

    if game.win != 0 or game.marked[i][j] or game.visited[i][j]:
        return
    
    game.check_grid(i,j)
    recolor(i,j)

    if game.game == 0:
        
        # check for loss
        if game.win == -1:
            button_smily.configure(bg = 'VIOLET', text = ":(")
        
        #check for win
        elif game.win == 1:
            button_count.configure(text = f'{n_mines}/{n_mines}') # set count to full
            button_smily.configure(bg = 'CYAN', text = ":D")
            for x in range(n_row):
                for y in range(n_col):
                    if game.mine_count[x][y] == 'M':
                        buttons[x][y].configure(bg = "ORANGE", text = 'M')
                    else:
                        buttons[x][y].configure(bg = "GREEN", text = game.mine_count[x][y])

def RightClick(i,j,click):
    if game.win != 0 or game.visited[i][j]:
        return
    game.mark_bomb(i,j)
    if not game.visited[i][j]:
        button_count.configure(text = f'{game.count_marked()}/{n_mines}')
        if game.marked[i][j] == 1:
            buttons[i][j].configure(bg = 'ORANGE', text = 'F')
        else:
            buttons[i][j].configure(bg = 'WHITE', text = ' ')

buttons = [[tk.Button(root, bg = 'WHITE', text=" ", width=c, height=c, compound='c', image = IMG, disabledforeground="black", command = partial(LeftClick,i,j)) for j in range(n_col)] for i in range(n_row)]

# place buttons in grid
for i in range(n_row):
    for j in range(n_col):
        buttons[i][j].grid(row = i, column = j)
        buttons[i][j].bind('<Button-3>', partial(RightClick,i,j))

button_restart = tk.Button(root, bg = 'YELLOW', text="RESET", width=c, height=c, compound='c', image = IMG, command = restart)
button_restart.grid(row = n_row, column = 0)

button_smily = tk.Button(root, bg = 'GRAY', text=":)", width=c, height=c, compound='c', image = IMG)
button_smily.grid(row = n_row, column = 1)

button_count = tk.Button(root, bg = 'ORANGE', text=f"0/{n_mines}", width=c, height=c, compound='c', image = IMG)
button_count.grid(row = n_row, column = 2)

###########
### SAT ###
###########

button_SAT_arrow = tk.Button(root, bg = 'CYAN', text="->", width=c, height=c, compound='c', image = IMG)

# button_SAT_arrow.grid(row = n_row, column = n_col-1)
# button_SAT_arrow.configure(state = "disabled")
# button_SAT_arrow.grid_forget()

def board_state(state): # state = 'normal' or 'disabled'
    for x in range(n_row):
        for y in range(n_col):
            buttons[x][y].configure(state = state)
        

def SAT_step():

    if game.win != 0:
        return
    
    while True:
        def close():
            button_SAT.configure(text = '>SAT<', command = SAT_step)
            button_SAT_arrow.grid_forget()
            var.set(-1)
            
        def proceed():
            var.set(1)

        if game.game == 0:
            return
        board_state('disabled')
        button_SAT.configure(text = 'X', command = close)
        button_SAT_arrow.configure(command = proceed)
        button_SAT_arrow.grid(row = n_row, column = n_col-1)
        safe, mines = game.find_safe_mines()
        
        var = tk.IntVar()
        var.set(0)

        # no zeros found yet
        if sum([0 in row for row in game.discovered_board()]) == 0:
            label.grid(row = n_row + 1, column = 0, columnspan=n_col)
            label.configure(text = "SAT solver:\nAt the moment we don't have enough information,\nI can just recommend a random guess,\nwhat about here?\n(click -> to proceed, x to exit)")
            i,j = random.randint(0,n_row-1), random.randint(0,n_col-1)
            while game.discovered_board()[i][j]:
                i,j = random.randint(0,n_row-1), random.randint(0,n_col-1)
            buttons[i][j].configure(bg = 'CYAN')

            root.wait_variable(var) # wait for X or -> to be clicked ...
            
            if var.get() == 0:
                raise AssertionError("this should not happen...")
            elif var.get() == -1:
                board_state('normal')
                button_SAT_arrow.grid_forget()
                buttons[i][j].configure(bg = 'WHITE')
                label.grid_forget()
                return
            elif var.get() == 1:
                board_state('normal')
                label.configure(text = 'SAT solver:\n')
                buttons[i][j].invoke() # click on cell
        
        # zeros were found
        else:
            safe_list, mines_list = game.find_safe_mines()
            
            if len(safe_list) == 0 and len(mines_list) == 0:
                #SAT SOLVER!
                print("The percentages shown are the probability of the cells being safe. I suggest guessing the highlighted cell (one with the highest probability of safe picked randomly)")
                sf_dct = game.p_safe_dict()
                for x,y in sf_dct:
                    buttons[x][y].configure(text = str(round(100*sf_dct[(x,y)]))+'%')
                
                cells_best = [cell for cell in sf_dct if sf_dct[cell] == max(sf_dct.values())]
                print(cells_best)
                i,j = random.choice(cells_best)

                buttons[i][j].configure(bg = "CYAN")
                
                root.wait_variable(var)

                if var.get() == 0:
                    raise AssertionError("this should not happen...")
                elif var.get() == -1:
                    board_state('normal')
                    button_SAT_arrow.grid_forget()
                    buttons[i][j].configure(text = '', bg = 'WHITE')
                    label.grid_forget()
                    return
                elif var.get() == 1:
                    board_state('normal')
                    for x,y in sf_dct:
                        buttons[x][y].configure(text = '', bg = 'WHITE')
                    buttons[i][j].invoke()

            else:
                label.configure(text = "SAT solver:\ngreens = safe cell,\nred = mine\n(click -> to proceed, x to exit).")
                
                for x,y in safe_list:
                    buttons[x][y].configure(bg = "LIMEGREEN")
                for x,y in mines_list:
                    buttons[x][y].configure(bg = "lightsalmon1")
                
                root.wait_variable(var) # wait for X or -> to be clicked ...
                
                if var.get() == 0:
                    raise AssertionError("this should not happen...")
                elif var.get() == -1:
                    board_state('normal')
                    button_SAT_arrow.grid_forget()
                    for x,y in safe_list:
                        buttons[x][y].configure(bg = 'WHITE')
                    for x,y in mines_list:
                        buttons[x][y].configure(bg = 'WHITE')
                    label.grid_forget()
                    return
                elif var.get() == 1:
                    board_state('normal')
                    for x,y in safe_list:
                        buttons[x][y].invoke() # click on cell
                    for x,y in mines_list:
                        RightClick(x,y,'')
                    label.configure(text = 'SAT solver:\n')
        
        board_state('disable')
        # var.set(0)
        root.wait_variable(var)
        if var.get() == -1:
            board_state('normal')
            button_SAT_arrow.grid_forget()
            return
        elif var.get() == 1:
            None

button_SAT = tk.Button(root, bg = 'CYAN', text=">SAT<", width=c, height=c, compound='c', image = IMG, command = SAT_step)
button_SAT.grid(row = n_row, column = n_col-2)

label = tk.Label(root, bg = "cadetblue2")

root.mainloop()

