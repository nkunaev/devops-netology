#vm db image vars

variable "vm_db_image" {
  type        = string
  default     = "ubuntu-2004-lts"
  description = "https://cloud.yandex.ru/marketplace?categories=os"
}

#platform vars
variable "vm_db_platform_name" {
  type    = string
  default = "develop-platform-db"
}

variable "vm_db_maintenance_class" {
  type        = string
  default     = "standard-v1"
  description = "https://cloud.yandex.ru/docs/compute/concepts/vm-platforms"
}

# resourse description

resource "yandex_compute_instance" "platform-db" {
  name        = local.db_name
  platform_id = var.vm_db_maintenance_class

  resources {
    cores         = var.bd_platform_resources.cores
    memory        = var.bd_platform_resources.memory
    core_fraction = var.bd_platform_resources.core_fraction
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
    ssh-keys           = var.metadata_info.ssh-keys
  }

}