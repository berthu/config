#!/bin/bash
# SSH addresses

# git functions
alias ga='git add'
alias gp='git push'
#alias gl='git log --graph --abbrev-commit --pretty=oneline --decorate --branches'
alias gl='git log --graph --pretty=format:"%C(green)%h%Creset %C(blue)%an%Creset -%C(red)%d%Creset %s %C(yellow)%cd" --branches --date=short'
alias gs='git status'
alias gd='git diff'
alias gm='git commit -m'
alias gam='git commit -am'
alias gca='git commit -a'
alias gb='git branch -avv'
alias gc='git checkout'
alias gcb='git checkout -b'
alias gr='git rebase'
alias gra='git remote add'
alias grr='git remote rm'
alias gpu='git pull --rebase'
alias gcl='git clone'
alias c='cd'
alias v='vim'
alias r='rm'
alias g='grep'
alias t='tail'
alias h='head'
alias w='wc -l'

# directories
function gh { cd ~/GitHub ; }
function cidigit { cd ~/CidiGit ; }
function qproc { ps aux | grep "$1" ; }

# apollo
function startd { bash scripts/bootstrap.sh ; }
function stopd { bash scripts/bootstrap.sh stop ; }
function bab { bash apollo.sh build ; }

function tplan { tail -f data/log/planning.INFO | grep "$1"; }

