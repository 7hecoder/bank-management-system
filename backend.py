import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []

    @classmethod
    def load_data(cls):
        try:
            if Path(cls.database).exists():
                with open(cls.database) as fs:
                    cls.data = json.loads(fs.read())
            else:
                cls.data = []
        except Exception as err:
            raise Exception(f"Error loading data: {err}")

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(cls.data))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)

    def create_account(self, name, age, email, pin):
        if age < 18 or len(str(pin)) != 4:
            raise ValueError("Sorry, you cannot create an account!")
        else:
            account_no = self.__accountgenerate()
            info = {
                "name": name,
                "age": age,
                "email": email,
                "pin": pin,
                "accountNo": account_no,
                "balance": 0
            }

            self.data.append(info)
            self.__update()
            return info

    def deposit(self, accno, pin, amount):
        userdata = [i for i in self.data if i['accountNo'] == accno and i['pin'] == pin]
        if not userdata:
            raise ValueError("Account or Pin is incorrect!")
        else:
            if amount <= 0:
                raise ValueError("Please enter a valid amount!")
            elif amount > 10000:
                raise ValueError("Amount exceeds the limit. Please visit the bank.")
            else:
                userdata[0]['balance'] += amount
                self.__update()
                return f"Amount of {amount} deposited successfully!"

    def withdraw(self, accno, pin, amount):
        userdata = [i for i in self.data if i['accountNo'] == accno and i['pin'] == pin]
        if not userdata:
            raise ValueError("Account or Pin is incorrect!")
        else:
            if amount <= 0:
                raise ValueError("Please enter a valid amount!")
            elif amount > userdata[0]['balance']:
                raise ValueError("Insufficient balance!")
            else:
                userdata[0]['balance'] -= amount
                self.__update()
                return f"Withdrawal of {amount} successful. Remaining balance: {userdata[0]['balance']}"

    def show_details(self, accno, pin):
        userdata = [i for i in self.data if i['accountNo'] == accno and i['pin'] == pin]
        if not userdata:
            raise ValueError("Account or Pin is incorrect!")
        else:
            return userdata[0]

    def update_details(self, accno, pin, new_name, new_email, new_pin):
        userdata = [i for i in self.data if i['accountNo'] == accno and i['pin'] == pin]
        if not userdata:
            raise ValueError("Account or Pin is incorrect!")
        else:
            userdata[0]['name'] = new_name if new_name else userdata[0]['name']
            userdata[0]['email'] = new_email if new_email else userdata[0]['email']
            userdata[0]['pin'] = int(new_pin) if new_pin else userdata[0]['pin']
            self.__update()
            return "Account details updated successfully!"

    def delete_account(self, accno, pin):
        userdata = [i for i in self.data if i['accountNo'] == accno and i['pin'] == pin]
        if not userdata:
            raise ValueError("Account or Pin is incorrect!")
        else:
            self.data.remove(userdata[0])
            self.__update()
            return "Account deleted successfully!"
