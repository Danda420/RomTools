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
echo $PRJDIR
echo $erofsdir
echo $ext4dir
echo $f2fsdir
echo $superdir
echo $u_bootdir
echo $DIRSCRIPTS
echo $TOOLDIR
echo $PYSCRIPTS
echo $DIRIN
echo Hello

#################################################
restart_tool
exit
#################################################
