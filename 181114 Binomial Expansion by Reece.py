""" Binomial expansion calculator. Takes an expression from the user and
returns the final expanded equation. This file includes an nCr calculator."""
import math

# returns the expression as a string
def expressionToExpand():
    exp = input("Please enter the expression in the form '(a+b)^n': ")
    return exp

# returns a tuple of the three numbers in the expression given by the user.
def findNumbersInExpression(toExpand):
    exp = toExpand
    bIsPositive = True

    # find if a + or - is used for the 'b' term.
    if exp.find("+") >= 0:
        a = exp[1 : exp.find("+")]
        bIsPositive = True
    else:
        a = exp[1 : exp.find("-")]
        bIsPositive = False

    
    if bIsPositive:
        b = exp[exp.find("+")+1 : exp.find(")")]
    else:
        b = exp[exp.find("-") : exp.find(")")]


    n = exp[exp.find("^")+1 :]


    values = (a, b, n)
    return values


# values is a parameter as nCr requires an 'n' value.    
def nCr(values):
    n = int(values[2])
    nFactorial = int(math.factorial(n))
    triangle = []

    for r in range(0, n + 1):
        triangleValues = nFactorial / (math.factorial(n - r) * math.factorial(r))
        triangle.append(triangleValues)

    return triangle

# returns unsimplified version of the expanded binomial.
def equation(nCrCoefficients, values):
    a = values[0]
    b = values[1]
    n = int(values[2])

    theBinomial = ""
    
    for i in range(0, n + 1):
        toAdd = str("({}*({})^({})*({})^({}))".format(int(nCrCoefficients[i]), a, n-i, b, i))
        if i == n:
            theBinomial = theBinomial + toAdd
        else:
            theBinomial = theBinomial + toAdd + " + "
    return theBinomial



### MAIN PROGRAM ###
if __name__ == "__main__":
    toExpand = expressionToExpand()
    values = findNumbersInExpression(toExpand)
    coefficients = nCr(values)
    answer = equation(coefficients, values)

    print(answer)
