# math-program
This program is a math program with multiple different features.  There is a sequence generator, simple calculator, equation solver, and a game.

    The sequence generator will have a menu that can print sequences with 15 numbers per line.  Afterwards it will also print the sum and return to the menu.  The sequences that will be present are arithmetic, geometric, harmonic, and fibonacci.

        An arithmetic sequence is a sequence where consecutive term differ by a common difference.  The parameters for this sequence type will be the first term, the common difference, and the number of terms to be printed.  For example, inputting 2 then 5 then 10 will output 2 7 12 17 22 27 32 37 42 47.  It will also print the sum of the numbers in the sequence (which in this case is 245).

        A geometric sequence is a sequence where consecutive terms have a common ratio.  The parameters for this sequence are similar to the arithmetic sequence but replace the common difference with the common ratio.  For example, inputting 3 then 2 then 5 will output 3 6 12 24 48.  Again, it will print the sum (in this case 93).

        A harmonic sequence is a sequence of fractions where the denominators form an arithmetic sequence.  The parameters for this sequence are the first term’s denominator, the common difference of denominators, and the number of terms.  This one prints one term per line since aside from the fraction (eg 1/2) there is also the approximation (eg 0.5).  For example, inputting 2 then 3 then 4 outputs:

            1/2 or 0.5
            1/5 or 0.2
            1/8 or 0.125
            1/11 or 0.09090909090909091

            Sum of Sequence: 0.9159090909090909

        The Fibonacci Sequence is defined such that the first two terms are 0 and 1 and each successive term is the sum of the two previous terms.  The only parameter for this one is the number of terms.  For example, inputting 16 will output:

            0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 
            610 
            Sum of Sequence: 1596

        Inputting 5 into the sequence generator’s main menu will exit out back to the main menu (whole program).
	
    The arithmetic calculator is pretty simple and just outputs the number that is the result of the equation inputted.  The calculator follows PEMDAS (in this case it’s just multiplication and division before addition and subtraction).  
    For example, inputting 21/3+5x4-1 outputs 26.  Typing ‘MAIN’ in the expression input will make you exit back to the main menu

    The equation solver solves equations inputted by the user.  This feature is restricted to the integers (for now). There
    are 4 sub-solvers within the main solver.  The program prompts the user for the necessary constants one at a time.  Afterwards, it displays the equation and the answer.

        Linear equations (ax+b=cx+d).  The solver checks for cases with no solutions and infinite solutions.  Aside from those cases it just outputs the answer.  For example, inputting 20 then 7 then 5 then 4 outputs:

            Input 'a' value: 20
            Input 'b' value: 7
            Input 'c' value: 5
            Input 'd' value: 4
            Equation: 20x+7=5x+4
            Answer: x=-0.2

        Quadratic equations (ax^2+bx+c=0). The solver checks for cases with no real solutions.  If ‘a’ is 0 (which would just be linear) the program also outputs the correct answer.  If both ‘a’ and ‘b’ are 0 then the program outputs infinite solutions or no solutions accordingly.  It also outputs the roots even if they are complex.  For example, inputting 15 then -2 then 5 outputs:

            Input 'a' value: 15
            Input 'b' value: -2
            Input 'c' value: 5
            Equation: 15x^2-2x+5=0
            Answer: x=(1±sqrt(74)i)/15

        Systems of linear equations (ax+by+c=0, dx+fy+g=0). The solver checks for cases with no solutions and infinite solutions.  It outputs the correct solution set for these cases.  If there is only one solution the solver outputs it accordingly.  For example, inputting 11 then -3 then 9 then 2 then 3 then -10 outputs:

            Input 'a' value: 11
            Input 'b' value: -3
            Input 'c' value: 9
            Input 'd' value: 2
            Input 'f' value: 3
            Input 'g' value: -10
            Equations: 11x-3y+9=0, 2x+3y-10=0
            Answer: (0.07692307692307697, 3.2820512820512824)

        Trigonometry is the last sub-solver in this equation solver.  The user will input an angle (in degrees) and the program will output the values of sine, cosine, tangent, secant, cosecant, and cotangent functions.  The program detects undefined values and also prints exact numbers for “nice” angles (15, 30, 45, 60, 90 etc)

        Inputting 5 into the equation solver’s main menu will exit out back to the main menu (whole program).

    Lastly, the math game is a simple game with five modes (addition, subtraction, multiplication, division, and
    powers) as well as a mode with mixed operations.  Every correct answer gives 5 points and every wrong or invalid answer deducts 3 points.  After every question the user is prompted to continue.  If the user stops the program outputs the score and the user can play a different mode or leave to the main menu.