import datetime
from datetime import datetime, date ,timedelta

class OneTrip:
   def __init__(self) :
       self.credit = 1000

   def use_card(self):
       if self.credit != 0:
        self.credit = self.credit - self.credit
        return 'pass!'

       else:
           return 'it was used one time! try another card'

   

class Credit:
    def __init__(self, credit) :
       self.credit = credit

    def use_card(self):
        if 1000 <= self.credit :
            self.credit = self.credit - 1000
            return f'your credit is: {self.credit}'
        else:
            while True:
                ask_to_charge = input('your credit is low want to charge(yes/No):').lower()
                if ask_to_charge == 'yes':
                    amount = input('enter times:')
                    if amount.isnumeric():
                        self.credit = self.credit + (int(amount)*1000)
                        return f'your card charge successfully and your credit is :{self.credit}'
                    else:
                         print('enter digit !! ','\n',
                         '--------------back to menu-------------')

                elif ask_to_charge == 'no':
                     return 'end of process!!'
                else:
                    print('just yes/No')

   
    def charge(self ,times):
        print ('your credit is:',self.credit)
        self.credit = self.credit + (times * 1000)
        return f'your card charged for {times} times and your credit is {self.credit}'



class CreditTime(Credit):
    def __init__(self ,credit):
        self.credit = credit
        self.start = start = datetime.now()
        self.expire = start.month + 1
    
    def use_card(self,time):
        if time ==  (date.today() - timedelta(days=1)):
            return f'your card is expired! your credit was{self.credit} it had credit until :{time}'

        elif time != self.expire:
            return super().use_card()
        else:
            return f'your card is expired! your credit was{self.credit} it had credit until :{self.expire}'

        

obj1 = OneTrip()
obj2 = Credit(2000)
obj3 = CreditTime(7000)

user_expire_date =  date.today() - timedelta(days=1) #yesterday time
user_date = date.today() 
'''one Trip'''
print(obj1.use_card())
print(obj1.use_card())
'''credit Time'''
print(obj3.use_card(user_expire_date)) #get the time of yesterday and pass it to CreditTme method

'''credit'''
print(obj2.charge(10))
# print(obj2.use_card())
# print(obj2.use_card()) # use to charge if credit is 0

'''use credit-time card until it's expire'''
# print(obj3.use_card(user_date))
# print(obj3.use_card(user_date))
# print(obj3.use_card(user_date))
# print(obj3.use_card(user_date))
# print(obj3.use_card(user_date))
# print(obj3.use_card(user_date))
# print(obj3.use_card(user_date)) #credit is 0
# print(obj3.use_card(user_date)) #use to charge card if the credit is 0