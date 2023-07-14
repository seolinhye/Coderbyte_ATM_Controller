from ATM_cash import ATMController
from Bank_API import BankAPI
user_db = Database() # 실제 데이터 베이스 인스턴스 
bank_api = BankAPI(user_db) 

atm = ATMController(bank_api)

#카드 삽입 test 
card_number = input("카드 삽입(카드 번호 입력)")
pin = atm.insert_card(card_number)

if pin:
    input_pin = input("PIN 입력")
    account_list = atm.pin_number(input_pin, card_number)

    if account_list:
        for account_number in account_list:
            print(account_number)
        
        selected_account = input("계좌번호 선택")
        account_info = atm.select_account(selected_account)

        if account_info:
            choice = input("1. 잔액조회 2. 입금 3. 출금")

            if choice == "1":
                balance = atm.see_balance(selected_account)
                if balance is not None:
                    print("잔액: ", balance)
                else:
                    print("조회 실패")
            elif choice == "2":
                amount = input("입금 금액")
                if atm.deposit(selected_account,amount):
                    print("입금 완료")
                else:
                    print("입금 실패")
            elif choice == "3":
                amount = input("출금 금액")
                if atm.withdraw(selected_account, amount):
                    print("출금 완료")
                else:
                    print("출금 실패")
            else:
                print("다시 선택하세요")
        else:
            print("계좌 정보 조회 실패")
    else:
        print("계좌 번호 선택 불가")
else:
    print("올바르지 않는 PIN")


