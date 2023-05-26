output "additional_vpc_network_id" {
  description = "net_module_network_id"
  value = module.additional_network.added_network_id
}

output "additional_vpc_subnet_id" {
  description = "net_module_subnet_id"
  value = module.additional_network.added_subnet_id
}

output "additional_vpc_netmask" {
  description = "net_module_cidr_info"
  value = module.additional_network.added_subnet_netmask[0]
}