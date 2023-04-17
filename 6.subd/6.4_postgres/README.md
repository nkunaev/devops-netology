## Задача 1

Используя Docker, поднимите инстанс PostgreSQL (версию 13). Данные БД сохраните в volume.

```ignorelang
docker pull postgres:13
docker run --name postgres1 -v $(pwd)/test_db:/tmp/test_db -e POSTGRES_PASSWORD=Qwaszx -d postgres:13
docker exec -it postgres1 psql -U postgres
```

Найдите и приведите управляющие команды для:

* вывода списка БД
```ignorelang
\l[+]
```
* подключения к БД
```ignorelang
\c[onnect] {[DBNAME|- USER|- HOST|- PORT|-] | conninfo}
```
* вывода списка таблиц
```ignorelang
\dt[+]
```
* вывода описания содержимого таблиц
```ignorelang
 \d[S+]  NAME  describe table, view, sequence, or index
```
* выхода из psql
```ignorelang
\q
```

## Задача 2

Вложенный запрос с фильтром по названию таблицы и макс. значению.
```ignorelang
test_database=# SELECT attname, avg_width FROM pg_stats WHERE avg_width = (SELECT MAX(avg_width) FROM pg_stats WHERE tablename = 'orders');
 title   |        16
```

## Задача 3

В ходе выполнения 3 задания я "вдохновлялся" выступлением специалиста на конференции [Highload++](https://habr.com/ru/companies/oleg-bunin/articles/309330/) и статьи об партицировании с [Хабра](https://habr.com/ru/companies/skyeng/articles/583222/). Выбор в пользу метода
партицирования таблиц через наследование обусловлен отсутствием даунтайма и изменнеия уже существующей таблицы.


```ignorelang
BEGIN;
CREATE TABLE orders_new(id INTEGER NOT NULL, title VARCHAR(80) NOT NULL, price INTEGER DEFAULT 0);
CREATE TABLE orders_1 (CHECK (price > 499)) INHERITS (orders_new);
CREATE TABLE orders_2 (CHECK (price <= 499)) INHERITS (orders_new);
CREATE RULE orders_insert_to_1 AS ON INSERT TO orders_new WHERE (price > 499) DO INSTEAD INSERT INTO orders_1 VALUES (NEW.*);
CREATE RULE orders_insert_to_2 AS ON INSERT TO orders_new WHERE (price <= 499) DO INSTEAD INSERT INTO orders_2 VALUES (NEW.*);
INSERT INTO orders_new SELECT * FROM orders;
DROP TABLE orders;
ALTER TABLE orders_new RENAME TO orders;
commit;
```

Как видно на примере:
```ignorelang
test_database=# explain select * from orders where price = 150;
 Append  (cost=0.00..14.77 rows=3 width=186)
   ->  Seq Scan on orders orders_1  (cost=0.00..0.00 rows=1 width=186)
         Filter: (price = 150)
   ->  Seq Scan on orders_2  (cost=0.00..14.75 rows=2 width=186)
         Filter: (price = 150)
```
Поиск сказу стал происходить по таблице orders_2.

* Можно ли было изначально исключить ручное разбиение при проектировании таблицы orders?

На мой взгляд можно, но полагаю, что чаще всего заранее неизвестно какие столбцы необходимо разбивать.

## Задача 4

* Используя утилиту pg_dump, создайте бекап БД test_database

```ignorelang
docker exec -it postgres1 pg_dump -U postgres -f /tmp/test_db/db_dump.sql test_database
```
* Как бы вы доработали бэкап-файл, чтобы добавить уникальность значения столбца title для таблиц test_database?
BEFORE
```ignorelang
CREATE TABLE public.orders (
    id integer NOT NULL,
    title character varying(80) NOT NULL,
    price integer DEFAULT 0
);
```

Можно к столбцу title можно добавить свойство UNIQUE, которое накладывает ограничение на столбец, обеспечивающие их уникальность.

Дополнительно (надо было сделать конечно при создании таблицы), установить у поля
id тип данных serial (аналог auto increment) и назначить первичным ключем. Эти же свойства унаследуют и дочерние таблицы, однако для них нужно будет отдельно создавать индексы.


AFTER
```ignorelang
CREATE TABLE public.orders (
    id serial NOT NULL PRIMARY KEY,
    title character varying(80) NOT NULL UNIQUE,
    price integer DEFAULT 0
);

```