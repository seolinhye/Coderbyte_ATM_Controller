class BankAPI:
    def __init__(self, user_db):
        self.user_db = user_db

    def get_pin_number(self, card_number):
        card_info = self.user_db.get(card_number)
        if card_info:
            return card_info.get("pin")
        else:
            return None
        
    def pin_check(self, card_number, pin):
        card_info = self.user_db.get(card_number)
        if card_info and pin == card_info.get("pin"):
            return True
        else:
            return False
    
    def get_account_list(self, card_number):
        card_info = self.user_db.get(card_number)
        if card_info:
            return card_info.get("accounts")
        else:
            return None
    
    def get_account_info(self, account_number):
        account_info = self.user_db.get_account_info(account_number)
        if account_info:
            return account_info
        else:
            return None
    
    def get_balance(self, account_number):
        account_info = self.user_db.get_account_info(account_number)
        if account_info:
            return account_info.get("balance")
        else:
            return None
    
    def deposit(self, account_number, amount):
        account_info = self.user_db.get_account_info(account_number)
        if account_info:
            account_info["balance"] += amount
            return True
        else:
            return False
    
    def withdraw(self, account_number, amount):
        account_info = self.user_db.get_account_info(account_number)
        if account_info:
            account_info["balance"] -= amount
            return True
        else:
            return False
        
