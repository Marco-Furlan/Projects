from parameters import *
import random
from itertools import combinations
from pysat.solvers import Minisat22
import copy # needed to use the "deepcopy" function

neighbour = lambda i,j: [cell for cell in [(i+I,j+J) for I in [-1,0,1] for J in [-1,0,1]] if 0 <= cell[0] < n_row and 0 <= cell[1] < n_col and cell != (i,j)]

class Game():
    def __init__(self):
        """starts a new game"""
        self.game = 1
        self.win = 0
        self.grid = [[0 for j in range(n_col)] for i in range(n_row)]
        for i,j in random.sample(sum([[(i,j) for j in range(n_col)] for i in range(n_row)], []), n_mines):
            self.grid[i][j] = 1
        self.visited = [[0 for j in range(n_col)] for i in range(n_row)]
        self.marked = [[0 for j in range(n_col)] for i in range(n_row)]
        self.mine_count = [[sum([1 for x,y in neighbour(i,j) if self.grid[x][y]]) if not self.grid[i][j] else 'M' for j in range(n_col)] for i in range(n_row)]

    def show_board(self, board = None, show = 'visited'):
        """shows the board. If called without specifying parameters, the board will look like a classic Minesweeper game.
        show='all' reveals the entire board"""
        if board == None:
            board = self.mine_count
        if show == 'all': #show entire board
            brd = [[board[i][j] for j in range(n_col)] for i in range(n_row)] ## add marked condition
        elif show != 'all': #show only visited cells
            brd = [[board[i][j] if self.visited[i][j]==1 else ' ' for j in range(n_col)] for i in range(n_row)]
            brd = [[brd[i][j] if self.marked[i][j] == 0 else 'X' for j in range(n_col)] for i in range(n_row)]
        print(' # | '+ ' '.join(list(map(str,range(n_col)))))
        print('-'*(2*n_col+4))
        for i in range(n_row):
            row = ' '+str(i)+' | ' + ' '.join([str(cell) for cell in brd[i]])
            print(row)
        return

    def return_board(self, show = 'visited'):
        if show == 'all': #show entire board
            brd = [[self.mine_count[i][j] for j in range(n_col)] for i in range(n_row)] ## add marked condition
        else: #show only visited cells
            brd = [[self.mine_count[i][j] if self.visited[i][j]==1 else ' ' for j in range(n_col)] for i in range(n_row)]
            brd = [[brd[i][j] if self.marked[i][j] == 0 else 'X' for j in range(n_col)] for i in range(n_row)]
        print(brd)
        return brd

    def check_grid(self,i,j, recur=False):
        """check cell (i,j). If marked or already visited, it won't check it. If there is a bomb, the game will end.
        If there is not a bomb, the game will continue (or end in a win). If cell's mine_count is zero, the function will
        recursively call itself to all the neighbouring cells"""

        if self.marked[i][j] or self.visited[i][j]:
            return
        # check if lose
        if self.grid[i][j] == 1:
            self.visited[i][j] = 1
            self.game = 0
            self.win = -1
            return
        #if not lose:
        self.visited[i][j] = 1
        if sum([sum(row) for row in self.visited]) == n_row*n_col-n_mines:
            self.game = 0
            self.win = 1
        if self.mine_count[i][j]:
            return
        else:
            for cell_i, cell_j in neighbour(i,j):
                if not self.visited[cell_i][cell_j]:
                    self.check_grid(cell_i, cell_j, recur=True)
                
    def mark_bomb(self,i,j):
        """If cell (i,j) is not visited, this function will mark that cell (or unmark if already marked).
        This is used when it is known that cell (i,j) contains a bomb"""
        if not self.visited[i][j]:
            if not self.marked[i][j]:
                self.marked[i][j] = 1
            else:
                self.marked[i][j] = 0
    
    def count_marked(self):
        """Counts marked cells"""
        return sum([sum(row) for row in self.marked])
    
    ###########
    ### SAT ###
    ###########
    
    @staticmethod
    def exactly(C,k):
        """Input: C list of SAT boolean variables (integers), k integer.
        Output: formula (list of clauses) to add to the model, equivalent to "exactly k"
        """
        assert len(C) >0, "Error: C must have size at least 1"
        assert isinstance(C,list), "Error: C must be  a list"
        assert len(C) >= k, "Error: len(C) < k"
        n = len(C)
        l = []
        # at least k
        combs = combinations(C,n-k+1)
        for comb in combs:
            l.append(list(comb))
        # at most k
        combs = combinations(C,k+1)
        for comb in combs:
            l.append(list(map(lambda x: -x, list(comb))))
        return l

    def discovered_board(self):
        """returns current known information about the board (discovered by the player)"""
        discovered_board = [[self.mine_count[i][j] if self.visited[i][j] else None for j in range(n_col)] for i in range(n_row)]
        for i in range(n_row):
            for j in range(n_col):
                if self.marked[i][j]:
                    discovered_board[i][j] = 'X'
        return discovered_board

    def find_safe_mines(self):
        """Finds safe squares and mines given the information contained in discovered_board.
        This function does not take into account the number of remaining mines."""
        
        discovered_board = self.discovered_board()

        # deal with marked mines
        info_board = copy.deepcopy(discovered_board)
        for i in range(n_row):
            for j in range(n_col):
                if info_board[i][j] == 'X':
                    for (x,y) in neighbour(i,j):
                        if isinstance(info_board[x][y],int):
                            info_board[x][y] -= 1
        
        # unvisited boundary (--> propositions)
        unvisited_boundary = []
        for i in range(n_row):
            for j in range(n_col):
                if info_board[i][j]==None:
                    for (x,y) in neighbour(i,j):
                        if info_board[x][y] != None and info_board[x][y] != 'X':
                            unvisited_boundary.append((i,j))
                            break
        
        # propositions (propositional variables)
        coords_to_int = {unvisited_boundary[i]:(i+1) for i in range(len(unvisited_boundary))}
        int_to_coords = {y: x for x, y in coords_to_int.items()}
        
        # visited_boundary (--> formulas)
        visited_boundary = []
        for i in range(n_row):
            for j in range(n_col):
                if isinstance(info_board[i][j],int):
                    for (x,y) in neighbour(i,j):
                        if info_board[x][y] == None:
                            visited_boundary.append((i,j))
                            break
        
        # formulas
        formulas = []
        for (i,j) in visited_boundary:
                C = [coords_to_int[(x,y)] for (x,y) in neighbour(i,j) if info_board[x][y] == None]
                k = info_board[i][j]
                formula = self.exactly(C, k)
                # print('adding formula:',(i,j),formula)
                formulas.append(formula)
        
        # find safe cells and mines
        safe_list = []
        mines_list = []
        for index in int_to_coords:
            
            # find safe
            with Minisat22() as model:
                for formula in formulas: model.append_formula(formula)
                model.add_clause([index]) # here we are adding "there is a mine in 'index'", if model is unsolvable it means that there is no mine in here
                if not model.solve():
                    safe_list.append(int_to_coords[index])
            
            # find mine
            with Minisat22() as model:
                for formula in formulas: model.append_formula(formula)
                model.add_clause([-index])
                if not model.solve():
                    mines_list.append(int_to_coords[index])
        
        return (safe_list,mines_list)

    @staticmethod
    def probability_of_safe(model):
        '''The input is a model.
        The output is a list whose first element is 0 and the i-th element is the number of models that make the proposition i false.
        (Proposition i false <-> there is no bomb in cell i <-> cell i is safe)'''
        
        model.solve()
        
        truth_count = [0 for _ in range(len(model.get_model())+1)]
        tot = 0
        for mod in model.enum_models():
            tot += 1
            for i in mod:
                if i < 0:
                    truth_count[-i] += 1
        
        return list(map(lambda x: x/tot, truth_count))


    def p_safe_dict(self):
        """Returns a dictionary whose keys are boundary cells and whose items are the percentages of models in which the proposition
        'the cell in the key is safe' is true"""
        
        discovered_board = self.discovered_board()

        # deal with marked mines
        info_board = copy.deepcopy(discovered_board)
        for i in range(n_row):
            for j in range(n_col):
                if info_board[i][j] == 'X':
                    for (x,y) in neighbour(i,j):
                        if isinstance(info_board[x][y],int):
                            info_board[x][y] -= 1
        
        # unvisited boundary (--> propositions)
        unvisited_boundary = []
        for i in range(n_row):
            for j in range(n_col):
                if info_board[i][j]==None:
                    for (x,y) in neighbour(i,j):
                        if info_board[x][y] != None and info_board[x][y] != 'X':
                            unvisited_boundary.append((i,j))
                            break
        
        # propositions (propositional variables)
        coords_to_int = {unvisited_boundary[i]:(i+1) for i in range(len(unvisited_boundary))}
        int_to_coords = {y: x for x, y in coords_to_int.items()}
        
        # visited_boundary (--> formulas)
        visited_boundary = []
        for i in range(n_row):
            for j in range(n_col):
                if isinstance(info_board[i][j],int):
                    for (x,y) in neighbour(i,j):
                        if info_board[x][y] == None:
                            visited_boundary.append((i,j))
                            break
        
        # formulas
        formulas = []
        for (i,j) in visited_boundary:
                C = [coords_to_int[(x,y)] for (x,y) in neighbour(i,j) if info_board[x][y] == None]
                k = info_board[i][j]
                formula = self.exactly(C, k)
                # print('adding formula:',(i,j),formula)
                formulas.append(formula)
        
        # define model and output dictionary
        
        with Minisat22() as model:
            for formula in formulas: model.append_formula(formula)
            p_safe = self.probability_of_safe(model)
            
        return {int_to_coords[i]:p_safe[i] for i in int_to_coords.keys()}

