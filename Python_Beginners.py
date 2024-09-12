from datetime import datetime

class Python_Begineers:

    #1) count number of vowels in a string ###
    def count_vowels(input_string):
        count = 0
        for x in input_string:
            if x in 'aeiouAEIOU':
                count += 1
            else:
                continue
        print("No of vowels in string : %s" % count)
        return count

    #2) put a paragraph(collection of string) in alphabetical order . Number will be sorted fist then alphabets###
    def alphabet_order(input_string):
        l = input_string.lower().split()
        l.sort()
        m=" ".join(l)
        print("Alphabetically sorted paragraph is :\n %s"%m)
        return m

    #3) Error Handling ###
    def python_error(input):
        try :
            x = (input)/0
            print("Error encountered in execution: %s"%x)
        except ZeroDivisionError as e:
            print("Zero Division Error")
            print(e)
            return e
        except TypeError as e:
            print("Type Error")
            print(e)
            return e
        except ValueError as e:
            print("Value Error")
            print(e)
            return e

    #4) days between 2 days, this function uses a python module datetime ###
    def days_between(date1,date2):
        date1=datetime.strptime(date1,'%Y%m%d')
        date2 = datetime.strptime(date2, '%Y%m%d')
        difference = date2-date1
        print("Difference between two given dates is %s"%difference)
        return

    #5) Find the factorial for input number
    def factorial(n):
        fact = 1
        for n in range(n,1,-1):
            fact *= n
        print("Factorial of input number is: %s"%fact)
        return fact

    #6) Program to transpose a matrix using nested loop

    def transpose_matrix(input_matrix):
        rows = len((input_matrix) # this will give the length of matrix i.e number of rows
        columns = len(input_matrix[0]) # this will give the length of columns as first element of list of list will have the number of columns

        transpose_matrix = [[0 for _ in range(rows)] for _ in range(columns)]
        for i in range(rows):
            for j in range(columns):
                transpose_matrix [j][i] = matrix[i][j]
        return transpose_matrix