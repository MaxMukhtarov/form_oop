class Registration_form:
    royxat  = {"Ali|Vali":'1234'}
    def __init__(self) -> None:
        pass


    ####################################
    ########## CLASSMETHODLAR ##########
    ####################################
    @classmethod
    def check_pwd(self, p1, p2):
        if p1 == p2:
            return True
        else:
            return False

    
    @classmethod
    def view(self, usr, id):
        if id == Registration_form.royxat[usr]['id']:
            print(f"Sizning parolingiz {(Registration_form.royxat[usr]['password'])}")
        else:
            print('Siz ushbu shaxs ekanligingizga shubxa bor')


    @classmethod
    def msid(self):
        import random
        uid = ''
        for i in range(6):
            uid += str(random.randint(0, 9))
        return uid

    
    
    ####################################
    ############ METHODLAR #############
    ####################################
    def register(self, name, surname, pwd, pwd_again):
        self.name = name
        self.surname = surname
        self.pwd = pwd
        self.pwd_again = pwd_again
        self.tekshiruv = Registration_form.check_pwd(self.pwd, self.pwd_again)
        self.full = f'{self.name}|{self.surname}'
        self.activate = Registration_form.msid()
        self.ijro = {'password':self.pwd,
        'id':self.activate}
        if self.tekshiruv and self.full not in list((Registration_form.royxat).keys()):
            Registration_form.royxat[self.full] = self.ijro
            print("Siz muvaffaqiyatli ro`yxatdan o`tdingiz")
            print(f'Sining aktivatsiya kodinggiz {self.activate}')
        elif self.tekshiruv == False:
            print("Kiritgan parollaringiz bir biriga mos kelmadi")
        elif self.full in list((Registration_form.royxat).keys()):
            print('Siz oldin ro`yxatdan o`tgansiz')
            
        else:
            print("Kutilmagan hatolik ro`y berdi")

    
    

    def signin(self, username, passwd):
        self.username = username
        self.passwd = passwd
        if self.username in list((Registration_form.royxat).keys()):
            if self.passwd == Registration_form.royxat[username]['password']:
                print('Ishchi oynaga xush kelibsiz')
            else:
                javob = input('Agar parolingiz esdan chiqqan bo`lsa, uni tiklash uchun 1 ni kiriting: ')
                if javob == '1':
                    id = input('Aktivatsiya kodini kiriting: ')
                    Registration_form.view(self.username, id)
