# -*- mode: ruby -*-
# vi: set ft=ruby

VAGRANT_FILE_API_VERSION = 2

Vagrant.configure(VAGRANT_FILE_API_VERSION) do |config|

  config.vm.define "app" do |app|
    app.vm.box = "ubuntu/trusty64"
    app.vm.network :private_network, ip: "192.168.33.23"

    app.vm.provision "ansible" do |ansible|
      ansible.playbook = "ansible/development.yml"
      ansible.veborse = "vvv"
      ansible.groups = {
        "app" => "192.168.33.23"
      }
      ansible.limit = "app"
    end
  end

  config.vm.provider "virtualbox" do |virtualbox|
    virtualbox.customize ["modifyvm", :id, "--memory", "1024"]
  end
end
