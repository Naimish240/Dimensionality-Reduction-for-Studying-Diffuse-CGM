# -----------------------------
# Created on 25th March, 2021
# By Naimish Mani B
# -----------------------------
'''
This program contains all the modules required to yield the
required data for the model to train on, through generators.

It has the following methods:

    processLine
        Takes l (line) as input and returns that line, as a list

    getRow
        Generator to yield a row

    getBatch
        Takes SIZE as input, and yields a batch with SIZE elements
        in it for training.
'''
# Import Statements
from math import sqrt
# -----------------------------


# Converts the read line into a list for further processing
def processLine(l):
    '''
    Input:
        l : line to convert into array

    Output:
        l : list, after conversion
    '''
    l = l.split(',')
    l = [float(i) for i in l]
    return l


# Generator to yield each row at a time
def getRow():
    '''
    Output:
        Generator object, yields each row
    '''
    with open('../../HIGGS_6M.csv', 'r') as fh:
        # Replace with path to dataset locally
        try:
            while True:
                line = fh.readline()
                # print(line)
                row = processLine(line)
                # print(row)
                yield row
        # End of file reached
        except:
            return None


# Generator to yield a batch at a time
def getBatch(SIZE):
    try:
        while True:
            x = getRow()
            i = 0
            batch = []
            while i < SIZE:
                row = next(x)
                batch.append(row)
                i += 1
            yield batch
    # EoF
    except:
        return None


# Function to print the properties of the dataset
def printProperties():
    x = getRow()
    rows = 0
    # Lists to store the properties for each column
    maximum = [0] * 29
    minimum = [0] * 29
    total = [0] * 29

    try:
        # While loop to iterate through the dataset
        while True:
            r = next(x)
            rows += 1
            # Iterate through each element in the row
            for i in range(len(r)):
                # If element is less than minimum
                if r[i] < minimum[i]:
                    minimum[i] = r[i]
                # If element is greater than maximum
                if r[i] > maximum[i]:
                    maximum[i] = r[i]
                # Add element to total, to find average
                total[i] += r[i]
    except:
        print("Iterated through ", rows, "rows (basic properties)")

    # Calculate average
    mu = [i/rows for i in total]

    # Generate again, because we're iterating again
    x = getRow()

    # List to store variance
    variance = [0] * 29

    try:
        # While loop to iterate through the dataset
        while True:
            r = next(x)
            # Iterate through each element in the row to calculate variance
            for i in range(len(r)):
                variance[i] += (((r[i] - mu[i]) ** 2) / rows)

    except:
        print("Iterated through all rows")

    # Calculate standard deviation for the column
    sd = [sqrt(i) for i in variance]

    # Print all properties of each column
    for i in range(29):
        print("-----------------------------")
        print(i+1, "th column properties")
        print("Maximum element: ", maximum[i])
        print("Minimum element: ", minimum[i])
        print("Sum of all elements: ", total[i])
        print("Average value of column: ", mu[i])
        print("Variance of column: ", variance[i])
        print("Standard Deviation of column: ", sd[i])
    print("-----------------------------")


if __name__ == '__main__':
    # Test generator to see if it works
    x = getRow()
    print(next(x))
    print(next(x))
    # Deleting the generator, because we don't want any memory leaks
    del x

    # Test batch generator to see if it works
    x = getBatch(2)
    print(next(x))
    # Delete generator
    del x

    # Print the properties of the dataset
    printProperties()
