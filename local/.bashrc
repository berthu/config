# SSH addresses
alias bear="ssh albert_hu@research.haas.berkeley.edu"
alias wrds="ssh alberthu@wrds-cloud.wharton.upenn.edu"

# search file for all TODO tags
function todo { more "$1" | grep --color=always "TODO"; }

# Directory helpers
alias size_dir='du -cksh *'
function findf { grep -Ril "$1" $2; }
export -f findf

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