#!/usr/bin/bash

#hexedit garden.jpg | grep -oE "picoCTF{.*}"

#or

#xxd garden.jpg

#or 

#xxd -p garden.jpg 


strings garden.jpg | tail -n 1 | cut -d '"' -f2
