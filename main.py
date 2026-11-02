""" In this assignment, you will build a Score List Explorer using recursion with lists. You will split a list into a head and tail, identify base cases, check whether
scores are sorted, calculate a recursive sum, and find the largest score without using built-in maximum functions."""

scores = [47, 62, 77, 90, 94]

print(f"Scores: {scores}")
print()

print("Head tail Pattern")
print(f"Head: {scores[0]}")
print(f"Tail: {scores[1:]}")
print()

print("Recursion for Lists")
print(f"Current List: {scores}")


def shrink(scoreList):
    if len(scoreList) == 1:
        print("Reached Base Case", scoreList)
        return
    
    shrink(scoreList[1:])

shrink(scores)
print()

print("Sorted Check")

def isSorted(scoreList):
    if len(scoreList) <= 1:
        return True

    if scoreList[0] > scoreList[1]:
        return False

    return isSorted(scoreList[1:])

print(f"Scores: {scores}")
print(f"Is Sorted: {isSorted(scores)}")

unsortedScores = [46, 90, 61, 77, 94]
print(f"Unsorted: {unsortedScores}")
print(f"Is sorted: {isSorted(unsortedScores)}")
print()

print("List Sum w/ Recursion")

def recursiveSum(scoreList):
    if len(scoreList) == 0:
        return 0

    return scoreList[0] + recursiveSum(scoreList[1:])

print(f"Total Score: {recursiveSum(scores)}")
print()

print("Largest Element")

def largestScore(scoreList):
    if len(scoreList) == 1:
        return scoreList[0]

    largestInTheTail = largestScore(scoreList[1:])

    if scoreList[0] > largestInTheTail:
        return scoreList[0]

    return largestInTheTail

print(f"Highest Score: {largestScore(scores)}")