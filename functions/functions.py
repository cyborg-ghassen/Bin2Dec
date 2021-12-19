# User input
def userInput():
    while True:
        x = input("Enter a binary number less than 8: ")
        if len(x) <= 8: break
    return x

# Calculate decimal number
def bin2dec(x):
    dec = 0
    for i in range(0, len(x)):
        if x[i] == "1":
            dec += pow(2, i)
        else:
            continue
    return dec