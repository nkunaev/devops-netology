resource "yandex_compute_disk" "volumes" {
  count = 3

  name     = "disk-${count.index}"
  type     = "network-hdd"
  size     = 1
  zone     = "ru-central1-a"

}

resource "yandex_compute_instance" "vm_with_disks" {
  name        = "kunaev-vm-with-disks"
  platform_id = var.vm_countable_maintenance_class


  resources {
    cores         = 2
    memory        = 1
    core_fraction = 5
  }
  boot_disk {
    initialize_params {
      image_id    = data.yandex_compute_image.ubuntu.image_id
    }
  }

  dynamic secondary_disk {
    for_each    = yandex_compute_disk.volumes.*.id
    content {
      disk_id   = secondary_disk.value
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