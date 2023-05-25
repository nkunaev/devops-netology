locals {
  ssh-key = "ubuntu:${file("~/.ssh/yc_rsa.pub")}"
}