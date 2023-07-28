locals {
  ssh-key = "centos:${file("~/.ssh/settings.pub")}"
}

