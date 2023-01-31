class Student:
    def __init__(self, name, surname, group, grades, age, gender, nationality):
        print('init', name)
        self.name = name
        self.surname = surname
        self.group = group
        self.grades = grades  # оценки
        self.age = age
        self.gender = gender
        self.nationality = nationality

    def __new__(cls, *args, **kwargs):
        print('new')
        return super(Student, cls).__new__(cls)

    def __del__(self):
        print(self.name, 'is deleted')

    def introduce(self):
        print(f'Hi, I am {self.name} from group {self.group}')

    @staticmethod
    def say_hi(name):
        print('Hi,', name)

    def age_gender(self):
        print(f'Hi, I am {self.name}, {self.gender}, {self.age} years old')

    def grade(self):
        print(f'I am {self.name}, my grades is {self.grades}')

    def nation(self):
        print(f'I am {self.name}, {self.nationality}')


new_group = '11-250'
a = Student('Izida', 'Ivanova', new_group, '90,3', '18', 'female', 'tatar')
b = Student('Kate', 'Petrova', '11-210', '83,6', '19', 'female', 'russian')
a.age_gender()
a.grade()
a.nation()


class Collection:
    def __init__(self, list):
        self.list = list

    def __len__(self):
        return len(self.list)


list = ['Hi', 'Hello']
print(len(list))
collection = Collection(list)

print(len(collection))