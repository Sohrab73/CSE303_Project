from django.db import connection
import os
PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))
import sys
sys.path.append(PROJECT_PATH)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DATABASE.settings')
import django
django.setup()
from RCRAS.models import *

# with connection.cursor() as c:
#     c.execute('''
#     CREATE OR REPLACE VIEW joinedtable AS
#     SELECT *
#     FROM RCRAS_department_t AS D INNER JOIN RCRAS_course_t AS C ON DeptID=DeptID_id
#                                INNER JOIN RCRAS_section_t AS S ON CourseID=CourseID_id
#     ''')
    
def enrollment_wise_course_school(School, Sem, Year):
    with connection.cursor() as cursor:
        cursor.execute('''
        SELECT COUNT(*)
        FROM (SELECT *
                        FROM RCRAS_department_t AS D INNER JOIN RCRAS_course_t AS C ON DeptID=DeptID_id
                               INNER JOIN RCRAS_section_t AS S ON CourseID=CourseID_id)
        WHERE SchoolTitle_id="{}" AND Semester="{}" AND Year={} AND SectionEnrolled BETWEEN 1 AND 10
        UNION ALL
        SELECT COUNT(*)
        FROM (SELECT *
                        FROM RCRAS_department_t AS D INNER JOIN RCRAS_course_t AS C ON DeptID=DeptID_id
                               INNER JOIN RCRAS_section_t AS S ON CourseID=CourseID_id)
        WHERE SchoolTitle_id="{}" AND Semester="{}" AND Year={} AND SectionEnrolled BETWEEN 11 AND 20
        UNION ALL
        SELECT COUNT(*)
        FROM (SELECT *
                        FROM RCRAS_department_t AS D INNER JOIN RCRAS_course_t AS C ON DeptID=DeptID_id
                               INNER JOIN RCRAS_section_t AS S ON CourseID=CourseID_id)
        WHERE SchoolTitle_id="{}" AND Semester="{}" AND Year={} AND SectionEnrolled BETWEEN 21 AND 30
        UNION ALL
        SELECT COUNT(*)
        FROM (SELECT *
                        FROM RCRAS_department_t AS D INNER JOIN RCRAS_course_t AS C ON DeptID=DeptID_id
                               INNER JOIN RCRAS_section_t AS S ON CourseID=CourseID_id)
        WHERE SchoolTitle_id="{}" AND Semester="{}" AND Year={} AND SectionEnrolled BETWEEN 31 AND 35
        UNION ALL
        SELECT COUNT(*)
        FROM (SELECT *
                        FROM RCRAS_department_t AS D INNER JOIN RCRAS_course_t AS C ON DeptID=DeptID_id
                               INNER JOIN RCRAS_section_t AS S ON CourseID=CourseID_id)
        WHERE SchoolTitle_id="{}" AND Semester="{}" AND Year={} AND SectionEnrolled BETWEEN 36 AND 40
        UNION ALL
        SELECT COUNT(*)
        FROM (SELECT *
                        FROM RCRAS_department_t AS D INNER JOIN RCRAS_course_t AS C ON DeptID=DeptID_id
                               INNER JOIN RCRAS_section_t AS S ON CourseID=CourseID_id)
        WHERE SchoolTitle_id="{}" AND Semester="{}" AND Year={} AND SectionEnrolled BETWEEN 41 AND 50
        UNION ALL
        SELECT COUNT(*)
        FROM (SELECT *
                        FROM RCRAS_department_t AS D INNER JOIN RCRAS_course_t AS C ON DeptID=DeptID_id
                               INNER JOIN RCRAS_section_t AS S ON CourseID=CourseID_id)
        WHERE SchoolTitle_id="{}" AND Semester="{}" AND Year={} AND SectionEnrolled BETWEEN 51 AND 55
        UNION ALL
        SELECT COUNT(*)
        FROM (SELECT *
                        FROM RCRAS_department_t AS D INNER JOIN RCRAS_course_t AS C ON DeptID=DeptID_id
                               INNER JOIN RCRAS_section_t AS S ON CourseID=CourseID_id)
        WHERE SchoolTitle_id="{}" AND Semester="{}" AND Year={} AND SectionEnrolled BETWEEN 56 AND 60
        UNION ALL
        SELECT COUNT(*)
        FROM (SELECT *
                        FROM RCRAS_department_t AS D INNER JOIN RCRAS_course_t AS C ON DeptID=DeptID_id
                               INNER JOIN RCRAS_section_t AS S ON CourseID=CourseID_id)
        WHERE SchoolTitle_id="{}" AND Semester="{}" AND Year={} AND SectionEnrolled > 60
        '''.format(School, Sem, Year, School, Sem, Year, School, Sem, Year, School, Sem, Year, School, Sem, Year, School, Sem, Year, School, Sem, Year, School, Sem, Year, School, Sem, Year))

        col = cursor.fetchall()
    return col
 


def classroom_requirement_course_offer(Sem, Year):
    #have to change SectionEnrolled -> SectionCapacity->noo neeeedddddd
    with connection.cursor() as cursor:
        cursor.execute('''
        SELECT COUNT(*) AS Sections
        FROM (SELECT *
                        FROM RCRAS_department_t AS D INNER JOIN RCRAS_course_t AS C ON DeptID=DeptID_id
                               INNER JOIN RCRAS_section_t AS S ON CourseID=CourseID_id)
        WHERE SectionEnrolled BETWEEN 1 AND 10
        AND semester = "{}"
        AND YEAR ={}

        UNION ALL

        SELECT COUNT(*)
        FROM (SELECT *
                        FROM RCRAS_department_t AS D INNER JOIN RCRAS_course_t AS C ON DeptID=DeptID_id
                               INNER JOIN RCRAS_section_t AS S ON CourseID=CourseID_id)
        WHERE SectionEnrolled BETWEEN 11 AND 20
        AND semester = "{}"
        AND YEAR ={}

        UNION ALL

        SELECT COUNT(*)
        FROM (SELECT *
                        FROM RCRAS_department_t AS D INNER JOIN RCRAS_course_t AS C ON DeptID=DeptID_id
                               INNER JOIN RCRAS_section_t AS S ON CourseID=CourseID_id)
        WHERE SectionEnrolled BETWEEN 21 AND 30
        AND semester = "{}"
        AND YEAR ={}

        UNION ALL

        SELECT COUNT(*)
        FROM (SELECT *
                        FROM RCRAS_department_t AS D INNER JOIN RCRAS_course_t AS C ON DeptID=DeptID_id
                               INNER JOIN RCRAS_section_t AS S ON CourseID=CourseID_id)
        WHERE SectionEnrolled BETWEEN 31 AND 35
        AND semester = "{}"
        AND YEAR ={}

        UNION ALL

        SELECT COUNT(*)
        FROM (SELECT *
                        FROM RCRAS_department_t AS D INNER JOIN RCRAS_course_t AS C ON DeptID=DeptID_id
                               INNER JOIN RCRAS_section_t AS S ON CourseID=CourseID_id)
        WHERE SectionEnrolled BETWEEN 36 AND 40
        AND semester = "{}"
        AND YEAR ={}

        UNION ALL

        SELECT COUNT(*)
        FROM (SELECT *
                        FROM RCRAS_department_t AS D INNER JOIN RCRAS_course_t AS C ON DeptID=DeptID_id
                               INNER JOIN RCRAS_section_t AS S ON CourseID=CourseID_id)
        WHERE SectionEnrolled BETWEEN 41 AND 50
        AND semester = "{}"
        AND YEAR ={}

        UNION ALL

        SELECT COUNT(*)
        FROM (SELECT *
                        FROM RCRAS_department_t AS D INNER JOIN RCRAS_course_t AS C ON DeptID=DeptID_id
                               INNER JOIN RCRAS_section_t AS S ON CourseID=CourseID_id)
        WHERE SectionEnrolled BETWEEN 51 AND 55
        AND semester = "{}"
        AND YEAR ={}

        UNION ALL

        SELECT COUNT(*)
        FROM (SELECT *
                        FROM RCRAS_department_t AS D INNER JOIN RCRAS_course_t AS C ON DeptID=DeptID_id
                               INNER JOIN RCRAS_section_t AS S ON CourseID=CourseID_id)
        WHERE SectionEnrolled BETWEEN 56 AND 65
        AND semester = "{}"
        AND YEAR ={}


        '''.format(Sem, Year, Sem, Year, Sem, Year, Sem, Year, Sem, Year, Sem, Year, Sem, Year, Sem, Year))
        sections=[]
        col = cursor.fetchall()
        for i in col:
            for j in i:
                sections.append(j)
    return (sections)