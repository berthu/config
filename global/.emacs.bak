;; background color
(add-to-list 'default-frame-alist '(foreground-color . "#00FF00"))
(add-to-list 'default-frame-alist '(background-color . "#171717"))

;; package manager
(require 'package)
(add-to-list 'package-archives '("melpa" . "http://melpa.org/packages/"))
(package-initialize)
;; Run M-x package-install RET markdown-mode RET

;; markdown preview
(add-to-list 'auto-mode-alist '("README\\.md\\'" . gfm-mode))
(setq markdown-command "pandoc -c ~/.emacs.d/github-pandoc.css --from markdown_github -t html5 --mathjax --highlight-style pygments --standalone")

