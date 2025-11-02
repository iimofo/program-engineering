
class Course:
    def __init__(self, title, duration_weeks):
        self.title = title
        self.duration_weeks = duration_weeks

    def get_details(self):
        return f"Курс: {self.title}, Длительность: {self.duration_weeks} недель."

class OnlineCourse(Course):
    
    def __init__(self, title, duration_weeks, platform):
        super().__init__(title, duration_weeks)
        self.platform = platform 

    def publish_link(self):
        print(f"Курс опубликован на платформе: {self.platform}")
        
    def get_details(self):
        return f"Онлайн-курс: {self.title}, Платформа: {self.platform}, Длительность: {self.duration_weeks} недель."

web_dev_course = OnlineCourse("Frontend Web Dev", 10, "Coursera")

print(web_dev_course.get_details())

web_dev_course.publish_link()
