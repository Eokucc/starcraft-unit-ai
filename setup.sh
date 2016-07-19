#!/bin/bash

sudo apt-get install -y python python-setuptools
sudo apt-get purge -y python-pip
sudo easy_install pip
sudo pip install -r requirements.txt
