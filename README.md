# Учебный проект банковского приложения на языке Python учебной платформы SkyPro.

## Банковское приложение, для работы с банковскими операциями, картами и счетами.

## Имеет функции:

  - Маскировки счета <font color="#218bff">(masks.get_mask_account())</font>.
  - Маскировки карты <font color="#218bff">(masks.get_mask_card_number())</font>.
  - Функцию, которая определяет тип информации(карта/счет) и
    возвращает маску и информацию типе данных <font color="#218bff">(widget.get_mask_account_card())</font>
  - Функция принимает дату в формате: "2024-03-11T02:26:18.671407",
    возвращает в формате: "ДД.ММ.ГГГГ". <font color="#218bff">(widget.get_date())</font>
  - Функции фильтрации банковских операций по состоянию "state" <font color="#218bff">(processing.filter_by_state)</font>.
  - Сортировки банковских операция по дате <font color="#218bff">(processing.sort_by_date)</font>
  - Функция принимает список словарей с транзакциями и возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной <font color="#218bff">(generators.filter_by_currency)</font>
  - Функция генератора, принимает список словарей с транзакциями и возвращает описание каждой операции по очереди <font color="#218bff">(generators.transaction_descriptions)</font>
  - Функция генератора, выдает номера банковских карт в формате XXXX XXXX XXXX XXXX в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Генератор принимает начальное и конечное значения для генерации диапазона номеров <font color="#218bff">(generators.card_number_generator)</font>

### Использование функций:

  - <font color="#218bff">masks.get_mask_account(account: int | str) -> str</font> Маскировка номера счета.  
    Для использования функции передайте в функцию номер счета в целочисленном(int) или строчном виде(str).  
    Функция вернет маску счета строчного типа(str) в виде: **4567
    ```
    def get_mask_account(account: int | str) -> str:
        ...
    account_number = "73654108430135874305"
    print(get_mask_account(account_number))
    ```
    Вывод:  
    `**4305`
  - <font color="#218bff">masks.get_mask_card_number()(card_number: int | str) -> str</font> Маскировка номера карта.  
    Для использования функции передайте в функцию номер карты в целочисленном(int) или строчном виде(str).  
    Функция вернет маску счета строчного типа(str) в виде: 1234 56** **** 7890
    ```
    def get_mask_card_number(card_number: int | str) -> str:
        ...
    card_number = "7000792289606361"
    print(get_mask_card_number("card_number"))
    ```
    Вывод:  
    `7000 79** **** 6361`
  - <font color="#218bff">widget.get_mask_account_card(masking_data: str) -> str</font> </font> Маскиро номера счета или
    карты.  
    Для использования функции передайте в функцию именование передаваемого номера и номер для преобразования в строчном
    виде(str).  
    Это может быть как счет так и карта. Функция вернет именование номера и маску номера в виде: **4567/1234 56\** ****
    7890
    ```
    def get_mask_account_card(masking_data: str) -> str:
        ...
    masking_data = "Счет 73654108430135874305"
    print(get_mask_account_card(accaunt_info))
    ```
    Вывод:  
    `Счет **4305`
  - <font color="#218bff">(widget.get_date(unformatted_date: str) -> str)</font> Функция переформатирования даты.  
    Для использования функции передайте в функцию дату в строковом виде(str) в формате: "2024-03-11T02:26:18.671407".  
    Функция вернет дату в строковом виде(str) в формате: "ДД.ММ.ГГГГ"
    ```
    def get_date(unformatted_date: str) -> str:
        ...

  
    print(get_date("2024-03-11T02:26:18.671407"))
    ```
    Вывод:  
    `11.03.2024`
  - <font color="#218bff">(processing.filter_by_state(banking_operations: List[dict], state: str = 'EXECUTED') ->
    List[dict])</font> Функции фильтрации банковских операций по состоянию(state).  
    Для использования функции передайте в функцию список банковских операций(словарей)(List[dict]) и опционально параметр
    state(по умолчанию 'EXECUTED').  
    Функция вернет отфильтрованный список по параметру state
    ```
    def filter_by_state(banking_operations: List[dict], state: str = 'EXECUTED') -> List[dict]:
        ...
    
  
    list_data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]  
  
    print(filter_by_state(list_data, "CANCELED"))
    ```
    Вывод:  
    ```
    [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},  
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    ```
  - <font color="#218bff">(processing.sort_by_date(banking_operations: List[dict], rev: bool = False) ->
    List[dict])</font> Сортировки банковских операция по дате.  
    Для использования функции передайте в функцию список банковских операций(словарей)(List[dict]) и опционально параметр
    reverse(по умолчанию 'True')  
    Функция вернет отсортированный по дате список банковских операций, по умолчанию по возрастанию. Если нужно
    отсортировать по убыванию, передайте в функцию параметр reverse со значением('False')
    ```
    def sort_by_date(banking_operations: List[dict], reverse: bool = True) -> List[dict]:
        ...
  
  
    list_data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]  
  
    print(sort_by_date(list_data, False))
    ```
    Вывод:  
    ``` 
     [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},  
     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},  
     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},  
     {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
    ```   
  - <font color="#218bff">(generators.filter_by_currency(transactions: list[dict], currency_code: str) -> Iterable:)</font> Фильтрация транзакций по валюте  
    Для использования функции передайте в качестве аргумента список транзакций и международный код валюты, функция вернет генератор, который будет отдавать по очереди  
    по одной транзакции за один запрос.  
    ```
    def filter_by_currency(transactions: list[dict], currency_code: str) -> Iterable:  
    ...
    
    transactions =
     [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]  
    
    usd_transactions = filter_by_currency(transactions, "USD")
    for _ in range(2):
        print(next(usd_transactions)) 
    
    ```
    Вывод:
    ```
    {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }  
    ```
    
  - <font color="#218bff">(generators.transaction_descriptions(transactions: list[dict]) -> Generator)</font> Функция для получения описаний транзакций.  
    Для использования функции передайте в качестве аргумента список транзакций. Функция вернет генератор, который будет выдавать по очереди описание транзакций, при каждом запросе.
    
    ```
    def transaction_descriptions(transactions: list[dict]) -> Generator:
        ...
    
    transactions = 
        [ 
          {}, 
          {},
          ...
        ]
    
    descriptions = transaction_descriptions(transactions)
    for _ in range(5):
        print(next(descriptions))
    ```
    Вывод:  
    ```
    Перевод организации
    Перевод со счета на счет
    Перевод со счета на счет
    Перевод с карты на карту
    Перевод организации
    ```
    
    <font color="#218bff">(generators.card_number_generator(start: int, finish: int) -> Generator)</font> Функция генератора номеров банковских карт.
    Для использования функции передайте в качестве аргументов начальное и конечное значение номеров карт.

    ```
    def card_number_generator(start: int, finish: int) -> Generator:
        ...
    
    for card_number in card_number_generator(1, 5):
        print(card_number)
    ```
    Вывод:
    ```
    0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003
    0000 0000 0000 0004
    0000 0000 0000 0005
    ```

## Тестирование


### Отчет по тестам:
````
____ coverage: platform win32, python 3.14.3-final-0 ____ 


Name                       Stmts   Miss  Cover
----------------------------------------------
src\__init__.py                0      0   100%
src\generators.py             14      1    93%
src\masks.py                  22      0   100%
src\processing.py              5      0   100%
src\widget.py                 25      2    92%
tests\__init__.py              0      0   100%
tests\conftest.py             28      0   100%
tests\test_generators.py      22      2    91%
tests\test_masks.py           24      0   100%
tests\test_processing.py      11      0   100%
tests\test_widget.py          17      0   100%
----------------------------------------------
TOTAL                        168      5    97%


==== 26 passed in 0.27s  ===
