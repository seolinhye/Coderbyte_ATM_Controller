# Coderbyte_ATM_Controller

## 실제 은행 시스템
- 사용자가 ATM기기에 카드 삽입, Pin 번호 입력, 계좌 선택 후 잔액조회/입금/출금 동작 수행
- 사용자의 입력은 API로 전달되고, API는 입력된 정보를 기반으로 컨트롤러를 실행
- api를 통해 데이터를 조회, 즉 controller에서 데이터베이스에 직접 접근 x, api를 통해 접근
- ATM controller에 은행 API 인스턴스를 전달하도록 하는 구조
  

## 가정
- 카드 번호, 핀 번호, 계좌 번호들에 대한 데이터베이스의 primary key는 card_number라고 가정 (그래야 사용자 별 구분하여 핀 번호 전달)
- api는 사용자에게 See account / deposit / withdraw 기능 중 1가지 선택 물어봄
- 잔액 부족의 예외 처리 로직 컨트롤러에서 수행 


## 알고리즘
- 카드가 삽입되었을 때, 카드 번호에 따라 데이터베이스에 있는 PIN값을 조회해서 return
- api에서 controller를 통해 핀 번호를 받고, 사용자가 입력한 핀 번호와 맞는지 체크 후 controller에게 올바른지 여부 알려줌
- api는 pin_number함수를 통해 여부에 따라 계좌 번호 리스트를 받아와서 사용자에게 전달
- 사용자가 선택할 계좌를 체크한 후  api는 선택한 계좌를 controller에게 전달
- controller는 선택한 계좌 정보를 은행 API를 통해 조회하여 return
- 사용자의 잔액 조회/ 입금/ 조회 선택에 따라 api에서 컨트롤러에서 해당 기능 불러옴
- see_balance 에서 은행 api를 통해 계좌 번호에 따른 잔액 조회 
- deposit은 은행 api를 통해 계좌에 입금
- withdraw는 은행 api를 통해 계좌에서 출금 (출금 금액이 잔액보다 큰지는 컨트롤러가 아닌 api에서 확인) 
