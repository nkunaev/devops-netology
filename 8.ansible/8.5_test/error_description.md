Вводные такие:  
Работаю я на Кубунте22 (форк убунты 22 с кде). Докер демон работает под рутом, мой юзер добавлен в его группу, чтобы через судо не теребить постоянно.  

Симптомы такие:  
Написал я файл - молекулу, в нем описываю хосты которые мне нужны. Например centos-8 и убунту22. Запускаю, после чего начинают отрабатывать таски. На моменте вызова хендлера мне говорит "не знаю никаких сервисов (Service is in unknown state)", но нужно же чекать состояние сервиса (status), автозагрузку (enabled), т.е. результат работы ансибла на целевых хостах.

Иду в гугл, ищу какие образы используют для теста ансибл ролей и нахожу geerlingguy (https://github.com/geerlingguy/molecule-playbook-testing) , который еще книгу написал "Ansible for devops". Беру его образы и повторяю попытку - тоже самое. 

Параллельно пробую просто руками по гайду из гита запустить контейнер(docker run --detach --privileged --volume=/sys/fs/cgroup:/sys/fs/cgroup:rw --cgroupns=host geerlingguy/docker-ubuntu2204-ansible:latest), затем залезаю в контейнер, чекаю - все ок Systemd работает, сервисы показывает. (systemctl status *servicename*)

Я переношу эти параметры в конфигу молекулы, запускаю - опять не работает. 

Думаю, может параметры не передаются или apparmor шалит. Запускаю в дебаг моде molecule —dubug test и смотрю какие параметры молекула в докер передает.

```ignorelang

molecule --debug test

TASK [Determine the CMD directives] ********************************************
ok: [localhost] => (item={'cgroupns_mode': 'host', 'hostname': 'centos', 'image': 'geerlingguy/docker-centos8-ansible:latest', 'name': 'centos-8', 'pre_build_image': True, 'privileged': True, 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup:rw']})
```

Ну и соответственно все выполняется
```ignorelang


TASK [Wait for instance(s) creation to complete] *******************************
changed: [localhost] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': 'j912998414540.45378', 'results_file': '/home/kunaev/.ansible_async/j912998414540.45378', 'changed': True, 'item': {'cgroupns_mode': 'host', 'hostname': 'centos', 'image': 'geerlingguy/docker-centos8-ansible:latest', 'name': 'centos-8', 'pre_build_image': True, 'privileged': True, 'volumes': ['/sys/fs/cgroup:/sys/fs/cgroup:rw']}, 'ansible_loop_var': 'item'})
```


Думаем дальше... Запускаю тест с флагом —destroy=never и ныряю в контейнер. Пытаюсь там запустить systemd, в ответ тоже болт, но более понятный, говорит, что у systemd должен быть pid 1 (самый первый запущенный процесс)

```ignorelang

root@ubuntu:/# systemctl 
System has not been booted with systemd as init system (PID 1). Can't operate.
Failed to connect to bus: Host is down
```

Начал гуглить почему же он не первый. Были разные варианты, что режим монтирования volume с cgroups надо поменять и как tmpfs примонтировать /run и /tmp, в итоге все мимо. Потом я догадался сделать ps aux, и явилось мне чудо, а именно

```ignorelang

root@ubuntu:/# ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.0   4360  3268 ?        Ss   10:12   0:00 bash -c while true; do sleep 10000; done
root           7  0.0  0.0   2788   996 ?        S    10:12   0:00 sleep 10000
root         284  0.0  0.0   4624  3784 pts/0    Ss   10:14   0:00 bash
root         294  0.0  0.0   7060  1580 pts/0    R+   10:18   0:00 ps aux
```

Т.е. первый процесс вызывал слип на 10000, а потом потихоньку считал. Ну я тут и вспомнил, что в докере CMD вызывает команду, с которой запускается контейнер и уже в молекуле, в модуле command вызвал /lib/systemd/systemd, и это сработало!

Systemd запустился первым, пакеты поставились, хендлер отработал и тесты прошли успешно.


Итоговый конфиг для хоста получился таким:
```yaml
 - name: ubuntu22-latest
    hostname: ubuntu
    image: geerlingguy/docker-ubuntu2204-ansible:latest
    cgroupns_mode: host
    volumes:
      - /sys/fs/cgroup:/sys/fs/cgroup:rw
    privileged: true
    command: /lib/systemd/systemd
    pre_build_image: true
```