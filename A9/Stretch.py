def load_scores():
    scores = []
    with open("scores.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(". ", 1)
                    if len(parts) == 2:
                        name_score = parts[1].split(":")
                        if len(name_score) == 2:
                            name = name_score[0].strip()
                            score = int(name_score[1].strip())
                            scores.append({"name": name, "score": score})
    return scores

def save_scores(scores):
    with open("scores.txt", "w") as file:
        for i, entry in enumerate(scores, start=1):
            file.write(f"{i}. {entry['name']}: {entry['score']}\n")

def display_scores(scores, title="Current High Scores:"):
    print(f"{title}")
    for i, entry in enumerate(scores, start=1):
        print(f"{i}. {entry['name']}: {entry['score']}")


print("High Scores Tracker")
scores = load_scores()
display_scores(scores)

name = input("Enter your name: ")
score = int(input("Enter your score: "))
scores.append({"name": name, "score": score})

scores.sort(key=lambda x: x["score"], reverse=True)

save_scores(scores)
print("Score saved successfully!")
display_scores(scores, title="Updated High Scores:")
