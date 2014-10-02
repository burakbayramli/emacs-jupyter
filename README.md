## DESCRIPTION

emacs-ipython connects to an inprocess ipython kernel, executes
notebook code, and displays the results automatically in a LaTeX
buffer. You could easily modify it to work in a text buffer, or a
markdown buffer.

## INSTALL

First install Pymacs - https://github.com/pinard/Pymacs. Build, install.

Install preview-latex for Emacs.

Then in your .emacs, do

```
(pymacs-load "[PYTEXIPY DIR]/pytexipy-notebook")
(global-set-key [f1] 'pytexipy-notebook-run-py-code); or choose any key you like
(global-set-key [f5] 'pytexipy-notebook-complete-py); or choose any key you like
(global-set-key [f11] 'reload-pymacs)
```

For minted-TeX integration, add this to your custom-set-variables

```
'(preview-LaTeX-command (quote ("%`%l -shell-escape \"\\nonstopmode\\nofiles\\PassOptionsToPackage{"
("," . preview-required-option-list) "}{preview}\\AtBeginDocument{\\ifx\\ifPreview\\undefined"
 preview-default-preamble "\\fi}\"%' %t")))
 ```

 If you are planning to plot things in your buffer, dont forget to
 include graphics with `\usepackage{graphicx}`. 


## FEATURES

* When you are in `\begin{minted}` and `\end{minted}` blocks, call
`'pytexipy-notebook-run-py-code`, and all code in that block will be
sent to a ipython kernel and the result will be displayed
underneath. If on `\inputminted{python}{file.py}` block, code will be
loaded from script filename between the curly braces. Results will be
placed in `\begin{verbatim}`, `\end{verbatim}` blocks right next to
the code, with one space in between. If a verbatim blocks already
exists there, it will be refreshed. If not, it will be added.

* If `plt.show()` is detected in code block, all previous code in
buffer will be scanned for `plt.savefig(..)` commands. Say there were
5 of them, in this case `show()` will be replaced with
`plt.savefig('[file]_6.png')`, an `\includegraphics` LaTeX command
will be added and a call to preview-latex will be made to refresh
buffer, so the figure is immediately shown underneath just like in an
ipython notebook!

* After entering any expression, if you call
`'pytexipy-notebook-complete-py`, emacs-ipython will show a list of
possible completions in a `*pytexipy*` buffer. This list comes
directly from ipython, hence it reflects the cumulation of runtime
code that has been executed and brought into memory thusfar through
multiple `'pytexipy-notebook-run-py-code` calls. 

## LIMITATIONS

* For now, there is one kernel per Emacs session.

* At the start, I have to hit f11 or `'reload-pymacs` to force
  initialization. I did not yet hook this up to a buffer load. However
  this command is useful for other purposes, such as wanting to clean
  up ipyton memory and starting from scratch, anytime. 

![](emacs-ipython.png)
