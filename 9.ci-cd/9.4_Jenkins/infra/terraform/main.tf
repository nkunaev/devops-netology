
data "yandex_compute_image" "centos7" {
  family = var.vm_image
}

resource "yandex_compute_instance" "platform" {
  count = 2

  name        = "${var.platform_name}-jenkins-server-${count.index}"
  hostname = "${var.platform_name}-jenkins-server-${count.index}"
  platform_id = var.vm_maintenance_class

  resources {
    cores         = var.platform_resources.cores
    memory        = var.platform_resources.memory
    core_fraction = var.platform_resources.core_fraction
  }
  boot_disk {
    initialize_params {
      image_id = data.yandex_compute_image.centos7.image_id
    }
  }
  scheduling_policy {
    preemptible = true
  }
  network_interface {
    subnet_id = yandex_vpc_subnet.develop.id
    nat       = true
    security_group_ids = [yandex_vpc_security_group.example.id]
  }

  metadata = {
    serial-port-enable = var.metadata_info.serial-port-enable
    ssh-keys           = local.ssh-key
  }
}
