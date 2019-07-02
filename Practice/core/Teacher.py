class Classes:
    def __init__(self, school, name, kind):
        self.school = school    # 学校
        self.name = name        # 班级名称
        self.kind = kind        # 班级科目


class Teacher:
    def __init__(self, name, classes, course):
        self.name = name
        self.classes = classes
        self.course = course

