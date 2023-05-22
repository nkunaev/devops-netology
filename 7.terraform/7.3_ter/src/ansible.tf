resource "local_file" "inventory_cfg" {
  content = templatefile("${path.module}/ansible.tftpl", {
    servers_countable   = yandex_compute_instance.vm_countable
    servers_for_each    = yandex_compute_instance.vm_for_each
  })
  filename = "${abspath(path.module)}/inventory.cfg"
}