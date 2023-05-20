variable "metadata_info" {
  default = {
    serial-port-enable = 1
    ssh-keys           = "ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGMnEWb24K3HZ4E0L7GvrcRUECIhelmu0eBKQuGtK4CR kunaev@dub-ws-235"
  }
  type = object({
    serial-port-enable = number
    ssh-keys           = string
  })
}

variable "web_platform_resources" {
  default = {
    cores         = 2
    memory        = 1
    core_fraction = 5
  }
  type = object({
    cores         = number
    memory        = number
    core_fraction = number
  })
}

variable "bd_platform_resources" {
  default = {
    cores         = 2
    memory        = 2
    core_fraction = 20
  }
  type = object({
    cores         = number
    memory        = number
    core_fraction = number
  })
}
#vm web image vars
variable "vm_web_image" {
  type        = string
  default     = "ubuntu-2004-lts"
  description = "https://cloud.yandex.ru/marketplace?categories=os"
}

#platform vars
variable "vm_web_platform_name" {
  type    = string
  default = "develop-platform-web"
}

variable "vm_web_maintenance_class" {
  type        = string
  default     = "standard-v1"
  description = "https://cloud.yandex.ru/docs/compute/concepts/vm-platforms"
}

###cloud vars
variable "token" {
  type        = string
  description = "OAuth-token; https://cloud.yandex.ru/docs/iam/concepts/authorization/oauth-token"
}

variable "cloud_id" {
  type        = string
  description = "https://cloud.yandex.ru/docs/resource-manager/operations/cloud/get-id"
}

variable "folder_id" {
  type        = string
  description = "https://cloud.yandex.ru/docs/resource-manager/operations/folder/get-id"
}

variable "default_zone" {
  type        = string
  default     = "ru-central1-a"
  description = "https://cloud.yandex.ru/docs/overview/concepts/geo-scope"
}
variable "default_cidr" {
  type        = list(string)
  default     = ["10.0.1.0/24"]
  description = "https://cloud.yandex.ru/docs/vpc/operations/subnet-create"
}

variable "vpc_name" {
  type        = string
  default     = "develop"
  description = "VPC network & subnet name"
}


###ssh vars

#variable "vms_ssh_root_key" {
#  type        = string
#  default     = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGMnEWb24K3HZ4E0L7GvrcRUECIhelmu0eBKQuGtK4CR kunaev@dub-ws-235"
#  description = "ssh-keygen -t ed25519"
#}
