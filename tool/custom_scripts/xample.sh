#!/bin/bash

### IMPORT FUNCTIONS AND VARIABLES FROM TOOLS ###
TOOLDIR="$(dirname "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")")"
source $TOOLDIR/functions
#################################################
clear
#################################################

### write script here ###

echo $PWD
echo $WORKDIR
echo $DIRSCRIPTS
echo $TOOLDIR
echo $PYSCRIPTS
echo $DIRIN
echo $DIROUT
echo $WORKDIR
echo Hello

#################################################
restart_tool
exit
#################################################
