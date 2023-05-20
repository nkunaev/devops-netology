locals {
  ssh-key = "ubuntu:${file("~/.ssh/ya_key.pub")}"
}