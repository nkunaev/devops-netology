variable "zone" {
  type        = string
  default     = "ru-central1-a"
  description = "https://cloud.yandex.ru/docs/overview/concepts/geo-scope"
  validation {
    condition = contains(["ru-central1-a", "ru-central1-b", "ru-central1-c"], var.zone)
    error_message = "Invalid zone, choose one of ru-central1-{a, b or c}."
  }
}

variable "cidr" {
  type        = list(string)
  default     = ["172.16.0.0/24"]
  description = "https://networkencyclopedia.com/local-address/"
}