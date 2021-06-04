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

mkdir -p dist
cd src
zip -r ../dist/AndaluhLibreOffice-0.1.0.oxt *

# Uncomment this if you also want the extension to 
# be installed and LibreOffice automatically started

unopkg add -f "../dist/AndaluhLibreOffice-0.1.0.oxt"
soffice --norestore