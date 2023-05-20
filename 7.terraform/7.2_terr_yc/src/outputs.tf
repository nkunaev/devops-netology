output "platform" {
  value = yandex_compute_instance.platform.network_interface[0].nat_ip_address
}
output "platform_db" {
  value = yandex_compute_instance.platform-db.network_interface[0].nat_ip_address
}

output "platform_map" {
  value = {
    instance_name = yandex_compute_instance.platform.name
    external_ip   = yandex_compute_instance.platform-db.network_interface[0].nat_ip_address
  }
}

output "platform_db_map" {
  value = {
    instance_name = yandex_compute_instance.platform.name
    external_ip   = yandex_compute_instance.platform-db.network_interface[0].nat_ip_address
  }
}