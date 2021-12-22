#!/bin/bash
# Checking whether user has enough permission to run this script
sudo -n true
if [ $? -ne 0 ]
    then
        echo "This script requires user to have passwordless sudo access"
        exit
fi
 sudo apt-get update
 # Install debian package of elasticsearch
 sudo wget  --directory-prefix=/opt/ https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.9.2-amd64.deb
 sudo dpkg -i /opt/elasticsearch-7.9.2-amd64.deb
 #install kibana
 sudo apt-get install apt-transport-https
 sudo wget  --directory-prefix=/opt/ https://artifacts.elastic.co/downloads/kibana/kibana-7.9.2-amd64.deb
 sudo dpkg -i /opt/kibana-7.9.2-amd64.deb
 sudo systemctl restart elasticsearch
 sudo systemctl enable elasticsearch
 sudo systemctl restart kibana
 sudo systemctl enable kibana
