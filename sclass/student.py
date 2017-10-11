from sclass.departments import departments

class students(departments):
    def __init__(self, name='N/A', surname='N/A'):
        print("Student initialization")
        self._name = name
        self._surname = surname

    def register(self, sname, ssurname):
        try:
            newname=''
            counter=0
            if (self.check_registered(sname)):
                newname = sname + '1'
                counter+=1
                raise RuntimeError('%s is already registered' % sname.upper())
            else:
                print('Create as New student: %s' % sname)

            if (self.check_gradute(sname)):
                counter += 1
                raise RuntimeError('%s has been graduated' % sname.upper())
            else:
                print('%s has NOT been graduated' % sname)

        except RuntimeError as r:
            print("There were %d exceptions:" % counter, r)
        except:
            print('unknown error')
        finally:

            if (len(newname)>1):
                print("Student will be registered with the name of %s " % newname.upper())
            else:
                print("Student will be registered with the name of %s " % sname.upper() )

    def check_gradute(self, name):
        graduated=['esra','ozan','ufuk']
        if name in graduated:
            return 1
        else:
            return 0

    def check_registered(self, name):
        registered=['']
        if name in registered:
            return 1
        else:
            return 0

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_surname(self, surname):
        self._surname = surname

    def get_surname(self):
        return self._surname