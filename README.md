# Учебный проект банковского приложения на языке Python учебной платформы SkyPro.
## Банковское приложение, для работы с банковскими операциями, картами и счетами.
## Имеет функции: 
- Маскировки счета <font color="#218bff">(masks.get_mask_account())</font>.
- Маскировки карты <font color="#218bff">(masks.get_mask_card_number())</font>. 
- Функцию, которая определяет тип инвормации(карта/счет) и 
возвращает маску и информацию типе данных <font color="#218bff">(widget.get_mask_account_card())</font>
- Функция принимает дату в формате: "2024-03-11T02:26:18.671407",
    возвращает в формате: "ДД.ММ.ГГГГ". <font color="#218bff">(widget.get_date())</font>
- Функции фильтрации банковских операций по состоянию "state" <font color="#218bff">(processing.filter_by_state)</font>.
- Сортировки банковских операция по дате <font color="#218bff">(processing.sort_by_date)</font>
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
- <font color="#218bff">widget.get_mask_account_card(account_info: str) -> str</font> </font> Маскиро номера счета или карты.  
  Для использования функции передайте в функцию именование передаваемого номера и номер для преобразования в строчном виде(str).  
  Это может быть как счет так и карта. Функция вернет именование номера и маску номера в виде: **4567/1234 56\** **** 7890
  ```
  def get_mask_account_card(account_info: str) -> str:
      ...
  accaunt_info = "Счет 73654108430135874305"
  print(get_mask_account_card(accaunt_info))
  ```
  Вывод:  
  `Счет **4305`
- <font color="#218bff">(widget.get_date(unformatted_date: str) -> str)</font> Функция переформатирования даты.  
  Для использования функии передайте в функцию дату в строковом виде(str) в формате: "2024-03-11T02:26:18.671407".  
  Функция вернет дату в строковом виде(str) в формате: "ДД.ММ.ГГГГ"
  ```
  def get_date(unformatted_date: str) -> str:
      ...

  
  print(get_date("2024-03-11T02:26:18.671407"))
  ```
  Вывод: `11.03.2024`
- <font color="#218bff">(processing.filter_by_state(banking_operations: List[dict], state: str = 'EXECUTED') -> List[dict])</font> Функции фильтрации банковских операций по состоянию(state).  
  Для использования функции передайте в функцию список банковских операций(словарей)(List[dict]) и опционально параметр state(по умолчанию 'EXECUTED').  
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
  `[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},  
  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]`
- <font color="#218bff">(processing.sort_by_date(banking_operations: List[dict], rev: bool = False) -> List[dict])</font> Сортировки банковских операция по дате.  
  Для использования функции передайте в функцию список банковских операций(словарей)(List[dict]) и опционально параметр rev(revers)(по умолчанию 'False')  
  Фунция вернет отсортированный по дате список банковских операций, по умолчанию по возвастанию. Если нужно отсортировать по убыванию, передайте в фунцию параметр rev со значием('True')  
  ```
  def sort_by_date(banking_operations: List[dict], rev: bool = False) -> List[dict]:
      ...
  
  
  list_data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]  
  
  print(sort_by_data(list_data, True))
  ```
  Вывод:  
 `[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]  
  `