variable "vm_count_image" {
  type        = string
  default     = "ubuntu-2004-lts"
  description = "https://cloud.yandex.ru/marketplace?categories=os"
}

#platform vars

variable "vm_countable_maintenance_class" {
  type        = string
  default     = "standard-v1"
  description = "https://cloud.yandex.ru/docs/compute/concepts/vm-platforms"
}

# resourse description

resource "yandex_compute_instance" "vm_countable" {
  count       = 2
  name        = "kunaev-vm-countable-${count.index}"
  platform_id = var.vm_countable_maintenance_class

  resources {
    cores         = 2
    memory        = 1
    core_fraction = 5
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