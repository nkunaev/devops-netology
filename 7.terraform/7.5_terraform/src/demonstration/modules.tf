module "additional_network" {
  source = "./modules/additional_network"
  zone   = "ru-central1-a"
  cidr   = ["172.16.0.0/24"]
}
