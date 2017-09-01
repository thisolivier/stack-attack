from django.db import models

class UserManager(models.Manager):

    def validator(self, data):
        def check_length(string, length):
            if len(string) < length:
                return (False, 'too short')
            return (True, '')

        def build_birthday():
            try:
                day_num = int(data['bday_day'])
                month_num = int(data['bday_month'])
                year_num = int(data['bday_year'])
            except:
                return (False, 'not all fields were numbers')

            try:
                birthday_input = datetime(year=year_num, month=month_num, day=day_num)
            except:
                return (False, 'your birthday wasn\'t a real day')

            checker = datetime.now() - timedelta(days=365*18)
            if birthday_input < checker:
                return (True, birthday_input)
            return (False, 'You are too young for this, buy me a drink first')
        
        def check_email(email):
            if re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', email) :
                return (True, '')
            else :
                return (False, 'not email')

        def process_pass(password, pass_check):
            if password != pass_check:
                return (False, 'passwords do not match')
            return (True, '')

        results = {
            # 'name': check_length(data['name'], 3),
            # 'fake_name': check_length(data['fake_name'], 3),
            'email': check_length(data['email'], 5),
            'password' : check_length(data['password'], 8),
            # 'birthday': build_birthday()
        }
        if results['email'][0] :
            results['email'] = check_email(data['email'])
        
        if results['password'][0]:
            results['password'] = process_pass(data['password'], data['password_check'])

        return results