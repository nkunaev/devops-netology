## Задача 1

Из-за того, что репозиторий elastic.co недоступен с территории РФ я собрал образ на базе Убунту 22 используя зеркало Яндекса.
* текст Dockerfile-манифеста
```dockerfile
FROM ubuntu:22.04

RUN apt update && apt install -y wget gpg ca-certificates tzdata && \
    useradd -MU elastic && mkdir /var/lib/nodes

ENV TZ="Europe/Moscow"

RUN wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | gpg --dearmor -o /usr/share/keyrings/elasticsearch-keyring.gpg && \
    echo "deb [trusted=yes signed-by=/usr/share/keyrings/elasticsearch-keyring.gpg] https://mirror.yandex.ru/mirrors/elastic/7/ stable main" | tee /etc/apt/sources.list.d/elastic-7.x.list && \
    apt update && apt install -y elasticsearch

COPY ./elasticsearch.yml /etc/elasticsearch/

RUN chown -R elastic:elastic /usr/share/elasticsearch && \
    chown -R elastic:elastic /etc/default/elasticsearch && \
    chown -R elastic:elastic /var/lib/elasticsearch && \
    chown -R elastic:elastic /etc/elasticsearch && \
    chown -R elastic:elastic /var/log/elasticsearch && \
    chown -R elastic:elastic /var/lib/nodes


EXPOSE 9200 9300

CMD ["su", "-", "elastic", "-c", "/usr/share/elasticsearch/bin/elasticsearch"]

```
* ссылку на образ в репозитории dockerhub
```ignorelang
https://hub.docker.com/repository/docker/kunaev/ubuntu22_elastic/general
```
* ответ Elasticsearch на запрос пути / в json-виде
```json
kunaev@dub-ws-235:~/projects/homework/hw65$ curl localhost:9200
{
  "name" : "netology_test",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "_PFheSXDSfuiswx3y6q6zA",
  "version" : {
    "number" : "7.17.9",
    "build_flavor" : "default",
    "build_type" : "deb",
    "build_hash" : "ef48222227ee6b9e70e502f0f0daa52435ee634d",
    "build_date" : "2023-01-31T05:34:43.305517834Z",
    "build_snapshot" : false,
    "lucene_version" : "8.11.1",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```

## Задача 2

* Ознакомьтесь с документацией и добавьте в Elasticsearch 3 индекса в соответствии с таблицей

```commandline
kunaev@dub-ws-235:~/projects/homework/hw65$ curl -X PUT "localhost:9200/ind-1?pretty" -H 'Content-Type: application/json' -d'
{
  "settings": {
    "index": {
      "number_of_shards": 1,  
      "number_of_replicas": 0 
    }
  }
}
'

kunaev@dub-ws-235:~/projects/homework/hw65$ curl -X PUT "localhost:9200/ind-2?pretty" -H 'Content-Type: application/json' -d'
{
  "settings": {
    "index": {
      "number_of_shards": 2,  
      "number_of_replicas": 1 
    }
  }
}
'

kunaev@dub-ws-235:~/projects/homework/hw65$ curl -X PUT "localhost:9200/ind-3?pretty" -H 'Content-Type: application/json' -d'
{
  "settings": {
    "index": {
      "number_of_shards": 4,  
      "number_of_replicas": 2 
    }
  }
}
'
```
* Получите список индексов и их статусов, используя API, и приведите в ответе на задание.

Список индексов
```commandline
kunaev@dub-ws-235:~/projects/homework/hw65$ curl -X GET localhost:9200/_cat/indices
green  open .geoip_databases Z1xCARq6QJqBf6Us9whVPA 1 0 42 0 40.5mb 40.5mb
green  open ind-1            7WkuySsORve53-OQ-ULaKA 1 0  0 0   226b   226b
yellow open ind-3            093Q4uYgS9m6AxKvk_WlPg 4 2  0 0   226b   226b
yellow open ind-2            SdPBhGYJS8C99byucrQVJw 2 1  0 0   452b   452b
```
Список их статусов
```commandline
{
  "cluster_name" : "elasticsearch",
  "status" : "yellow",
  "timed_out" : false,
  "number_of_nodes" : 1,
  "number_of_data_nodes" : 1,
  "active_primary_shards" : 10,
  "active_shards" : 10,
  "relocating_shards" : 0,
  "initializing_shards" : 0,
  "unassigned_shards" : 10,
  "delayed_unassigned_shards" : 0,
  "number_of_pending_tasks" : 0,
  "number_of_in_flight_fetch" : 0,
  "task_max_waiting_in_queue_millis" : 0,
  "active_shards_percent_as_number" : 50.0,
  "indices" : {
    ".geoip_databases" : {
      "status" : "green",
      "number_of_shards" : 1,
      "number_of_replicas" : 0,
      "active_primary_shards" : 1,
      "active_shards" : 1,
      "relocating_shards" : 0,
      "initializing_shards" : 0,
      "unassigned_shards" : 0
    },
    "ind-1" : {
      "status" : "green",
      "number_of_shards" : 1,
      "number_of_replicas" : 0,
      "active_primary_shards" : 1,
      "active_shards" : 1,
      "relocating_shards" : 0,
      "initializing_shards" : 0,
      "unassigned_shards" : 0
    },
    "ind-3" : {
      "status" : "yellow",
      "number_of_shards" : 4,
      "number_of_replicas" : 2,
      "active_primary_shards" : 4,
      "active_shards" : 4,
      "relocating_shards" : 0,
      "initializing_shards" : 0,
      "unassigned_shards" : 8
    },
    "ind-2" : {
      "status" : "yellow",
      "number_of_shards" : 2,
      "number_of_replicas" : 1,
      "active_primary_shards" : 2,
      "active_shards" : 2,
      "relocating_shards" : 0,
      "initializing_shards" : 0,
      "unassigned_shards" : 2
    }
  }
}

```

* Получите состояние кластера Elasticsearch, используя API.
```commandline
kunaev@dub-ws-235:~/projects/homework/hw65$ curl -X GET localhost:9200/_cluster/health?pretty
{
  "cluster_name" : "elasticsearch",
  "status" : "yellow",
  "timed_out" : false,
  "number_of_nodes" : 1,
  "number_of_data_nodes" : 1,
  "active_primary_shards" : 10,
  "active_shards" : 10,
  "relocating_shards" : 0,
  "initializing_shards" : 0,
  "unassigned_shards" : 10,
  "delayed_unassigned_shards" : 0,
  "number_of_pending_tasks" : 0,
  "number_of_in_flight_fetch" : 0,
  "task_max_waiting_in_queue_millis" : 0,
  "active_shards_percent_as_number" : 50.0
}
```

* Как вы думаете, почему часть индексов и кластер находятся в состоянии yellow?

Полагаю дело в том, что при создании индексов мы указали наличие определенного количества реплик, которые фактически отсутствуют и как следствие
неназначенных шардов.

* Удалите все индексы.

```commandline
kunaev@dub-ws-235:~/projects/homework/hw65$ curl -X DELETE 'http://127.0.0.1:9200/ind-1'
{"acknowledged":true}
kunaev@dub-ws-235:~/projects/homework/hw65$ curl -X DELETE 'http://127.0.0.1:9200/ind-2'
{"acknowledged":true}
kunaev@dub-ws-235:~/projects/homework/hw65$ curl -X DELETE 'http://127.0.0.1:9200/ind-3'
{"acknowledged":true}
```

## Задание 3

* Создайте директорию {путь до корневой директории с Elasticsearch в образе}/snapshots
* Используя API, зарегистрируйте эту директорию как snapshot repository c именем netology_backup.
* Приведите в ответе запрос API и результат вызова API для создания репозитория.
```commandline
kunaev@dub-ws-235:~/projects/homework/hw65$ curl -X PUT "localhost:9200/_snapshot/netology_backup?pretty" -H 'Content-Type: application/json' -d'
{
  "type": "fs",
  "settings": {
    "location": "/tmp/elastic_backup"
  }
}
'
{
  "acknowledged" : true
}
```
* Создайте индекс test с 0 реплик и 1 шардом и приведите в ответе список индексов.
```commandline
kunaev@dub-ws-235:~/projects/homework/hw65$ curl -X PUT "localhost:9200/test?pretty" -H 'Content-Type: application/json' -d'
{
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 0
  }
}
'
{
  "acknowledged" : true,
  "shards_acknowledged" : true,
  "index" : "test"
}
```
* Создайте snapshot состояния кластера Elasticsearch.
```commandline
kunaev@dub-ws-235:~/projects/homework/hw65$ curl -X PUT "localhost:9200/_snapshot/netology_backup/snapshot_1?wait_for_completion=true&pretty"
{
  "snapshot" : {
    "snapshot" : "snapshot_1",
    "uuid" : "p60uUgh0Tk231CvcW9BAmg",
    "repository" : "netology_backup",
    "version_id" : 7170999,
    "version" : "7.17.9",
    "indices" : [
      "test",
      ".ds-ilm-history-5-2023.04.27-000001",
      ".geoip_databases",
      ".ds-.logs-deprecation.elasticsearch-default-2023.04.27-000001"
    ],
    "data_streams" : [
      "ilm-history-5",
      ".logs-deprecation.elasticsearch-default"
    ],
    "include_global_state" : true,
    "state" : "SUCCESS",
    "start_time" : "2023-04-27T13:32:39.359Z",
    "start_time_in_millis" : 1682602359359,
    "end_time" : "2023-04-27T13:32:40.760Z",
    "end_time_in_millis" : 1682602360760,
    "duration_in_millis" : 1401,
    "failures" : [ ],
    "shards" : {
      "total" : 4,
      "failed" : 0,
      "successful" : 4
    },
    "feature_states" : [
      {
        "feature_name" : "geoip",
        "indices" : [
          ".geoip_databases"
        ]
      }
    ]
  }
}
```
* Приведите в ответе список файлов в директории со snapshot.
```commandline
kunaev@dub-ws-235:~/projects/homework/hw65$ docker exec -it elastic bash -c 'ls -l /tmp/elastic_backup'
total 48
-rw-r--r-- 1 root    root        0 Apr 27 16:00 hello.txt
-rw-rw-r-- 1 elastic elastic  1422 Apr 27 16:32 index-0
-rw-rw-r-- 1 elastic elastic     8 Apr 27 16:32 index.latest
drwxrwxr-x 6 elastic elastic  4096 Apr 27 16:32 indices
-rw-rw-r-- 1 elastic elastic 29317 Apr 27 16:32 meta-p60uUgh0Tk231CvcW9BAmg.dat
-rw-rw-r-- 1 elastic elastic   709 Apr 27 16:32 snap-p60uUgh0Tk231CvcW9BAmg.dat

```
* Удалите индекс test и создайте индекс test-2. Приведите в ответе список индексов.
```commandline
kunaev@dub-ws-235:~/projects/homework/hw65$ curl -X GET localhost:9200/_cat/indices
green open .geoip_databases OyzBkuI1QSy_AlqupIXSGw 1 0 42 0 40.5mb 40.5mb
green open test-2           RQbSOhRfQeqqlp4q5izOgA 1 0  0 0   226b   226b

```
* Восстановите состояние кластера Elasticsearch из snapshot, созданного ранее.
* Приведите в ответе запрос к API восстановления.

```commandline
kunaev@dub-ws-235:~/projects/homework/hw65$ curl -X POST "localhost:9200/_snapshot/netology_backup/snapshot_1/_restore?pretty" -H 'Content-Type: application/json' -d'
{
  "indices": "test"
}
'
{
  "accepted" : true
}
```
* итоговый список индексов
```commandline
kunaev@dub-ws-235:~/projects/homework/hw65$ curl -X GET localhost:9200/_cat/indices?pretty
green open .geoip_databases OyzBkuI1QSy_AlqupIXSGw 1 0 42 0 40.5mb 40.5mb
green open test-2           RQbSOhRfQeqqlp4q5izOgA 1 0  0 0   226b   226b
green open test             UfPbOgTBQ8e_0slpuqBbwQ 1 0  0 0   226b   226b

```