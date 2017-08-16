#!/bin/bash
destination=$1
if [ $destination == "local" ];
    then
    cp ./local/.bashrc ~/.bashrc
    fi
if [ $destination == "remote" ];
    then
    cp ./remote/.bashrc ~/.bashrc
    fi

