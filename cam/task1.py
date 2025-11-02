

class Course:
    def __init__(self, title, duration_weeks):
        self.title = title
        self.duration_weeks = duration_weeks
        print(f"Курс '{self.title}' создан.")

programming_course = Course("Python OOP Fundamentals", 8)
print(f"Длительность курса: {programming_course.duration_weeks} недель.")
