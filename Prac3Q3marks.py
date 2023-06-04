#Given the following Python list, write a program that prints out all the elements of the list that are greater than or equal to 80.

marks = [80,39,79,81,79,70,84,57,66,86]

print(f"The {len(marks)} students scored {marks}.\nScores that qualify for 'A' grade are:")
for score in marks:
    if score>=80:
        print(score)

print(f"a) Marks in ascending order: {sorted(marks, reverse=False)}")
print(f"b) Marks in descending order: {sorted(marks, reverse=True)}")
print(f"c) Highest Mark: {max(marks)}")
print(f"d) Lowest Mark: {min(marks)}")

msg=f"e) Index(es) of students who failed: "
i=0
for score in marks:
    if score<50:
        msg+=str(i)+"\t"
    i+=1

print(msg)