import sys


mean = 0
for elem in sys.argv[1:]:
    mean = mean + float(elem)

mean = mean / float(len(sys.argv) - 1)
print("Thoust's mean be:", mean)
word = input("insert a descriptor: ")
print("stev is a", word)
