 # 8.1 Ansible playbook

* Подготовьте свой inventory-файл prod.yml.
```yaml
---
clickhouse:
  hosts:
    clickhouse-01:
      ansbile_connection: ssh
      ansible_host: 127.0.0.1
      ansible_port: 2222
      ansible_user: vagrant

vector:
  hosts:
    vector-01:
      ansbile_connection: ssh
      ansible_host: 127.0.0.1
      ansible_port: 2222
      ansible_user: vagrant

```

* Допишите playbook: нужно сделать ещё один play, который устанавливает и настраивает vector.
* При создании tasks рекомендую использовать модули: get_url, template, unarchive, file.
* Tasks должны: скачать дистрибутив нужной версии, выполнить распаковку в выбранную директорию, установить vector.
```yaml

- name: Install Vector
  hosts: vector
  handlers:
    - name: Restart Vector
      become: true
      ansible.builtin.service:
        name: vector
        state: restarted
  tasks:
    - name: Get Vector Package
      become: true
      ansible.builtin.apt:
        deb: https://packages.timber.io/vector/0.30.0/vector_{{ vector_version }}-1_amd64.deb
        state: present

```


* Запустите ansible-lint site.yml и исправьте ошибки, если они есть.

```ignorelang
kunaev@dub-ws-235:~/projects/devops-netology/8.ansible/8.2_playbook/playbook$ ansible-lint site.yml 
WARNING  Overriding detected file kind 'yaml' with 'playbook' for given positional argument: site.yml
```

* Попробуйте запустить playbook на этом окружении с флагом --check.

на старой инсталяции
```ignorelang
kunaev@dub-ws-235:~/projects/devops-netology/8.ansible/8.2_playbook/playbook$ ansible-playbook -i inventory/prod.yml site.yml --check

PLAY [Install Clickhouse] ***************************************************************************

TASK [Gathering Facts] ***************************************************************************
Enter passphrase for key '/home/kunaev/.ssh/id_rsa': 
ok: [clickhouse-01]

TASK [Get clickhouse distrib] ***************************************************************************
ok: [clickhouse-01] => (item=clickhouse-client)
ok: [clickhouse-01] => (item=clickhouse-server)
ok: [clickhouse-01] => (item=clickhouse-common-static)

TASK [Install clickhouse packages] ***************************************************************************
ok: [clickhouse-01] => (item=clickhouse-common-static-22.4.6.53.deb)
ok: [clickhouse-01] => (item=clickhouse-client-22.4.6.53.deb)
ok: [clickhouse-01] => (item=clickhouse-server-22.4.6.53.deb)

TASK [Create database] ***************************************************************************
skipping: [clickhouse-01]

PLAY [Install Vector] ***************************************************************************

TASK [Gathering Facts] ***************************************************************************
ok: [vector-01]

TASK [Get Vector Package] ***************************************************************************
ok: [vector-01]

PLAY RECAP ***************************************************************************
clickhouse-01: ok=3    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
vector-01: ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

на новой инсталяции 
```ignorelang
kunaev@dub-ws-235:~/projects/devops-netology/8.ansible/8.2_playbook/playbook$ ansible-playbook -i inventory/prod.yml site.yml --check

PLAY [Install Clickhouse] ***************************************************************************

TASK [Gathering Facts] ***************************************************************************
ok: [clickhouse-01]

TASK [Get clickhouse distrib] ***************************************************************************
changed: [clickhouse-01] => (item=clickhouse-client)
changed: [clickhouse-01] => (item=clickhouse-server)
changed: [clickhouse-01] => (item=clickhouse-common-static)

TASK [Install clickhouse packages] ******************************************************************************************************************************************************************
failed: [clickhouse-01] (item=clickhouse-common-static-22.4.6.53.deb) => {"ansible_loop_var": "item", "changed": false, "item": "clickhouse-common-static-22.4.6.53.deb", "msg": "Unable to install package: E:Could not open file clickhouse-common-static-22.4.6.53.deb - open (2: No such file or directory)"}
failed: [clickhouse-01] (item=clickhouse-client-22.4.6.53.deb) => {"ansible_loop_var": "item", "changed": false, "item": "clickhouse-client-22.4.6.53.deb", "msg": "Unable to install package: E:Could not open file clickhouse-client-22.4.6.53.deb - open (2: No such file or directory)"}
failed: [clickhouse-01] (item=clickhouse-server-22.4.6.53.deb) => {"ansible_loop_var": "item", "changed": false, "item": "clickhouse-server-22.4.6.53.deb", "msg": "Unable to install package: E:Could not open file clickhouse-server-22.4.6.53.deb - open (2: No such file or directory)"}

PLAY RECAP ******************************************************************************************************************************************************************************************
clickhouse-01              : ok=2    changed=1    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0 
```

Ругается из-за того, что ему нечего пока устанавливать

* Запустите playbook на prod.yml окружении с флагом --diff. Убедитесь, что изменения на системе произведены.

```ignorelang
kunaev@dub-ws-235:~/projects/devops-netology/8.ansible/8.2_playbook/playbook$ ansible-playbook -i inventory/prod.yml site.yml --diff

PLAY [Install Clickhouse] ***************************************************************************

TASK [Gathering Facts] ***************************************************************************
Enter passphrase for key '/home/kunaev/.ssh/id_rsa': 
ok: [clickhouse-01]

TASK [Get clickhouse distrib] ***************************************************************************
changed: [clickhouse-01] => (item=clickhouse-client)
changed: [clickhouse-01] => (item=clickhouse-server)
changed: [clickhouse-01] => (item=clickhouse-common-static)

TASK [Install clickhouse packages] ***************************************************************************
Selecting previously unselected package clickhouse-common-static.
(Reading database ... 26185 files and directories currently installed.)
Preparing to unpack clickhouse-common-static-22.4.6.53.deb ...
Unpacking clickhouse-common-static (22.4.6.53) ...
Setting up clickhouse-common-static (22.4.6.53) ...
changed: [clickhouse-01] => (item=clickhouse-common-static-22.4.6.53.deb)
Selecting previously unselected package clickhouse-client.
(Reading database ... 26199 files and directories currently installed.)
Preparing to unpack clickhouse-client-22.4.6.53.deb ...
Unpacking clickhouse-client (22.4.6.53) ...
Setting up clickhouse-client (22.4.6.53) ...
changed: [clickhouse-01] => (item=clickhouse-client-22.4.6.53.deb)
Selecting previously unselected package clickhouse-server.
(Reading database ... 26212 files and directories currently installed.)
Preparing to unpack clickhouse-server-22.4.6.53.deb ...
Unpacking clickhouse-server (22.4.6.53) ...
Setting up clickhouse-server (22.4.6.53) ...
changed: [clickhouse-01] => (item=clickhouse-server-22.4.6.53.deb)

RUNNING HANDLER [Start clickhouse service] ***************************************************************************
changed: [clickhouse-01]

TASK [Create database] ***************************************************************************
changed: [clickhouse-01]

PLAY [Install Vector] ***************************************************************************

TASK [Gathering Facts] ***************************************************************************
ok: [vector-01]

TASK [Get Vector Package] ***************************************************************************
Selecting previously unselected package vector.
(Reading database ... 26226 files and directories currently installed.)
Preparing to unpack .../vector_0.30.0-1_amd64f9n8ztax.deb ...
Unpacking vector (0.30.0-1) ...
Setting up vector (0.30.0-1) ...
systemd-journal:x:101:
changed: [vector-01]

PLAY RECAP ***************************************************************************
clickhouse-01              : ok=5    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
vector-01                  : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
```

* Повторно запустите playbook с флагом --diff и убедитесь, что playbook идемпотентен.

```ignorelang
kunaev@dub-ws-235:~/projects/devops-netology/8.ansible/8.2_playbook/playbook$ ansible-playbook -i inventory/prod.yml site.yml --diff

PLAY [Install Clickhouse] ***************************************************************************

TASK [Gathering Facts] ***************************************************************************
Enter passphrase for key '/home/kunaev/.ssh/id_rsa': 
ok: [clickhouse-01]

TASK [Get clickhouse distrib] ***************************************************************************
ok: [clickhouse-01] => (item=clickhouse-client)
ok: [clickhouse-01] => (item=clickhouse-server)
ok: [clickhouse-01] => (item=clickhouse-common-static)

TASK [Install clickhouse packages] ***************************************************************************
ok: [clickhouse-01] => (item=clickhouse-common-static-22.4.6.53.deb)
ok: [clickhouse-01] => (item=clickhouse-client-22.4.6.53.deb)
ok: [clickhouse-01] => (item=clickhouse-server-22.4.6.53.deb)

TASK [Create database] ***************************************************************************
ok: [clickhouse-01]

PLAY [Install Vector] ***************************************************************************

TASK [Gathering Facts] ***************************************************************************
ok: [vector-01]

TASK [Get Vector Package] ***************************************************************************
ok: [vector-01]

PLAY RECAP ***************************************************************************
clickhouse-01              : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
vector-01                  : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```
Как видно - изменений нет

* Подготовьте README.md-файл по своему playbook. В нём должно быть описано: что делает playbook, какие у него есть параметры и теги.

Playbook описан в файле site.yml, в котром содержитва 2 plays:

- Install Clickhouse
- Install Vector 

Clickhouse.

Группа хостов: Clickhouse \
Состоит из 1 Hendler и 4 Tasks

В начале описывется Hendler, который перезагужает сервер после его установки

Таски: \
1. Скачивает пакеты с сайта https://packages.clickhouse.com. Переменные (версия и тип дистрибутива) задаются в group_vars/clickhouse. Предусмотрен rescue сценарий для скачивания дистрибутива с альтернативного источника 

2. Устанавливает скаченные пакеты
3. Запускает хендлер для перезапуска сервиса после установки
4. Согдает БД "logs". Определает статусы: failed код возврата не 0 и changes если 0.

Vector. \
Группа хостов: vector

Состоит из 1 хендлера и 1 таски. \

Хендлер нужен для перезапуска сервиса, для применения конфига (сам конфиг туда не подкидывал)

Таска - устанавливает пакет, скачивая его с нужного ресурса по http. Переменная для указания версии определеяется в group_vars/vector.


* Готовый playbook выложите в свой репозиторий, поставьте тег 08-ansible-02-playbook на фиксирующий коммит, в ответ предоставьте ссылку на него.



