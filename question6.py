#Question 6 Task 1
#Calculate the value of a particular arithmetic expression twice: once normally, and once using parentheses. Compare the two results to see if they match.
expression1 = 3 + 2 * 4
expression2 = (3 + 2) * 4

print("Result without parentheses:", expression1)
print("Result with parentheses:", expression2)

if expression1 == expression2:
    print("The results match!")
else:
    print("The results do not match.")

#Question 6 Task 2
result = (12 + 5) > 10 or (3 * 6) == 18
#prediction: the outcome will be true 
print("The outcome of the expression is:", result)
