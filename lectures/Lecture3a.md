# Lecture 3a:  A few comments after Lecture3 :

- miniconda install peculiarities:

  - the installation directory cannot be moved to a new location (even
    if you edit the new $PATH location). The reason is the **#!** line
    in many scripts are hardcoded (and we also found some conda issues)

  - The installation of miniconda (or anaconda) cannot handle a space
    in the directory name. The solution we came up with was a symbolic
    link. For example, if we have a user "Peter 1" on a Mac, we fix this
    as follows:
```
    cd  /Users
    sudo ln -s "Peter 1"  Peter_1
    cd Peter_1
    bash Miniconda....
```

- The ubuntu "*add account*" System Settings method does not allow the Username to contain spaces.
The **adduser** command has similar restrictions, so the following command would fail:
```
	sudo adduser "space man"
```
    
- ursa accounts are using **/bin/tcsh** as login shell, not
  **/bin/bash**, which is commonly the default on most Unix (Mac too) systems.
  This means you should add your modified command
  search path in the .cshrc file:

```
	setenv PATH  $HOME/miniconda3:$PATH
```
instead of the bash variant
```
	export PATH=$HOME/miniconda3:$PATH
```
and aliases are added without the **=** sign. For example:
```
	alias i ipython
	alias j "jupyter notebook"
	alias dth "ls -lt | head"
```
instead of the bash variant
```
	alias i=ipython
	alias j="jupyter notebook"
	alias dth="ls -lt | head"
```	
