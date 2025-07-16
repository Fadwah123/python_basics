print("Grade tracker")
student={"Alice":85,"Bob":92,"Charlie":78}
avg=0
sum=0
for i,j in student.items():
    sum=sum+j
avg=sum/3

print(f"Avergae grade:{avg}")
high=max(student.values())
for i,j in student.items():
    if j==high:
        print(f"Highest scorer:{i}({j})")
        break

low=min(student.values())
for i,j in student.items():
    if j==low:
        print(f"Lowest scorer:{i}({j})")
        break
