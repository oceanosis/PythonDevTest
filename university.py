import sclass.student as s
import os
import sys

def main():
        student1 = s.students()

        student1.set_name("ufuk")

        print ('Name: {}'.format(student1.get_name()).upper());

        student1.set_surname("duMlu")

        print ('Surname: {}'.format(student1.get_surname()).upper());

        student1.register(student1.get_name(), student1.get_surname())

        student2 = s.departments()
        student2.register()


main()