#!/bin/bash
destination=$1
if [ $destination == "local" ];
    then
    cp ./configs/local/.bashrc ~/.bashrc
    fi
if [ $destination == "remote" ];
    then
    cp ./configs/remote/.bashrc ~/.bashrc
    fi

