#!/bin/bash

cp ~/.bash_aliases ./global/.bash_aliases
cp ~/.emacs ./global/.emacs

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
    cp ~/.network_aliases ./local/.network_aliases
    fi
if [ "$SESSION_TYPE" == "remote/ssh" ];
    then
    cp ~/.network_aliases ./remote/.network_aliases 
    fi
