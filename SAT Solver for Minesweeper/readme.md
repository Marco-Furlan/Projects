# SAT solver for Minesweeper

Video explenation: [...]

In this project [^1] I coded from scratch the popular game Minesweeper, and impmlemented a SAT solver to it.

[^1]: made for the course Knowledge and Data Mining, from the Data Science Master at University of Padua.

![](<https://github.com/Marco-Furlan/Projects/blob/main/SAT Solver for Minesweeper/images/minesweeper.png?raw=true>)

## What is an SAT solver for Minesweeper?

You can find a description of a SAT solver [here](https://en.wikipedia.org/wiki/SAT_solver). We encode a configuration of the game of minesweeper in boolean propositions where the variables are the cells (true if contains bomb, false otherwise) and the propositions are built with the information shown in the board.

An example: if we have the following configuration:

![](<https://github.com/Marco-Furlan/Projects/blob/main/SAT Solver for Minesweeper/images/example1.png?raw=true>)

We can call the empty cells $x, y, z$:

![](<https://github.com/Marco-Furlan/Projects/blob/main/SAT Solver for Minesweeper/images/example2.png?raw=true>)


