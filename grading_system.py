def show_history() -> None:
    print("\n== Brief History of Python ==")
    print("Python was created by Guido van Rossum and first released in 1991.")
    print("It is known for its simplicity and readability.")
    print("Python supports multiple programming paradigms and is widely used in web development, data science, automation, and more.\n")

    print("== Program: Compute Average Score and Assign Grades to Students ==")


def get_names_scores() -> tuple[list[str], list[float]]:
    while True:
        try:
            count = int(input("Number of students: "))
            if count <= 0:
                print("Please input a number greater than zero.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    names_of_students = []
    scores = []

    print("\nEnter student names and scores:\n")

    for i in range(count):
        name = input(f'Student {i+1} name: ').strip()
        if not name:
            name = f'Student{i+1}'
        names_of_students.append(name)

        while True:
            try:
                score = float(input(f"Enter the score for {name}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Score must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    return names_of_students, scores

def greet_student(name: str) -> str:
    return (name.title())


def assign_grade(score: float) -> str:
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


def display_results(names: list[str], scores: list[float]) -> None:
    print("\n=== Student Results ===")
    for name, score in zip(names, scores):
        grade = assign_grade(score)
        print(f"{name}: Score = {score}, Grade = {grade}")

    average = sum(scores) / len(scores)
    print(f"\nClass Average Score: {average:.2f}")


# Run the program
if __name__ == "__main__":
    show_history()
    student_names, student_scores = get_names_scores()
    display_results(student_names, student_scores)