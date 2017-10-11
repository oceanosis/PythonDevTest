from sclass.departments import departments

class students(departments):
    def __init__(self, *args):
        print("Student initialization with %d parameter" % len(args))
        try:
            self._surname = 'N/A'
            self._name = 'N/A'
            print (args)
            if (len(args) == 0):
                raise RuntimeError('Specify Name / Surname')
            elif (len(args) == 1):
                raise RuntimeError('Specify Surname as well')
            else:
                pass
                self._name = args[0]
                self._surname = args[1]
        except RuntimeError as r:
            print("Missing Arguments:", r)
        except AttributeError as a:
            print("Attributes are missing", a)
        except:
            print ('Unknown Error')



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

    def set_name(self):
        self.name = self._name

    def get_name(self):
        return self.name

    def set_surname(self):
        self.surname = self._surname

    def get_surname(self):
        return self.surname