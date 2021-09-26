"""
Chaining Multiple Conditions


The university gives students discounts on tuition fees depending on their performance:
90-100 => 50%
80-89 => 30%
70-79 => 10%
0-69 => 0%
Write a program that will take the scores from the first and second semesters, then calculate the average score, and output the discount, depending on the score.

Sample Input
67
83

Sample Output
10

Explanation
Average of 67 and 83 is 75, which is in range of 70 to 79 and gets a 10% discount. Do not include the % symbol in the output.
"""

score1 = int(input())
score2 = int(input())
if (score1+score2)//2 >= 90:
    print(50)
elif (score1+score2)//2 >=80 and (score1+score2)//2 <=89:
    print(30)
elif (score1+score2)//2 >= 70 and (score1+score2)//2 <= 79:
    print(10)
elif (score1+score2)//2 <= 69:
    print(0)