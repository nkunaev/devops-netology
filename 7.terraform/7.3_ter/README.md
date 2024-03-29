## Задание 1

* Инициализация проекта прошла успешно
![img.png](img/img.png)

* Приложите скриншот входящих правил "Группы безопасности" в ЛК Yandex Cloud 
![img_1.png](img/img_1.png)

## Задание 2

1. Создайте файл count-vm.tf. Опишите в нем создание двух **одинаковых** виртуальных машин с минимальными параметрами, используя мета-аргумент **count loop**. \
Созданы 2 VM в "минимальной" комплектации.
![img_2.png](img/img_2.png)

2.Создайте файл for_each-vm.tf. 
Опишите в нем создание 2 разных по cpu/ram/disk виртуальных машин, используя мета-аргумент for_each loop.
Используйте переменную типа list(object({ vm_name=string, cpu=number, ram=number, disk=number })).
При желании внесите в переменную все возможные параметры.

Создана переменная со списком словарей
```terraform
variable "vm_resources_list" {
  type = list(object({
    vm_name       = string
    cpu           = number
    ram           = number
    disk          = number
    core_fraction = number
  }))
  default = [
    {
      vm_name       = "vm-1"
      cpu           = 2
      ram           = 1
      disk          = 1
      core_fraction = 5

    },
        {
      vm_name       = "vm-2"
      cpu           = 2
      ram           = 2
      disk          = 3
      core_fraction = 5
    },
  ]
  description = "There's list if dict's with VM resources"
}

```

В блоке resources, в разделе for_each идет итерация по списку

```terraform
  for_each   = {
    for index, vm in var.vm_resources_list:
    vm.vm_name => vm
  }
  name        = each.value.vm_name

  resources {
    cores         = each.value.cpu
    memory        = each.value.ram
    core_fraction = each.value.core_fraction

  }
```

3. ВМ из пункта 2.2 должны создаваться после создания ВМ из пункта 2.1.

  depends_on = [yandex_compute_instance.vm_countable]
  
4. Используйте функцию file в local переменной для считывания ключа ~/.ssh/id_rsa.pub и его последующего использования в блоке metadata, взятому из ДЗ №2.

```terraform
locals {
  ssh-key = "ubuntu:${file("~/.ssh/ya_key.pub")}"
}
```

Использование:

```terraform
  metadata = {
    serial-port-enable = var.metadata_info.serial-port-enable
    ssh-keys           = local.ssh-key
  }
```
5. Инициализируйте проект, выполните код
![img_3.png](img/img_3.png)

## Задание 3

* Создайте 3 одинаковых виртуальных диска, размером 1 Гб с помощью ресурса yandex_compute_disk и мета-аргумента count в файле disk_vm.tf .

```terraform
resource "yandex_compute_disk" "volumes" {
  count = 3

  name     = "disk-${count.index}"
  type     = "network-hdd"
  size     = 1
  zone     = "ru-central1-a"

}
```

* Создайте в том же файле одну любую ВМ. Используйте блок dynamic secondary_disk{..} и мета-аргумент for_each для подключения созданных вами дополнительных дисков.

```terraform
resource "yandex_compute_instance" "vm_with_disks" {
  name        = "kunaev-vm-with-disks"
  platform_id = var.vm_countable_maintenance_class
  #####################################################

  dynamic secondary_disk {
    for_each = yandex_compute_disk.volumes.*.id
    content {
      disk_id = secondary_disk.value
    }
  }
}
```

* Назначьте ВМ созданную в 1-м задании группу безопасности.

```terraform
  network_interface {
    subnet_id = yandex_vpc_subnet.develop.id
    nat       = true
    security_group_ids = [yandex_vpc_security_group.example.id]
  }
```

![img_4.png](img/img_4.png)

## Задание 4
* В файле ansible.tf создайте inventory-файл для ansible. Используйте функцию tepmplatefile и файл-шаблон для создания ansible inventory-файла из лекции. Готовый код возьмите из демонстрации к лекции demonstration2. Передайте в него в качестве переменных имена и внешние ip-адреса ВМ из задания 2.1 и 2.2.
```terraform
resource "local_file" "inventory_cfg" {
  content = templatefile("${path.module}/ansible.tftpl", {
    servers_countable   = yandex_compute_instance.vm_countable
    servers_for_each    = yandex_compute_instance.vm_for_each
  })
  filename = "${abspath(path.module)}/inventory.cfg"
}
```

* Выполните код. Приложите скриншот получившегося файла.

```ignorelang
[servers]

kunaev-vm-countable-0   ansible_host=51.250.94.108
kunaev-vm-countable-1   ansible_host=84.201.129.228
vm-1   ansible_host=62.84.125.175
vm-2   ansible_host=130.193.36.108
```

Ссылка на коммит в созданной ветке
e6a9b24 (HEAD -> terraform-03, origin/terraform-03) hw7.3_kunaev
