output "added_network_id" {
  value = yandex_vpc_network.stage.id
}

output "added_subnet_id" {
  value = yandex_vpc_subnet.stage.id
}

output "added_subnet_netmask" {
  value = yandex_vpc_subnet.stage.v4_cidr_blocks
}