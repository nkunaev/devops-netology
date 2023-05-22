variable "vm_resources_list" {
  type = map
    default = {
      vm-1 = {
        cpu = 2
        ram = 1
        disk = 1
        core_fraction = 5
      }
      vm-2 = {
        cpu = 2
        ram = 2
        disk          = 3
        core_fraction = 5
        }
  }
  description = "There's list if dict's with VM resources"
}


resource "yandex_compute_instance" "vm_for_each" {
  depends_on = [yandex_compute_instance.vm_countable]
  # определим имена и ресурсы
#  for_each   = {
#    for index, vm in var.vm_resources_list:
#    vm.vm_name => vm
#  }

  for_each   =  var.vm_resources_list
  name        = each.key
  platform_id = var.vm_countable_maintenance_class

  resources {
    cores         = each.value.cpu
    memory        = each.value.ram
    core_fraction = each.value.core_fraction

  }
  boot_disk {
    initialize_params {
      image_id = data.yandex_compute_image.ubuntu.image_id
    }
  }
  scheduling_policy {
    preemptible = true
  }
  network_interface {
    subnet_id = yandex_vpc_subnet.develop.id
    nat       = true
  }

  metadata = {
    serial-port-enable = var.metadata_info.serial-port-enable
    ssh-keys           = local.ssh-key
  }
}