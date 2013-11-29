# Tryton 

from trytond.model import ModelView, ModelSQL, fields
from trytond.pyson import Eval, If

__all__ = ['Student','Course','Distribution', 'Enrollment', 
           'StudentScore', 'Enrollment', 'GradeSheet']

STATES = {
    'readonly': ~Eval('active'),
    }

class Student(ModelView, ModelSQL):
    'Student'
    __name__ = 'op.student'
    
    firstname = fields.Char('Firstname')
    lastname = fields.Char('Lastname')
    major = fields.Char('Major')
    courses = fields.Many2Many('op.student-op.course',
            'student', 'course', 'Courses')

class Course(ModelView, ModelSQL):
    'Course'
    __name__ = 'op.course'
    
    name = fields.Char('Name')
    department = fields.Char('Department')
    major = fields.Char('Major')
    semester = fields.Char('Semester')
    year = fields.Char('Year')
    distributions = fields.One2Many('op.distribution', 'course', 
                                    'Distributions')
    students = fields.Many2Many('op.student-op.course',
            'course', 'student', 'Students', readonly=True)

class Distribution(ModelView, ModelSQL):
    'Distributions'
    __name__ = 'op.distribution'
    
    course = fields.Many2One('op.course', 'Assigments',
                             required=True)
    category = fields.Char('Category')
    percentage = fields.Char('Percentage')

class Enrollment(ModelView, ModelSQL):
    'Student Course Enrollment'
    __name__ = 'op.student-op.course'
    
    student = fields.Many2One('op.student', 'Student', ondelete='CASCADE',
            select=True, required=True)
    course = fields.Many2One('op.course', 'Course', ondelete='CASCADE',
            select=True, required=True)

class StudentScore(ModelView, ModelSQL):
    'Student Score'
    __name__ = 'op.student-op.distribution'
    
    student = fields.Many2One('op.student', 'Student')
    distribution = fields.Many2One('op.distribution', 'Distribution')
    points = fields.Numeric('Points')
    
class GradeSheet(ModelView, ModelSQL):
    'Grade Sheet'
    __name__ = 'op.grade.sheet'
    
    course = fields.Many2One('op.course', 'Course',)
    scores = fields.Many2Many('op.student-op.distribution', 'student','distribution',
                            'Scores')