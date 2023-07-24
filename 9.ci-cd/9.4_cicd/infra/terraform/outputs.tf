output "platform_hw_cicd" {
  value = {
    instance_name = yandex_compute_instance.platform[*].name
    external_ip   = yandex_compute_instance.platform[*].network_interface[0].nat_ip_address
  }
}