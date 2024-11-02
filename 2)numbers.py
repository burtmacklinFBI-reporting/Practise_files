#Q1) You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.

length = 92
breadth = 48.8
print(length*breadth)

#Q2) You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?

packets = 9
packet_cost = 1.49
total_cost = packets*packet_cost
total_given = 20
change = total_given - total_cost
print(change)

#Q3)You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles. Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)
print((5.5**2)*500)
print(5.5**2*500)


#Q4)Print binary representation of number 17

bnr = 17
print ( '10001')
print('{:b}'.format(bnr))
print(format(bnr,'b'))

# the format function can be used in many ways to convert the number into various types especially if the number in the curly braces is something that you want to format then using the format function is something that you can totally use. It is a great catch if you want to convert the numbers you want into binary numbers. Above are the two representations that you can use the format function to convert them into binary numbers.
