#!/bin/bash
destination=$1
if [ $destination == "local" ];
    then
    cp ./local/.bash_aliases ~/.bash_aliases
    fi
if [ $destination == "remote" ];
    then
    cp ./remote/.bash_aliases ~/.bash_aliases
    fi

