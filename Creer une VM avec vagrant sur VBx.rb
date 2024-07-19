# creer une VM avec vagrant sur VBx
# installer vagrant sur windows 11 depuis le web 
# https://www.vagrantup.com/docs/vagrantup/installation




Vagrant.configure("2") do |config|

    config.vm.box = "" # < Mettre ici le nom de la box pour installer la VM sur VBx > le choix sera une box ubuntu 20.04 

end

# mettre la box ubuntu 20.04 dans VBx

vagrant.configure("2") do |config|

    Vagrant.configure("2") do |config|
        config.vm.network "public_network", ip: "89.0.142.86", auto_config: false, nat : true , name : "wlan0" 
        config.vm.network "private_network", type: "static", ip: "192.168.40.11"
        config.vm.network "forwarded_port", guest: 80, host: 8080
      end
end
