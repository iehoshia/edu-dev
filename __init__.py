# tryton test

from trytond.pool import Pool

from .student import *

def register():
    Pool.register(
        Student,
        Course,
        Distribution,
        Enrollment,
        GradeSheet,
        StudentScore, 
        module='edu', type_='model')
