# SAT solver for Minesweeper

Video explenation: [...]

In this project [^1] I coded from scratch the popular game Minesweeper, and impmlemented a SAT solver to it.

[^1]: made for the course Knowledge and Data Mining, from the Data Science Master at University of Padua.

![](<https://github.com/Marco-Furlan/Projects/blob/main/SAT Solver for Minesweeper/images/minesweeper.png?raw=true>)

## What is a SAT solver for Minesweeper?

You can find a description of a SAT solver [here](https://en.wikipedia.org/wiki/SAT_solver). We encode a configuration of the game of minesweeper in boolean propositions where the variables are the cells (true if contains bomb, false otherwise) and the propositions are built with the information shown in the board.

An example: if we have the following configuration:

![](<https://github.com/Marco-Furlan/Projects/blob/main/SAT Solver for Minesweeper/images/example1.png?raw=true>)

We can call the empty cells $x, y, z$:

![](<https://github.com/Marco-Furlan/Projects/blob/main/SAT Solver for Minesweeper/images/example2.png?raw=true>)

The information given by the $1$ can therefore be encoded in the following way:

$(x \lor y \lor z) \land (\neg x \lor \neg y) \land (\neg y \lor \neg z) \land (\neg x \lor \neg z)$

Which is equivalent to: "*exactly one among* $x,y,z$ *is true*" (that is, exactly one contains a bomb). In fact:

- $x \lor y \lor z$ is equivalent to: "*at least one among* $x,y,z$ *contains a bomb*";
- $(\neg x \lor \neg y) \land (\neg y \lor \neg z) \land (\neg x \lor \neg z)$ is equivalent to: "*at most one among* $x,y,z$ *contains a bomb*".

<br/>

More generally, any number we see on the board of a minesweeper game means "*exactly [...] of the neighbouring cells contains a bomb*". So we need a way to encode this information in boolean propositions.

Here's how: given $n$ propositional variables $x_1, x_2, \dots, x_n$, the proposition "*exactly k among* $x_1, x_2, \dots, x_n$ *are true*" can be written as the logical intersecion of:

- "*at least k among* $x_1, x_2, \dots, x_n$ *are true*":

$\package{amsmath}$

$$\bigwedge_{\substack{I \subset \{1,2, \dots, n\} \\ |I| = n-k+1}} \bigvee\limits_{i \in I} x_i$$

- "*at most k among* $x_1, x_2, \dots, x_n$ *are true*":