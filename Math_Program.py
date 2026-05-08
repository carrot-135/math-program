# CS2 Python script template for Quarter 4 Coding Project (AY 2025-2026)

# Program: ALL in ONE Math Program
# Programmer: Ethan Caleb M. Choy
# Section: 8 Ilang-Ilang
# Start Date: 24 March 2026
# Last Date of Revision: DD April 2026

# Honor Code:

# As a Philippine Science High School scholar I subscribe to the core
# values of INTEGRITY, EXCELLENCE, SERVICE. That the output I will submit
# is MY OWN ORIGINAL WORK. I will AVOID sharing answers with others
# (electronically or through other forms), and I will report suspected
# violations (academic dishonesty). Further, I am aware that ANY FORM
# OF ACADEMIC DISHONESTY is subject to DISCIPLINARY ACTIONS.

import math, random, operator
from fractions import Fraction

int_option_choice = ''

def clear_screen():
    for i in range(0, 45):
        print("")

def main_menu():
    
    while True:
        print("ALL IN ONE MATH PROGRAM!!!")
        print("\tSelect your option:")
        print("\t1. Sequence Generator")
        print("\t2. Arithmetic Calculator")
        print("\t3. Equation Solver")
        print("\t4. Math Game!!")
        print("\t5. Exit :(")

        int_option_choice = input("Your Choice: ")

        while int_option_choice not in ['1', '2', '3', '4', '5']:
            print("Invalid Choice! Please try again.")
            int_option_choice = input("Your Choice: ")
            
        if int_option_choice == '1':
            Seq_Gen()
        elif int_option_choice == '2':
            Arith_Calc()
        elif int_option_choice == '3':
            Equa_Solver()
        elif int_option_choice == '4':
            Math_Game()
        else: #choice is 5
            print("Thank you for using the program! :D")
            break

def Seq_Gen():
    clear_screen()
    
    while True:
    
        int_SG_first = 0
        int_SG_diff = 0
        int_SG_ratio = 0
        int_SG_num_terms = 0
        int_SG_sum = 0
        int_SG_last = 0
        int_SG_sum = 0
        str_SG_choice = ''
        int_SG_FB_term1 = 0
        int_SG_FB_term2 = 0
        int_SG_no_of_terms_on_line = 0
        
        print("Sequence Generator")
        print("\tSelect Sequence Type:")
        print("\t1. Arithmetic Sequence")
        print("\t2. Geometric Sequence")
        print("\t3. Harmonic Sequence")
        print("\t4. Fibonacci Sequence")
        print("\t5. Back to Main Menu")
        str_SG_choice = input("What is your choice? ")

        while str_SG_choice not in ['1', '2', '3', '4', '5']:
            print("Invalid Choice! Please try again.")
            str_SG_choice = input("Your Choice: ")
    
        if str_SG_choice == '1':
            int_SG_first = input("What is the first number of the arithmetic sequence? ")
            int_SG_diff = input("What is the common difference? ")
            int_SG_num_terms = input("How many terms do you want? ")
            print("")

            try:
                int_SG_first, int_SG_diff, int_SG_num_terms = int(int_SG_first), int(int_SG_diff), int(int_SG_num_terms)
            except:
                input("Invalid input! Please try again!")
                clear_screen()
            else:
                if int_SG_num_terms <= 0:
                    input("Number of terms must be a positive integer!")
                    clear_screen()
                else:
                    for i in range(0, int_SG_num_terms):
                        if int_SG_no_of_terms_on_line == 15:
                            print("")
                            int_SG_no_of_terms_on_line = 0
                        print(int_SG_first, end=" ")
                        int_SG_sum += int_SG_first
                        int_SG_no_of_terms_on_line += 1
                        int_SG_first += int_SG_diff
                    print()
                    print("Sum of Sequence:", int_SG_sum)
                    input("Press Enter to go back")
                    clear_screen()
            
        elif str_SG_choice == '2':
            int_SG_first = input("What is the first number of the geometric sequence? ")
            int_SG_ratio = input("What is the common ratio? ")
            int_SG_num_terms = input("How many terms do you want? ")
            print("")

            try:
                int_SG_first, int_SG_ratio, int_SG_num_terms = int(int_SG_first), int(int_SG_ratio), int(int_SG_num_terms)
            except:
                input("Invalid input! Please try again!")
                clear_screen()
            else:
                if int_SG_num_terms <= 0:
                    input("Number of terms must be a positive integer!")
                    clear_screen()
                else:
                    for i in range(0, int_SG_num_terms):
                        if int_SG_no_of_terms_on_line == 15:
                            print("")
                            int_SG_no_of_terms_on_line = 0
                        print(int_SG_first, end=" ")
                        int_SG_sum += int_SG_first
                        int_SG_no_of_terms_on_line += 1
                        int_SG_first *= int_SG_ratio
                    print()
                    print("Sum of Sequence:", int_SG_sum)
                    input("Press Enter to go back")
                    clear_screen()
            
        elif str_SG_choice == '3':
            int_SG_first = input("What is the denominator of the first term? ")
            int_SG_diff = input("What is the common difference between consecutive denominators? ")
            int_SG_num_terms = input("How many terms do you want? ")
            print("")

            try:
                int_SG_first, int_SG_diff, int_SG_num_terms = int(int_SG_first), int(int_SG_diff), int(int_SG_num_terms)
            except:
                input("Invalid input! Please try again!")
                clear_screen()
            else:
                int_SG_last = int_SG_first + int_SG_diff * int_SG_num_terms

                if int_SG_first == 0:
                    input("Error! Division by 0.")
                    clear_screen()
                else:
                    if int_SG_num_terms <= 0:
                        input("Number of terms must be a positive integer!")
                        clear_screen()
                    else:
                        print("")
                        try:
                            for i in range(0, int_SG_num_terms):
                                if int_SG_first > 0:
                                    print(f"1/{int_SG_first} or {1/int_SG_first}")
                                else: #less than 0
                                    print(f"-1/{-int_SG_first} or {1/int_SG_first}")
                                int_SG_sum += 1/int_SG_first
                                int_SG_first += int_SG_diff
                            print("\nSum of Sequence:", int_SG_sum)
                        except:
                            print("Error! The denominator has reached 0.")
                            print("\nPartial Sum:", int_SG_sum)
                        input("Press Enter to go back")
                        clear_screen()
            
        elif str_SG_choice == '4':
            int_SG_num_terms = input("How many terms do you want? ")
            print("")
            int_SG_FB_term1 = 0
            int_SG_FB_term2 = 1

            try:
                int_SG_num_terms = int(int_SG_num_terms)
            except:
                input("Invalid input! Please try again!")
                clear_screen()
            else:
                int_SG_num_terms = int(int_SG_num_terms)
                if int_SG_num_terms <= 0:
                    input("Number of terms must be a positive integer!")
                    clear_screen()
                else:
                    for i in range(int_SG_num_terms):
                        if int_SG_no_of_terms_on_line == 15:
                            print("")
                            int_SG_no_of_terms_on_line = 0
                        print(int_SG_FB_term1, end=" ")
                        int_SG_sum += int_SG_FB_term1
                        int_SG_no_of_terms_on_line += 1
                        int_SG_FB_term1, int_SG_FB_term2 = int_SG_FB_term2, int_SG_FB_term1 + int_SG_FB_term2
                    print()
                    print("Sum of Sequence:", int_SG_sum)
                    input("Press Enter to go back")
                    clear_screen()
                
        elif str_SG_choice == '5':
            input("Thank you for using the Sequence Generator! :)")
            clear_screen()
            return

def Arith_Calc():
    clear_screen()
        
    while True:
        str_AC_expre = ''
        list_AC_numbers = []
        list_AC_operands = []
        str_AC_slack_num = ''
        int_AC_new_number = 0
        int_AC_index = 0
        bool_AC_calc_error = False

        print("Arithmetic Calculator")
        print("RULES:")
        print("\t1. Use +-*/ ONLY")
        print("\t2. FIRST and LAST characters MUST be numbers")
        print("\t3. NO DECIMALS (instead do a/b)")
        print("\t4. PEMDAS will be followed")
        print("\t5. NO characters besides numbers and +-*/")
        print("\t6. NO spaces")
        print("\n\tEnter 'MAIN' to return to main menu\n")
        str_AC_expre = str(input("Input your expression: "))

        if str_AC_expre == 'MAIN':
            input("Thank you for using the calculator! :D")
            clear_screen()
            return
        elif str_AC_expre == '':
            input("Error! Blank Expression!")
            clear_screen()
        else:
            if not str_AC_expre[0].isnumeric() or not str_AC_expre[len(str_AC_expre)-1].isnumeric():
                input("Error! Malformed Expression.")
                clear_screen()
            else:
                for i in range(0, len(str_AC_expre)):
                    if str_AC_expre[i] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '/']:
                        input("Error! Your expression has a space or an illegal symbol.")
                        clear_screen()
                        break
                    elif str_AC_expre[i].isnumeric():
                        str_AC_slack_num += str(str_AC_expre[i])
                    else:
                        list_AC_numbers.append(Fraction(str_AC_slack_num))
                        str_AC_slack_num = ''
                        list_AC_operands.append(str(str_AC_expre[i]))

                    if not str_AC_expre[i].isnumeric():
                        if i+1<len(str_AC_expre) and not str_AC_expre[i+1].isnumeric():
                            input("Error! Consecutive operators is not allowed!")
                            clear_screen()
                            break
                    
                else:
                    list_AC_numbers.append(Fraction(str_AC_slack_num))
                    if len(list_AC_operands) == 0:
                        print(f"Answer: {str_AC_expre}")
                        
                        str_AC_again = input("Go Again? [y/n]: ")
                        if str_AC_again == 'n':
                            input("Thank you for using the calculator! :D")
                            break
                        else:
                            clear_screen()
                    else:
                        int_AC_index = 0
                        while int_AC_index < len(list_AC_operands):
                            int_AC_new_number = 0
                            if list_AC_operands[int_AC_index] == '*':
                                int_AC_new_number = list_AC_numbers[int_AC_index] * list_AC_numbers[int_AC_index+1]
                                del list_AC_operands[int_AC_index]
                                del list_AC_numbers[int_AC_index:int_AC_index+2]
                                list_AC_numbers.insert(int_AC_index, int_AC_new_number)
                            elif list_AC_operands[int_AC_index] == '/':
                                if list_AC_numbers[int_AC_index+1] == 0:
                                    input("Error! Division by 0.")
                                    bool_AC_calc_error = True
                                    break
                                else:
                                    int_AC_new_number = list_AC_numbers[int_AC_index] / list_AC_numbers[int_AC_index+1]
                                    del list_AC_operands[int_AC_index]
                                    del list_AC_numbers[int_AC_index:int_AC_index+2]
                                    list_AC_numbers.insert(int_AC_index, int_AC_new_number)
                            else:
                                int_AC_index += 1

                        int_AC_index = 0
                        while int_AC_index < len(list_AC_operands):
                            int_AC_new_number = 0
                            if list_AC_operands[int_AC_index] == '+':
                                int_AC_new_number = list_AC_numbers[int_AC_index] + list_AC_numbers[int_AC_index+1]
                                del list_AC_operands[int_AC_index]
                                del list_AC_numbers[int_AC_index:int_AC_index+2]
                                list_AC_numbers.insert(int_AC_index, int_AC_new_number)
                            elif list_AC_operands[int_AC_index] == '-':
                                int_AC_new_number = list_AC_numbers[int_AC_index] - list_AC_numbers[int_AC_index+1]
                                del list_AC_operands[int_AC_index]
                                del list_AC_numbers[int_AC_index:int_AC_index+2]
                                list_AC_numbers.insert(int_AC_index, int_AC_new_number)
                            else:
                                int_AC_index += 1

                        
                        if not bool_AC_calc_error:
                            if int_AC_new_number % 1 == 0:
                                print("Answer:", int(int_AC_new_number))
                            else:
                                print("Answer:", float(int_AC_new_number))
                            
                            input("Press Enter to go back")
                            clear_screen()
                        else:
                            clear_screen()
        
    clear_screen()
    return

def ES_sqrt_coeff(disc):
    int_coeff = 1
    for i in range(2, math.ceil(disc/2)+1):
        while disc % i**2 == 0:
            int_coeff *= i
            disc /= i**2
    return int_coeff
    
def ES_sqrt_radicand(disc):
    for i in range(2, math.ceil(disc/2)+1):
        while disc % i**2 == 0:
            disc /= i**2
    return int(disc)
        
def Equa_Solver():
    clear_screen()

    while True:
        str_ES_choice = ''
        
        int_ES_a = 0
        int_ES_b = 0
        int_ES_c = 0
        int_ES_d = 0
        int_ES_f = 0
        int_ES_g = 0
    
        int_ES_disc = 0
        int_ES_const = 0
        int_ES_imag_part_coeff = 0
        int_ES_imag_part_radicand = 0
        int_ES_denom = 0
        int_ES_GCD = 0
    
        str_ES_equation = ''
        str_ES_answer = ''
    
        int_ES_slope_EQ1 = 0
        int_ES_yint_EQ1 = 0
        int_ES_slope_EQ2 = 0
        int_ES_yint_EQ2 = 0
        int_ES_xcoord = 0
        int_ES_ycoord = 0
    
        int_ES_angle = 0
        int_ES_og_angle = 0

        float_ES_sin = ''
        float_ES_cos = ''
        float_ES_tan = ''
        float_ES_csc = ''
        float_ES_sec = ''
        float_ES_cot = ''
    
        bool_ES_a_is_0 = False
        bool_ES_b_is_0 = False
        bool_ES_c_is_0 = False
        bool_ES_d_is_0 = False
        bool_ES_f_is_0 = False
        bool_ES_EQ1_iden = False
        bool_ES_EQ1_contr = False
        bool_ES_EQ2_iden = False
        bool_ES_EQ2_contr = False
    
        print("Equation Solver")
        print("\tSelect Equation Type:")
        print("\t1. Linear (ax+b=cx+d)")
        print("\t2. Quadratic (ax^2+bx+c=0)")
        print("\t3. Systems of Linear Equations")
        print("\t4. Trigonometry (eg. sin(60) = ?)")
        print("\t5. Back to Main Menu")
        
        str_ES_choice = input("What is your choice? ")

        while str_ES_choice not in ['1', '2', '3', '4', '5']:
            print("Invalid Choice! Please try again.")
            str_ES_choice = input("Your Choice: ")
    
        if str_ES_choice == '1':
            print("\n\tax+b=cx+d")
            int_ES_a = input("Input 'a' value: ")
            int_ES_b = input("Input 'b' value: ")
            int_ES_c = input("Input 'c' value: ")
            int_ES_d = input("Input 'd' value: ")

            try:
                int_ES_a, int_ES_b, int_ES_c, int_ES_d = int(int_ES_a), int(int_ES_b), int(int_ES_c), int(int_ES_d)
            except:
                input("Error! Please input integers only.")
                clear_screen()
            else:

                str_ES_equation += 'Equation: '

                if int_ES_a == 0:
                    bool_ES_a_is_0 = True
                elif int_ES_a == 1:
                    str_ES_equation += 'x'
                else:
                    str_ES_equation += f'{int_ES_a}x'

                if int_ES_b == 0:
                    if bool_ES_a_is_0:
                        str_ES_equation += '0'
                    else:
                        pass
                elif int_ES_b>0:
                    if bool_ES_a_is_0:
                        str_ES_equation += f'{int_ES_b}'
                    else:
                        str_ES_equation += f'+{int_ES_b}'
                else: #b<0
                    str_ES_equation += f'{int_ES_b}'

                str_ES_equation += '='

                if int_ES_c == 0:
                    bool_ES_c_is_0 = True
                elif int_ES_c == 1:
                    str_ES_equation += 'x'
                else:
                    str_ES_equation += f'{int_ES_c}x'

                if int_ES_d == 0:
                    if bool_ES_c_is_0:
                        str_ES_equation += '0'
                    else:
                        pass
                elif int_ES_d>0:
                    if bool_ES_c_is_0:
                        str_ES_equation += f'{int_ES_d}'
                    else:
                        str_ES_equation += f'+{int_ES_d}'
                else: #d<0
                    str_ES_equation += f'{int_ES_d}'

                print(str_ES_equation)

                if int_ES_a == int_ES_c:
                    if int_ES_b != int_ES_d:
                        print("Contradiction! The equation has no solutions")
                    else:
                        print("Identity. The equation has infinite solutions")
                else:
                    str_ES_answer = (int_ES_d-int_ES_b) / (int_ES_a-int_ES_c)
                    
                    if str_ES_answer % 1 == 0:
                        str_ES_answer = int(str_ES_answer)
                    else:
                        str_ES_answer = float(str_ES_answer)

                    print("Answer: x=" + str(str_ES_answer))
                input("Press Enter to go back")
                clear_screen()

        elif str_ES_choice == '2':
            print("\n\tax^2+bx+c=0")
            
            int_ES_a = input("Input 'a' value: ")
            int_ES_b = input("Input 'b' value: ")
            int_ES_c = input("Input 'c' value: ")

            try:
                int_ES_a, int_ES_b, int_ES_c = int(int_ES_a), int(int_ES_b), int(int_ES_c)
            except:
                input("Error! Please input integers only.")
                clear_screen()
            else:

                int_ES_disc = int_ES_b**2 - 4*int_ES_a*int_ES_c

                str_ES_equation += 'Equation: '

                if int_ES_a == 1:
                    str_ES_equation += 'x^2'
                elif int_ES_a == 0:
                    bool_ES_a_is_0 = True
                elif int_ES_a == -1:
                    str_ES_equation += '-x^2'
                else:
                    str_ES_equation += f'{int_ES_a}x^2'

                if int_ES_b == 1:
                    str_ES_equation += '+x'
                elif int_ES_b == 0:
                    bool_ES_b_is_0 = True
                elif int_ES_b == -1:
                    str_ES_equation += '-x'
                elif int_ES_b > 0 and not bool_ES_a_is_0:
                    str_ES_equation += f'+{int_ES_b}x'
                else: #b<0 or a = 0
                    str_ES_equation += f'{int_ES_b}x'
                    
                if bool_ES_b_is_0 and bool_ES_a_is_0:
                    str_ES_equation += f'{int_ES_c}'
                else: #not both of them are 0
                    if int_ES_c > 0:
                        str_ES_equation += f'+{int_ES_c}'
                    elif int_ES_c == 0:
                        pass
                    else: #c<0
                        str_ES_equation += f'{int_ES_c}'

                str_ES_equation += '=0'

                print(str_ES_equation)
                
                if int_ES_a == 0 and int_ES_b ==0:
                    if int_ES_c == 0:
                        print("Identity. The equation has infinite solutions.")
                    else:
                        print("Contradiction! The equation has no solution.")
                else:
                    int_ES_a, int_ES_b, int_ES_c = Fraction(int_ES_a), Fraction(int_ES_b), Fraction(int_ES_c)
                    
                    if int_ES_a == 0:
                        str_ES_answer = (-int_ES_c)/int_ES_b
                        try:
                            float(str_ES_answer)
                        except:
                            pass
                        else:
                            if str_ES_answer % 1 == 0:
                                str_ES_answer = int(str_ES_answer)
                            else:
                                str_ES_answer = Fraction(str_ES_answer)
                                str_ES_answer = Fraction.limit_denominator(str_ES_answer)

                        print("Answer: x=" + str(str_ES_answer))
                    else:
                        if int_ES_disc < 0:
                        
                            int_ES_const = -int_ES_b
                            int_ES_imag_part_coeff = ES_sqrt_coeff(-int_ES_disc)
                            int_ES_imag_part_radicand = ES_sqrt_radicand(-int_ES_disc)
                            int_ES_denom = 2*int_ES_a

                            int_ES_GCD = math.gcd(int(int_ES_const), int(int_ES_imag_part_coeff), int(int_ES_denom))
                        
                            if int_ES_GCD != 1:
                            
                                int_ES_const /= int_ES_GCD
                                int_ES_imag_part_coeff /= int_ES_GCD
                                int_ES_denom /= int_ES_GCD

                                int_ES_const = int(int_ES_const)
                                int_ES_imag_part_coeff = int(int_ES_imag_part_coeff)
                                int_ES_denom = int(int_ES_denom)

                            if int_ES_denom < 0:
                                int_ES_denom *= -1
                                int_ES_const *= -1
                                int_ES_imag_part_coeff *= -1

                            if int_ES_imag_part_radicand == 1:
                                if int_ES_imag_part_coeff == 1:
                                    if int_ES_denom == 1:
                                        if int_ES_const == 0:
                                            print("Answer: x=±i")
                                        else: #int_ES_const != 0
                                            print(f"Answer: x={int_ES_const}±i")
                                    else: #denominator != 1
                                        if int_ES_const == 0:
                                            print(f"Answer: x=±i/{int_ES_denom}")
                                        else: #int_ES_const != 0
                                            print(f"Answer: x=({int_ES_const}±i)/{int_ES_denom}")
                                else: #imaginary part coefficient != 1
                                    if int_ES_denom == 1:
                                        if int_ES_const == 0:
                                            print(f"Answer: x=±{int_ES_imag_part_coeff}i")
                                        else: #int_ES_const != 0
                                            print(f"Answer: x={int_ES_const}±{int_ES_imag_part_coeff}i")
                                    else: #denominator != 1
                                        if int_ES_const == 0:
                                            print(f"Answer: x=±{int_ES_imag_part_coeff}i/{int_ES_denom}")
                                        else: #int_ES_const != 0
                                            print(f"Answer: x=({int_ES_const}±{int_ES_imag_part_coeff}i)/{int_ES_denom}")
                            else: #imaginary part radical != 1
                                if int_ES_imag_part_coeff == 1:
                                    if int_ES_denom == 1:
                                        if int_ES_const == 0:
                                            print(f"Answer: x=±sqrt({int_ES_imag_part_radicand})i")
                                        else: #int_ES_const != 0
                                            print(f"Answer: x={int_ES_const}±sqrt({int_ES_imag_part_radicand})i")
                                    else: #denominator != 1
                                        if int_ES_const == 0:
                                            print(f"Answer: x=±sqrt({int_ES_imag_part_radicand})i/{int_ES_denom}")
                                        else: #int_ES_const != 0
                                            print(f"Answer: x=({int_ES_const}±sqrt({int_ES_imag_part_radicand})i)/{int_ES_denom}")
                                else: #imaginary part coefficient != 1
                                    if int_ES_denom == 1:
                                        if int_ES_const == 0:
                                            print(f"Answer: x=±{int_ES_imag_part_coeff}sqrt({int_ES_imag_part_radicand})i")
                                        else: #int_ES_const != 0
                                            print(f"Answer: x={int_ES_const}±{int_ES_imag_part_coeff}sqrt({int_ES_imag_part_radicand})i")
                                    else: #denominator != 1
                                        if int_ES_const == 0:
                                            print(f"Answer: x=±{int_ES_imag_part_coeff}sqrt({int_ES_imag_part_radicand})i/{int_ES_denom}")
                                        else: #int_ES_const != 0
                                            print(f"Answer: x=({int_ES_const}±{int_ES_imag_part_coeff}sqrt({int_ES_imag_part_radicand})i)/{int_ES_denom}")
                                    
                        elif int_ES_disc == 0:

                            int_ES_const = -int_ES_b
                            int_ES_denom = 2*int_ES_a
                        
                            int_ES_GCD = math.gcd(int(int_ES_const), int(int_ES_denom))
                        
                            if int_ES_GCD != 1:
                                int_ES_const /= int_ES_GCD
                                int_ES_denom /= int_ES_GCD

                                int_ES_const = int(int_ES_const)
                                int_ES_denom = int(int_ES_denom)

                            if int_ES_denom < 0:
                                int_ES_denom *= -1
                                int_ES_const *= -1

                            if int_ES_const == 0:
                                print(f"Answer: x=0")
                            else:
                                if int_ES_denom == 1:
                                    print(f"Answer: x={int_ES_const}")
                                else:
                                    print(f"Answer: x={int_ES_const}/{int_ES_denom}")

                        else: #disc > 0

                            int_ES_const = -int_ES_b
                            int_ES_denom = 2*int_ES_a

                            int_ES_root1 = (int_ES_const + math.sqrt(int_ES_disc)) / int_ES_denom
                            int_ES_root2 = (int_ES_const - math.sqrt(int_ES_disc)) / int_ES_denom

                            if math.sqrt(int_ES_disc) % 1 == 0:
                                int_ES_root1, int_ES_root2 = Fraction(int_ES_root1), Fraction(int_ES_root2)
                                int_ES_root1, int_ES_root2 = Fraction.limit_denominator(int_ES_root1), Fraction.limit_denominator(int_ES_root2)
                            
                            if int_ES_root1 % 1 == 0:
                                int_ES_root1 = int(int_ES_root1)

                            if int_ES_root2 % 1 == 0:
                                int_ES_root2 = int(int_ES_root2)

                            print(f"Answer: x={int_ES_root1} or x={int_ES_root2}")
                        
                input("Press Enter to go back")
                clear_screen()
                        
        elif str_ES_choice == '3':
            print("\n\tax+by+c=0, dx+fy+g=0")

            int_ES_a = input("Input 'a' value: ")
            int_ES_b = input("Input 'b' value: ")
            int_ES_c = input("Input 'c' value: ")
            int_ES_d = input("Input 'd' value: ")
            int_ES_f = input("Input 'f' value: ")
            int_ES_g = input("Input 'g' value: ")

            try:
                int_ES_a, int_ES_b, int_ES_c, int_ES_d, int_ES_f, int_ES_g = int(int_ES_a), int(int_ES_b), int(int_ES_c), int(int_ES_d), int(int_ES_f), int(int_ES_g)
            except:
                input("Error! Please input integers only.")
                clear_screen()
            else:
                str_ES_equation += 'Equations: '

                if int_ES_a == 0:
                    bool_ES_a_is_0 = True
                elif int_ES_a == 1:
                    str_ES_equation += 'x'
                elif int_ES_a == -1:
                    str_ES_equation += '-x'
                else:
                    str_ES_equation += f'{int_ES_a}x'

                if int_ES_b == 0:
                    bool_ES_b_is_0 = True
                elif int_ES_b == -1:
                    str_ES_equation += '-y'
                elif int_ES_b < 0:
                    str_ES_equation += f'{int_ES_b}y'
                elif bool_ES_a_is_0:
                    if int_ES_b == 1:
                        str_ES_equation += 'y'
                    else: #b>0
                        str_ES_equation += f'{int_ES_b}y'
                else: #a != 0, b>=1
                    if int_ES_b == 1:
                        str_ES_equation += '+y'
                    else: #b>0
                        str_ES_equation += f'+{int_ES_b}y'

                if bool_ES_b_is_0 and bool_ES_a_is_0:
                    str_ES_equation += f'{int_ES_c}'
                else: #not both of them are 0
                    if int_ES_c > 0:
                        str_ES_equation += f'+{int_ES_c}'
                    elif int_ES_c == 0:
                        pass
                    else: #c<0
                        str_ES_equation += f'{int_ES_c}'

                str_ES_equation += '=0, '

                if int_ES_d == 0:
                    bool_ES_d_is_0 = True
                elif int_ES_d == 1:
                    str_ES_equation += 'x'
                elif int_ES_d == -1:
                    str_ES_equation += '-x'
                else:
                    str_ES_equation += f'{int_ES_d}x'

                if int_ES_f == 0:
                    bool_ES_f_is_0 = True
                elif int_ES_f == -1:
                    str_ES_equation += '-y'
                elif int_ES_f < 0:
                    str_ES_equation += f'{int_ES_f}y'
                elif bool_ES_d_is_0:
                    if int_ES_f == 1:
                        str_ES_equation += 'y'
                    else: #f>0
                        str_ES_equation += f'{int_ES_f}y'
                else: #d != 0, f>=1
                    if int_ES_f == 1:
                        str_ES_equation += '+y'
                    else: #f>0
                        str_ES_equation += f'+{int_ES_f}y'

                if bool_ES_d_is_0 and bool_ES_f_is_0:
                    str_ES_equation += f'{int_ES_g}'
                else: #not both of them are 0
                    if int_ES_g > 0:
                        str_ES_equation += f'+{int_ES_g}'
                    elif int_ES_g == 0:
                        pass
                    else: #g<0
                        str_ES_equation += f'{int_ES_g}'

                str_ES_equation += '=0'

                print(str_ES_equation)

                if bool_ES_a_is_0 and bool_ES_b_is_0:
                    if int_ES_c == 0:
                        bool_ES_EQ1_iden = True
                    else:
                        bool_ES_EQ1_contr = True

                if bool_ES_d_is_0 and bool_ES_f_is_0:
                    if int_ES_g == 0:
                        bool_ES_EQ2_iden = True
                    else:
                        bool_ES_EQ2_contr = True

                if bool_ES_EQ1_contr or bool_ES_EQ2_contr:
                    print("The system has no solution.")
                elif bool_ES_EQ1_iden and bool_ES_EQ2_iden:
                    print("The system has infinite solutions.  Any point satisfies the system.")
                elif bool_ES_EQ1_iden:
                    int_ES_GCD = math.gcd(int_ES_d, int_ES_f, int_ES_g)

                    if int_ES_GCD != 1:
                        int_ES_d /= int_ES_GCD
                        int_ES_f /= int_ES_GCD
                        int_ES_g /= int_ES_GCD

                        int_ES_d = int(int_ES_d)
                        int_ES_f = int(int_ES_f)
                        int_ES_g = int(int_ES_g)

                    str_ES_answer = 'Answer: {(x,y) | '

                    if int_ES_d == 0:
                        pass
                    elif int_ES_d == 1:
                        str_ES_answer += 'x'
                    else:
                        str_ES_answer += f'{int_ES_d}x'

                    if int_ES_f == 0:
                        bool_ES_f_is_0 = True
                    elif int_ES_f == -1:
                        str_ES_answer += '-y'
                    elif int_ES_f < 0:
                        str_ES_answer += f'{int_ES_f}y'
                    elif bool_ES_d_is_0:
                        if int_ES_f == 1:
                            str_ES_answer += 'y'
                        else: #f>0
                            str_ES_answer += f'{int_ES_f}y'
                    else: #d != 0, f>=1
                        if int_ES_f == 1:
                            str_ES_answer += '+y'
                        else: #f>0
                            str_ES_answer += f'+{int_ES_f}y'

                    if bool_ES_d_is_0 and bool_ES_f_is_0:
                        str_ES_answer += f'{int_ES_g}'
                    else: #not both of them are 0
                        if int_ES_g > 0:
                            str_ES_answer += f'+{int_ES_g}'
                        elif int_ES_g == 0:
                            pass
                        else: #g<0
                            str_ES_answer += f'{int_ES_g}'

                    str_ES_answer += '=0}'
                    print(str_ES_answer)
                elif bool_ES_EQ2_iden:
                    int_ES_GCD = math.gcd(int_ES_a, int_ES_b, int_ES_c)

                    if int_ES_GCD != 1:
                        int_ES_a /= int_ES_GCD
                        int_ES_b /= int_ES_GCD
                        int_ES_c /= int_ES_GCD

                        int_ES_a = int(int_ES_a)
                        int_ES_b = int(int_ES_b)
                        int_ES_c = int(int_ES_c)

                    str_ES_answer = 'Answer: {(x,y) | '

                    if int_ES_a == 0:
                        pass
                    elif int_ES_a == 1:
                        str_ES_answer += 'x'
                    else:
                        str_ES_answer += f'{int_ES_a}x'

                    if int_ES_b == 0:
                        bool_ES_b_is_0 = True
                    elif int_ES_b == -1:
                        str_ES_answer += '-y'
                    elif int_ES_b < 0:
                        str_ES_answer += f'{int_ES_b}y'
                    elif bool_ES_a_is_0:
                        if int_ES_b == 1:
                            str_ES_answer += 'y'
                        else: #b>0
                            str_ES_answer += f'{int_ES_b}y'
                    else: #a != 0, b>=1
                        if int_ES_b == 1:
                            str_ES_answer += '+y'
                        else: #b>0
                            str_ES_answer += f'+{int_ES_b}y'

                    if bool_ES_b_is_0 and bool_ES_a_is_0:
                        str_ES_answer += f'{int_ES_c}'
                    else: #not both of them are 0
                        if int_ES_c > 0:
                            str_ES_answer += f'+{int_ES_c}'
                        elif int_ES_c == 0:
                            pass
                        else: #c<0
                            str_ES_answer += f'{int_ES_c}'

                    str_ES_answer += '=0}'
                    print(str_ES_answer)
                else: #both are conditional
                    int_ES_a, int_ES_b, int_ES_c, int_ES_d, int_ES_f, int_ES_g = Fraction(int_ES_a), Fraction(int_ES_b), Fraction(int_ES_c), Fraction(int_ES_d), Fraction(int_ES_f), Fraction(int_ES_g)
                    
                    if int_ES_b != 0:
                        int_ES_slope_EQ1 = -int_ES_a / int_ES_b
                        int_ES_yint_EQ1 = -int_ES_c / int_ES_b
                    else:
                        int_ES_slope_EQ1 = 'undefined'
                        int_ES_yint_EQ1 = 'undefined'

                    if int_ES_f != 0:
                        int_ES_slope_EQ2 = -int_ES_d / int_ES_f
                        int_ES_yint_EQ2 = -int_ES_g / int_ES_f
                    else:
                        int_ES_slope_EQ2 = 'undefined'
                        int_ES_yint_EQ2 = 'undefined'

                    if int_ES_slope_EQ1 == int_ES_slope_EQ2 and int_ES_slope_EQ1 != 'undefined' and int_ES_slope_EQ2 != 'undefined':
                        if int_ES_yint_EQ1 == int_ES_yint_EQ2: #coinciding lines
                            int_ES_d, int_ES_f, int_ES_g = int(int_ES_d), int(int_ES_f), int(int_ES_g)
                            
                            int_ES_GCD = math.gcd(int_ES_d, int_ES_f, int_ES_g)

                            if int_ES_GCD != 1:
                                int_ES_d /= int_ES_GCD
                                int_ES_f /= int_ES_GCD
                                int_ES_g /= int_ES_GCD

                                int_ES_d = int(int_ES_d)
                                int_ES_f = int(int_ES_f)
                                int_ES_g = int(int_ES_g)

                            str_ES_answer = 'The two lines are coinciding, the solution set is {(x,y) | '

                            if int_ES_d == 0:
                                pass
                            elif int_ES_d == 1:
                                str_ES_answer += 'x'
                            else:
                                str_ES_answer += f'{int_ES_d}x'

                            if int_ES_f == 0:
                                bool_ES_f_is_0 = True
                            elif int_ES_f == -1:
                                str_ES_answer += '-y'
                            elif int_ES_f < 0:
                                str_ES_answer += f'{int_ES_f}y'
                            elif bool_ES_d_is_0:
                                if int_ES_f == 1:
                                    str_ES_answer += 'y'
                                else: #f>0
                                    str_ES_answer += f'{int_ES_f}y'
                            else: #d != 0, f>=1
                                if int_ES_f == 1:
                                    str_ES_answer += '+y'
                                else: #f>0
                                    str_ES_answer += f'+{int_ES_f}y'

                            if bool_ES_d_is_0 and bool_ES_f_is_0:
                                str_ES_answer += f'{int_ES_g}'
                            else: #not both of them are 0
                                if int_ES_g > 0:
                                    str_ES_answer += f'+{int_ES_g}'
                                elif int_ES_g == 0:
                                    pass
                                else: #g<0
                                    str_ES_answer += f'{int_ES_g}'

                            str_ES_answer += '=0}'
                            print(str_ES_answer)
                        else: #parallel lines
                            print("The two lines are parallel and don't intersect, the solution set is {}")
                    elif int_ES_slope_EQ1 == int_ES_slope_EQ2: #both slopes are undefined
                        if int_ES_c == int_ES_g:
                            int_ES_d, int_ES_f, int_ES_g = int(int_ES_d), int(int_ES_f), int(int_ES_g)
                            
                            int_ES_GCD = math.gcd(int_ES_d, int_ES_f, int_ES_g)

                            if int_ES_GCD != 1:
                                int_ES_d /= int_ES_GCD
                                int_ES_f /= int_ES_GCD
                                int_ES_g /= int_ES_GCD

                                int_ES_d = int(int_ES_d)
                                int_ES_f = int(int_ES_f)
                                int_ES_g = int(int_ES_g)

                            str_ES_answer = 'The two lines are coinciding, the solution set is {(x,y) | '

                            if int_ES_d == 0:
                                pass
                            elif int_ES_d == 1:
                                str_ES_answer += 'x'
                            else:
                                str_ES_answer += f'{int_ES_d}x'

                            #f is always 0
                            bool_ES_f_is_0 = True

                            if bool_ES_d_is_0 and bool_ES_f_is_0:
                                str_ES_answer += f'{int_ES_g}'
                            else: #not both of them are 0
                                if int_ES_g > 0:
                                    str_ES_answer += f'+{int_ES_g}'
                                elif int_ES_g == 0:
                                    pass
                                else: #g<0
                                    str_ES_answer += f'{int_ES_g}'

                            str_ES_answer += '=0}'
                            print(str_ES_answer)
                        else: #Parallel Vertical
                            print("The two lines are parallel and don't intersect, the solution set is {}")
                    else: #intersecting lines
                        if int_ES_slope_EQ1 == 'undefined':
                            int_ES_xcoord = -int_ES_c / int_ES_a
                            int_ES_ycoord = (int_ES_c*int_ES_d) / (int_ES_a*int_ES_f) - int_ES_g/int_ES_f
                        elif int_ES_slope_EQ2 == 'undefined':
                            int_ES_xcoord = -int_ES_g / int_ES_d
                            int_ES_ycoord = (int_ES_a*int_ES_g) / (int_ES_b*int_ES_d) - int_ES_c/int_ES_b
                        else:
                            int_ES_xcoord = (int_ES_yint_EQ2-int_ES_yint_EQ1) / (int_ES_slope_EQ1-int_ES_slope_EQ2)
                            int_ES_ycoord = -int_ES_a*int_ES_xcoord/int_ES_b - int_ES_c/int_ES_b

                        if int_ES_xcoord % 1 == 0:
                            int_ES_xcoord = Fraction(int_ES_xcoord)
                        if int_ES_ycoord % 1 == 0:
                            int_ES_ycoord = Fraction(int_ES_ycoord)
                            
                        print(f"Answer: ({int_ES_xcoord}, {int_ES_ycoord})")
                    
                input("Press Enter to go back")
                clear_screen()

        elif str_ES_choice == '4':
            
            int_ES_angle = input("Input your angle (in degrees): ")
            int_ES_og_angle = int_ES_angle

            while True:
                try:
                    int(int_ES_angle)
                except:
                    print("Angle must be an integer! Please try again.")
                    int_ES_angle = input("Input your angle: ")
                else:
                    int_ES_angle, int_ES_og_angle = int(int_ES_angle), int(int_ES_og_angle)
                    break

            print("\nGiven angle:", int_ES_angle, "degrees")
            int_ES_angle %= 360
            int_ES_og_angle %= 360
            print("Reduced angle:", int_ES_angle, "degrees")

            if int_ES_angle <= 90:
                #angle = angle
                pass
            elif int_ES_angle <= 180:
                int_ES_angle = 180 - int_ES_angle
            elif int_ES_angle <= 270:
                int_ES_angle = int_ES_angle - 180
            else: #int_ES_angle >= 270
                int_ES_angle = 360 - int_ES_angle

            if int_ES_angle == 0:
                float_ES_sin = 0
                float_ES_cos = 1
                float_ES_tan = 0
            elif int_ES_angle == 15:
                float_ES_sin = (math.sqrt(6)-math.sqrt(4)) / 4
                float_ES_cos = (math.sqrt(6)+math.sqrt(4)) / 4
                float_ES_tan = 2-math.sqrt(3)
            elif int_ES_angle == 30:
                float_ES_sin = 1/2
                float_ES_cos = math.sqrt(3) / 2
                float_ES_tan = math.sqrt(3) / 3
            elif int_ES_angle == 45:
                float_ES_sin = math.sqrt(2) / 2
                float_ES_cos = math.sqrt(2) / 2
                float_ES_tan = 1
            elif int_ES_angle == 60:
                float_ES_sin = math.sqrt(3) / 2
                float_ES_cos = 1/2
                float_ES_tan = math.sqrt(3)
            elif int_ES_angle == 75:
                float_ES_sin = (math.sqrt(6)+math.sqrt(4)) / 4
                float_ES_cos = (math.sqrt(6)-math.sqrt(4)) / 4
                float_ES_tan = 2+math.sqrt(3)
            elif int_ES_angle == 90:
                float_ES_sin = 1
                float_ES_cos = 0
                float_ES_tan = 'undefined'
            else: #angle is not a 'nice' number
                int_ES_angle *= math.pi/180
                float_ES_sin = math.sin(int_ES_angle)
                float_ES_cos = math.cos(int_ES_angle)
                float_ES_tan = math.tan(int_ES_angle)

            if float_ES_sin == 0:
                float_ES_csc = 'undefined'
            else:
                float_ES_csc = 1 / float(float_ES_sin)
                float_ES_sin, float_ES_csc = round(float_ES_sin, 8), round(float_ES_csc, 8)

            if float_ES_cos == 0:
                float_ES_sec = 'undefined'
            else:
                float_ES_sec = 1 / float(float_ES_cos)
                float_ES_cos, float_ES_sec = round(float_ES_cos, 8), round(float_ES_sec, 8)

            if float_ES_tan == 0:
                float_ES_cot = 'undefined'
            elif float_ES_tan == 'undefined':
                float_ES_cot = 0
            else:
                float_ES_cot = 1 / float(float_ES_tan)
                float_ES_tan, float_ES_cot = round(float_ES_tan, 8), round(float_ES_cot, 8)

            if int_ES_og_angle <= 90:
                pass #no sign changes
            elif int_ES_og_angle <= 180: #sign change is cos, sec, tan, cot
                
                if float_ES_cos == 0:
                    pass #-0=0
                else:
                    float_ES_cos *= -1
                
                if float_ES_sec == 'undefined':
                    pass #-und=und
                else:
                    float_ES_sec *= -1

                if float_ES_tan == '0' or float_ES_tan == 'undefined':
                    pass #-0=0, -und=und
                else:
                    float_ES_tan *= -1

                if float_ES_cot == '0' or float_ES_cot == 'undefined':
                    pass #-0=0, -und=und
                else:
                    float_ES_cot *= -1
                    
            elif int_ES_og_angle <= 270: #sign change is sin, csc, cos, sec
                
                if float_ES_sin == 0:
                    pass #-0=0
                else:
                    float_ES_sin *= -1
                
                if float_ES_csc == 'undefined':
                    pass #-und=und
                else:
                    float_ES_csc *= -1

                if float_ES_cos == 0:
                    pass #-0=0
                else:
                    float_ES_cos *= -1
                
                if float_ES_sec == 'undefined':
                    pass #-und=und
                else:
                    float_ES_sec *= -1

            else: #angle > 270 -> sign change is sin, csc, tan, cot

                if float_ES_sin == 0:
                    pass #-0=0
                else:
                    float_ES_sin *= -1
                
                if float_ES_csc == 'undefined':
                    pass #-und=und
                else:
                    float_ES_csc *= -1

                if float_ES_tan == '0' or float_ES_tan == 'undefined':
                    pass #-0=0, -und=und
                else:
                    float_ES_tan *= -1

                if float_ES_cot == '0' or float_ES_cot == 'undefined':
                    pass #-0=0, -und=und
                else:
                    float_ES_cot *= -1

            if float_ES_csc == 'undefined':
                pass
            elif int(float_ES_csc) != float_ES_csc:
                pass
            else:
                float_ES_csc = int(float_ES_csc)

            if float_ES_sec == 'undefined':
                pass
            elif int(float_ES_sec) != float_ES_sec:
                pass
            else:
                float_ES_sec = int(float_ES_sec)

            if float_ES_cot == 'undefined':
                pass
            elif int(float_ES_cot) != float_ES_cot:
                pass
            else:
                float_ES_cot = int(float_ES_cot)


            print("\n\tSine:", float_ES_sin)
            print("\tCosine:", float_ES_cos)
            print("\tTangent:", float_ES_tan)
            print("\tCosecant:", float_ES_csc)
            print("\tSecant:", float_ES_sec)
            print("\tCotangent:", float_ES_cot)
            print("")
            
            input("Press Enter to go back")
            clear_screen()
            
        else: #choice = 5
            input("Thank you for using the Equation Solver! :D")
            clear_screen()
            return

def Math_Game():
    while True:
        clear_screen()
        
        str_MG_choice = ''
        int_MG_num1 = 0
        int_MG_num2 = 0
        int_MG_score = 0
        int_MG_Qnum = 1
        int_MG_user_ans = 0
        int_MG_ans = 0

        str_MG_rand_mode = ''
        str_MG_proceed = ''
    
        print("Math Game :D")
        print("\tSelect Operation:")
        print("\t1. Addition")
        print("\t2. Subtraction")
        print("\t3. Multiplication")
        print("\t4. Division")
        print("\t5. Powers")
        print("\t6. Assorted Operations")
        print("\t7. Back to Main Menu")
        str_MG_choice = input("What is your choice? ")

        while str_MG_choice not in ['1', '2', '3', '4', '5', '6', '7']:
            print("Invalid Choice! Please try again.")
            str_MG_choice = input("Your Choice: ")

        dict_MG_modes = {
            '1': ('+', operator.add, -100, 100),
            '2': ('-', operator.sub, -100, 100),
            '3': ('*', operator.mul, -25, 25),
            '5': ('^', operator.pow, 2, 16)
        }

        while str_MG_proceed != 'n':
            int_MG_num1 = 0
            int_MG_num2 = 0
            int_MG_user_ans = 0
            int_MG_ans = 0
            int_MG_user_ans = 0

            if str_MG_choice == '7':
                input("Thank you for playing the game! :D")
                clear_screen()
                return

            elif str_MG_choice == '4':
                int_MG_ans = random.randint(-15, 15)
                int_MG_num2 = random.randint(-50, 50)
                while int_MG_ans in [0, 1, -1] or int_MG_num2 == 0:
                    int_MG_ans, int_MG_num2 = random.randint(-15, 15), random.randint(-50, 50)

                int_MG_num1 = int_MG_ans * int_MG_num2
                symbol = '/'
                
            elif str_MG_choice == '5':
                int_MG_num1 = random.randint(2, 16)
                int_MG_num2 = random.randint(2, 4)

                symbol, operand, _, _ = dict_MG_modes[str_MG_choice]

                int_MG_ans = operand(int_MG_num1, int_MG_num2)

            elif str_MG_choice in ['1', '2', '3']:
                symbol, operand, lowbound, upbound = dict_MG_modes[str_MG_choice]

                int_MG_num1 = random.randint(lowbound, upbound)
                int_MG_num2 = random.randint(lowbound, upbound)

                int_MG_ans = operand(int_MG_num1, int_MG_num2)
                
            elif str_MG_choice == '6':
                str_MG_rand_mode = str(random.randint(1, 5))
                
                if str_MG_rand_mode == '4':
                    int_MG_ans = random.randint(-15, 15)
                    int_MG_num2 = random.randint(-50, 50)
                    while int_MG_ans in [0, 1, -1] or int_MG_num2 == 0:
                        int_MG_ans, int_MG_num2 = random.randint(-15, 15), random.randint(-50, 50)

                    int_MG_num1 = int_MG_ans * int_MG_num2
                    symbol = '/'
                elif str_MG_rand_mode == '5':
                    int_MG_num1 = random.randint(2, 16)
                    int_MG_num2 = random.randint(2, 4)

                    symbol, operand, _, _ = dict_MG_modes[str_MG_rand_mode]

                    int_MG_ans = operand(int_MG_num1, int_MG_num2)
                else:
                    symbol, operand, lowbound, upbound = dict_MG_modes[str_MG_rand_mode]
                    int_MG_num1 = random.randint(lowbound, upbound)
                    int_MG_num2 = random.randint(lowbound, upbound)

                    int_MG_ans = operand(int_MG_num1, int_MG_num2)
            else:
                input("Thank you for playing the game! :D")
                return

            for i in range(0, 15):
                print("")
            
            print(f"Current Score: {int_MG_score}\n")
            print(f"\tQuestion {int_MG_Qnum}: {int_MG_num1} {symbol} {int_MG_num2}")
            int_MG_user_ans = input("\tAnswer: ")

            try:
                float(int_MG_user_ans)
            except:
                print("\nInvalid input! -3 pts")
                int_MG_score -= 3
            else:
                int_MG_user_ans = float(int_MG_user_ans)
                if int_MG_user_ans % 1 == 0:
                    int_MG_user_ans = int(int_MG_user_ans)
                else:
                    pass
                
                if int_MG_user_ans == int_MG_ans:
                    print("\nCorrect! +5 pts")
                    int_MG_score += 5
                else:
                    print("\nWrong! -3 pts")
                    int_MG_score -= 3

            int_MG_Qnum += 1

            str_MG_proceed = input("\nType n to stop the game:")
            if str_MG_proceed != 'n':
                for i in range(0, 15):
                    print("")
            else:
                print("\nGame Complete!")
                print(f"Final Score: {int_MG_score}")
                input("Press enter to proceed")
                break
    
main_menu()
