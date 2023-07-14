# 카드 삽입 -> PIN 번호 -> 계좌 선택 -> 잔액/입금/출급 참조 

#단순화를 위해 세상에는 1달러 지폐만 있고, 센트는 없음, 따라서 계좌 잔액은 정수로 표시됨
#코드가 실제 은행 시스템과 통합될 필요는 없지만, 향후에는 실제 은행 시스템과 통합되기를 원할 수 있음
# 현금 보관함 및 카드 판독기와 같은 은행 통합 및 ATM 하드웨어를 구현하는 것은 범위가 아님
# 컨트롤러 부분 (은행 시스템, 현금 보관함 등은 포함하지 않음)을 테스트하는 것이 포함
# 은행 API는 ATM에 PIN번호를 제공하지 않지만 PIN번호가 올바른지 여부를 알려줌
# 함수/클래스/메소드 만 구현 


class ATMcontroller:
    def __init___(self, bank_api):
        self.bank_api = bank_api

    def insert_card(self, card_number):
        pin = self.bank_api.get_pin_number(card_number)
        if pin:
            return pin
        else:
            return None  
        
    def pin_number(self, card_number, pin):
        pin_check = self.bank_api.pin_check(card_number, pin)
        if pin_check:
            account_list = self.bank_api.get_account_list(card_number)
            if account_list:
                return account_list
            else:
                return None
        else:
            return None

    def select_account(self, account_number):
        account_info = self.bank_api.get_account_info(account_number)
        if account_info:
            return account_info
        else:
            return None
    
    def see_balance(self, account_number):
        balance = self.bank_api.get_balance(account_number)
        if balance is not None:
            return balance
        else:
            return None
    
    def deposit(self, account_number, amount):
        return self.bank_api.deposit(account_number, amount)
    
    def withdraw(self, account_number, amount):
        balance = self.bank_api.get_balance(account_number)
        try:
            if amount <= balance and balance is not None:
                return self.bank_api.withdraw(account_number, amount)
            else:
                raise Exception("계좌 잔액 부족")
        except Exception as e:
            return False
