resource "yandex_vpc_network" "stage" {
  name = "stage"
}

resource "yandex_vpc_subnet" "stage" {
  name           = "stage-${var.zone}"
  zone           = var.zone
  network_id     = yandex_vpc_network.stage.id
  v4_cidr_blocks = var.cidr
}

