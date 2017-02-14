# Lecture 3a:  A few comments after Lecture3 :

- miniconda install peculiarities:

  - the installation directory cannot be moved to a new location (even
    if you edit the new $PATH location). The reason is the **#!** line
    in many scripts are hardcoded (and potentially more)

  - The installation of miniconda (or anaconda) cannot handle a space
    in the directory name. The solution we came up with was a symbolic
    link. For example:

```
    cd  /Users
    sudo ln -s "Peter 1"  Peter_1
    cd Peter_1
    bash Miniconda....
```

- ursa account are using /bin/tcsh as login shell, not /bin/bash.  This means you should add your modified path in the .cshrc file:

```
	setenv PATH  $HOME/miniconda3:$PATH
```
