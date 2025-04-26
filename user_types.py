from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, transactions):
        self.transactions = transactions

    @abstractmethod
    def is_fraudulent(self):
        pass


class PersonalUser(User):
    def is_fraudulent(self):
        conditions = []

        if len(self.transactions) == 1:
            tx = self.transactions[0]
            conditions.append(tx['country'].lower() == "usa")
            conditions.append(tx['amount'] < 20000)
        elif len(self.transactions) == 2:
            tx1, tx2 = self.transactions
            conditions.append(tx1['amount'] < 7000 and tx2['amount'] < 7000)
            conditions.append(tx1['country'].lower() == "usa" and tx2['country'].lower() == "usa")
            conditions.append(tx1['device'] == tx2['device'])
        else:
            return True  # أي عدد معاملات غير مسموح به = احتيال

        return not all(conditions)


class BusinessUser(User):
    disallowed_countries = ['caribbean', 'mexico', 'russia', 'east asia', 'south africa']

    def is_fraudulent(self):
        if len(self.transactions) > 3:
            return True

        for tx in self.transactions:
            if tx['amount'] > 50000:
                return True
            if tx['country'].lower() in self.disallowed_countries:
                return True

        devices = set(tx['device'] for tx in self.transactions)
        return not len(devices) == 1  # لازم كل العمليات من نفس الجهاز


class ResidentForeignUser(User):
    def __init__(self, transactions, original_country):
        super().__init__(transactions)
        self.original_country = original_country.lower()

    def is_fraudulent(self):
        if len(self.transactions) != 1:
            return True

        tx = self.transactions[0]
        conditions = [
            tx['amount'] < 15000,
            tx['country'].lower() == self.original_country,
        ]
        return not all(conditions)
