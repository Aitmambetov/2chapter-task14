'''
Given a list of numbers, find and print all elements that are an even number. In
this case use a for-loop that iterates over the list, and not over its indices! That
is, don't use range(На английском языке что бы Вы научились понимать )
'''
given = [3,4,58,56,54,55,676,76,5]
for elements in given:
    if elements % 2 == 0:
        print(elements)
