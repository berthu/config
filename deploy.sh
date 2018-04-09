#!/bin/bash

cp ./global/.bash_aliases ~/.bash_aliases
cp ./global/.emacs ~/.emacs
cp ./global/.gitconfig ~/.gitconfig

# check if in an SSH client
if [ -n "$SSH_CLIENT" ] || [ -n "$SSH_TTY" ]; then
  SESSION_TYPE=remote/ssh
else
  case $(ps -o comm= -p $PPID) in
    sshd|*/sshd) SESSION_TYPE=remote/ssh;;
  esac
fi


if [ "$SESSION_TYPE" != "remote/ssh" ];
    then
    cp ./local/.network_aliases ~/.network_aliases
    fi
if [ "$SESSION_TYPE" == "remote/ssh" ];
    then
    cp ./remote/.network_aliases ~/.network_aliases
    fi

source ~/.bash_aliases
