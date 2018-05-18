#!/bin/bash
# SSH addresses
source ~/.network_aliases

# search file for all TODO tags
function todo { more "$1" | grep --color=always "TODO"; }

# Directory helpers
alias size_dir='du -cksh *'
function findf { grep -Ril "$1" $2; }
export -f findf
function n { nautilus $1; }

# populate directory with common files
function fmake {
    if [ $1 == "latexbase" ];
        then
        cp ~/Dropbox/latexbase/alhulatex.tex .
        cp ~/Dropbox/latexbase/docbase.tex .
        fi
    if [ $1 == "testdirs" ];
        then
        mkdir testing
        cd testing
        mkdir errors logs _pre post
        fi
}

# zip directory, $1 = x.zip, $2 is directory
function zdir { zip -r $1 $2; }

# applications
function tempftp { python -m pyftpdlib -w; }
function ml { /usr/local/MATLAB/R2018a/bin/matlab; }
function mlgl { /usr/local/MATLAB/R2018a/bin/matlab -softwareopengl; }
function shadowsocks { sslocal -s ~/shadowsocks.json; }

# directories
function gh { cd ~/GitHub ; }
function cidigit { cd ~/CidiGit ; }
function qproc { ps aux | grep "$1" ; }

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

function depbert() { cp bert_apollo_aliases.sh /apollo/ ; }
