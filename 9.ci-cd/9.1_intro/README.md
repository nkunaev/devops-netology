# CI/CD Intro

## Подготовка к выполнению

* Создать доски Kanban и Scrum.

![img.png](img/img.png)

## Основная часть

* Необходимо создать собственные workflow для bug 

    Open -> On reproduce.  
    On reproduce -> Open, Done reproduce.  
    Done reproduce -> On fix.  
    On fix -> On reproduce, Done fix.  
    Done fix -> On test.  
    On test -> On fix, Done.  
    Done -> Closed, Open.  

![img_3.png](img/img_3.png)

* Необходимо создать собственные workflow для остальных.

    Open -> On develop.  
    On develop -> Open, Done develop.  
    Done develop -> On test.  
    On test -> On develop, Done.  
    Done -> Closed, Open.  

![img_1.png](img/img_1.png)

## TO DO

* Создайте задачу с типом bug, попытайтесь провести его по всему workflow до Done.

![img_2.png](img/img_2.png)

* Создайте задачу с типом epic, к ней привяжите несколько задач с типом task, проведите их по всему workflow до Done. При проведении обеих задач по статусам используйте kanban.

![img_4.png](img/img_4.png)


* Верните задачи в статус Open.
![img_5.png](img/img_5.png)

* Перейдите в Scrum, запланируйте новый спринт, состоящий из задач эпика и одного бага, стартуйте спринт, проведите задачи до состояния Closed. Закройте спринт.
![img_6.png](img/img_6.png)
![img_7.png](img/img_7.png)
* Если всё отработалось в рамках ожидания — выгрузите схемы workflow для импорта в XML. Файлы с workflow и скриншоты workflow приложите к решению задания.
