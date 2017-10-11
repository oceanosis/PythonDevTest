import sclass.student as s

def main():
        student1 = s.students('aaa')
        student1.set_name()
        student1.set_surname()

        print('Name: {}'.format(student1.get_name()).upper());
        print ('Surname: {}'.format(student1.get_surname()).upper());

        student1.register(student1.get_name(), student1.get_surname())

        student2 = s.departments()
        student2.register()


main()