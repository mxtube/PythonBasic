"""
Lesson 36 - OOP
10.05.2023 @ Kirill Kuznetsov
"""


class StudyGroup:
    property1 = 'ISiP-15'
    property2 = 'S-12'
    name = 'guest'

    def say_hi(self, name=''):
        if name:
            return 'Hi, ' + name
        else:
            return 'Hello, ' + self.name


group = StudyGroup()
group2 = StudyGroup()
print(group)
print(group2)
# group.property1 = 'ISiP-15'  # No good
# group.property2 = 'ISiP-25'  # No good
print(group.property1)
print(group.property2)

print(group.say_hi('Kirill'))
print(group2.say_hi('Alex'))

print(group2.say_hi())


