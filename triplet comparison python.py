""" COMPARING OF TRIPLETS
SAMPLE INPUT:
a0, a1, a2 =5 6 7
b0, b1, b2 = 3 6 10
SAMPLE OUTPUT WILL BE:
1 1 """
import sys

def solve(a0, a1, a2, b0, b1, b2):
    a0, a1, a2 = input().strip().split(' ')
    a0, a1, a2 = [int(a0), int(a1), int(a2)]
    b0, b1, b2 = input().strip().split(' ')
    b0, b1, b2 = [int(b0), int(b1), int(b2)]
    alice_score = (1 if a0>b0 else 0) + (1 if a1>b1 else 0) + (1 if a2>b2 else 0)
    bob_score = (1 if a0<b0 else 0) + (1 if a1<b1 else 0) + (1 if a2<b2 else 0)
    return (alice_score,bob_score)
    
result = solve(5,6,7,3,6,10)

print (" ".join(map(str, result)))

