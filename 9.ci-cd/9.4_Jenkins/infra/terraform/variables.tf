variable "metadata_info" {
  default = {
    serial-port-enable = 1
  }
  type = object({
    serial-port-enable = number
  })
}

variable "platform_resources" {
  default = {
    cores         = 2
    memory        = 4
    core_fraction = 5
  }
  type = object({
    cores         = number
    memory        = number
    core_fraction = number
  })
}

variable "vm_image" {
  type        = string
  default     = "centos-stream-8"
  description = "https://cloud.yandex.ru/marketplace?categories=os"
}

#platform vars
variable "platform_name" {
  type    = string
  default = "centos-stream-8"
}

variable "vm_maintenance_class" {
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

