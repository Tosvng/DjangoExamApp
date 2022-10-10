from django.test import TestCase
from .onlinecourse.models import Course, Enrollment,Question,Choice, Instructor, Learner,Lesson , Submission

# Create your tests here.
class OnlineCourseTestCase(TestCase):
    def setUp(self):
        Course.objects.create(name ='Learning Django', description = 'Lets learn',pub_date ='12/09/2022', instructors = 'Raheem', users = 'Raheem', total_enrollment = 0)
        Instructor.objects.create(user='Raheem', full_time = True)
        Learner.objects.create(user='Raheem Learner', occupation = 'STUDENT')
        Lesson.objects.create(title ="Nothing", course= 'Learning Django', content="Empty line")
        Enrollment.objects.create(user='Raheem Learner', course='Learning Django')
        Question.objects.create(lesson='Nothing' ,question_text="What is good?", grade=100)
        Choice.objects.create(question="What is good?", choice_text='this is good', is_correct= True)
        Choice.objects.create(question="What is good?", choice_text='this is good', is_correct= True)
        Choice.objects.create(question="What is good?", choice_text='this is not good', is_correct= False)
        Choice.objects.create(question="What is good?", choice_text='this is not good', is_correct= False)
    def check_course(self):
        course_title = Course.objects.get(name ='Learning Django')
        self.assertEqual(course_title.name, 'Learning Django')
        self.assertNotEqual(course_title.name, 'LDjango')
    def check_lesson(self):
        course_title = Course.objects.get(name ='Learning Django')
        lesson = course_title.lesson_set.all()
        self.assertEqual(lesson[0].name, 'Nothing')
        self.assertNotEqual(lesson[0].name, 'no')
