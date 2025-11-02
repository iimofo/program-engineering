
class Course:
    def __init__(self, title, duration_weeks):
        self.title = title
        self.duration_weeks = duration_weeks
        self.is_active = False

    def start_course(self):
        if not self.is_active:
            self.is_active = True
            print(f"✅ Курс '{self.title}' запущен. Продолжительность: {self.duration_weeks} недель.")
        else:
            print(f"❌ Курс '{self.title}' уже активен.")

programming_course = Course("Data Structures", 12)
programming_course.start_course()
programming_course.start_course()