## Домашнее задание к занятию "Языки разметки JSON и YAML"

------

## Задание 1

Мы выгрузили JSON, который получили через API запрос к нашему сервису:

```
    { "info" : "Sample JSON output from our service\t",
        "elements" :[
            { "name" : "first",
            "type" : "server",
            "ip" : 7175 
            }
            { "name" : "second",
            "type" : "proxy",
            "ip : 71.78.22.43
            }
        ]
    }
```
  Нужно найти и исправить все ошибки, которые допускает наш сервис

### Ваш скрипт:
```
    { "info" : "Sample JSON output from our service \n",
        "elements" :[
            { "name" : "first",
            "type" : "server",
            "ip" : 7175 
            },
            { "name" : "second",
            "type" : "proxy",
            "ip : "71.78.22.43"
            }
        ]
    }
```

---

## Задание 2

В прошлый рабочий день мы создавали скрипт, позволяющий опрашивать веб-сервисы и получать их IP. К уже реализованному функционалу нам нужно добавить возможность записи JSON и YAML файлов, описывающих наши сервисы. Формат записи JSON по одному сервису: `{ "имя сервиса" : "его IP"}`. Формат записи YAML по одному сервису: `- имя сервиса: его IP`. Если в момент исполнения скрипта меняется IP у сервиса - он должен так же поменяться в yml и json файле.

### Ваш скрипт:
```python
from socket import gethostbyname
from sys import exit
import json
import yaml


def get_sites_addr(urls_: list) -> list:
    sites = []
    for site in urls_:
        sites.append({site: gethostbyname(site)})
    return sites


def print_sites_addr(sites: list):
    for site in sites:
        for url_, addr in site.items():
            print(url_, addr)
    print()


def check_vals_in_dns(sites: list):
    print("Проверка актуальности dns записей... ")
    count = 0
    for site in sites:
        for url_, addr in site.items():
            new_addr = gethostbyname(url_)
            if addr != new_addr:
                print(f"[ERROR] {url_} IP mismatch: {addr} {new_addr}. Correcting addresses... ")
                site[url_] = new_addr
                count += 1
    if count > 0:
        print(f"Данные актуализированы. Исправлено {count} адрес(а). ")
    else:
        print("Все адреса актуальны. ")
    print()


def save_json(sites: list):
    check_vals_in_dns(sites)
    with open("dns.json", "w") as js:
        js.write(json.dumps(sites, indent=2))
    print("Файл dns.json сохранен. ")


def save_yaml(sites: list):
    check_vals_in_dns(sites)
    with open("dns.yml", "w") as ym:
        ym.write(yaml.dump(sites, explicit_start=True, explicit_end=True, indent=2))
    print("Файл dns.yml сохранен. ")


print("Получаем соответствие ip-адресов - dns записям.")
urls = ['drive.google.com', 'mail.google.com', 'google.com']
sites_list = get_sites_addr(urls)
while True:
    print('''1 - распечатать соответствие ip-адресов - dns записям
2 - сравнить текущее значение ip-адресов с сохраненным значением
3 - сохранить в json
4 - сохранить данные в yaml
5 - завершить работу скрипта
    ''')
    status = int(input('Введите значение: '))
    if status == 1:
        print_sites_addr(sites_list)
    elif status == 2:
        check_vals_in_dns(sites_list)
    elif status == 3:
        save_json(sites_list)
    elif status == 4:
        save_yaml(sites_list)
    elif status == 5:
        print("Завершаю работу. ")
        exit(0)
    else:
        print("Введите корректное значение из списка.")
        print()

```

### Вывод скрипта при запуске при тестировании:
```
Получаем соответствие ip-адресов - dns записям.
1 - распечатать соответствие ip-адресов - dns записям
2 - сравнить текущее значение ip-адресов с сохраненным значением
3 - сохранить в json
4 - сохранить данные в yaml
5 - завершить работу скрипта
    
Введите значение: 4
Проверка актуальности dns записей... 
Все адреса актуальны. 

Файл dns.yml сохранен. 
```

### json-файл(ы), который(е) записал ваш скрипт:
```json
[
  {
    "drive.google.com": "173.194.222.194"
  },
  {
    "mail.google.com": "64.233.164.18"
  },
  {
    "google.com": "142.251.1.100"
  }
]
```

### yml-файл(ы), который(е) записал ваш скрипт:
```yaml
---
- drive.google.com: 173.194.222.194
- mail.google.com: 64.233.164.17
- google.com: 142.251.1.100
...
```

---
