#!/bin/bash
#
# Packages the extension and build the .oxt file 
# under dist/. Do not forget to rename file to 
# set the proper version!
# 
# Copyleft (c) 2021 AndaluGeeks Team
# 
# Authors : 
#   J. Félix Ontañón <felixonta@gmail.com> 


# Upgrade andaluh dependency from pip
# pip3 install andaluh -t src/ --upgrade

# Remove unuself files from dependency
# rm -rf src/bin/ src/andaluh-0.2.1.dist-info/

# Package as oxt libreoffice extension file
mkdir -p dist
cd src

# Uncomment this if you also want the extension to 
# be installed and LibreOffice automatically started

# If extension was installed, remove first
unopkg remove es.andaluh.AndaluhLibre
rm -f ../dist/AndaluhLibreOffice-0.1.0.oxt
zip -r ../dist/AndaluhLibreOffice-0.1.0.oxt *
unopkg add -f "../dist/AndaluhLibreOffice-0.1.0.oxt"
soffice --norestore