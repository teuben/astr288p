Lecture 11: PDE's and ODE's
===========================

## Homeworks

**Homework-02** is available, **Homework-03** is available as draft.

## Jupyter 5.0

A new and improved version of jupyter has come out:

http://blog.jupyter.org/2017/04/04/jupyter-notebook-5-0/

to install use any of the following methods:

```
pip install --upgrade notebook 
conda upgrade notebook 
```

**however** ... this could break your miniconda, and/or make new notebooks not readable by previous versions of jupyter.
How can we test this before sacrifice all our precious work?  This happened to me on my old miniconda2 tree, so this is
not always a safe way to experiment with the bleeding edge.

```
   # make a backup
   cd $HOME
   tar cf miniconda3.tar miniconda3
or
   zip -r miniconda3.zip  miniconda3
or
   7z a  miniconda3.7z  miniconda3

   # now experiment
   conda upgrade notebook 

   # conda:    4.3.14-py35_0 --> 4.3.16-py35_0
   # notebook: 4.2.3-py35_0  --> 5.0.0-py35_0 
```

If this worked (as it did for me), fine. If not, restore the backup;
```
  cd $HOME
  tar xf miniconda3.tar
or
  unzip miniconda3.zip
or
  7z x miniconda3.7z

```

Remember from earlier experiments: you cannot move the miniconda3 tree to another location and just adjust the $PATH, as
at the original install time the python path for things such as pip to work are hardcoded!!


## notebooks:


* **athena-01** : PDE's  

* **orbits-01** : ODE's - after **In[12]** - Q3:
  what if the potential is not axisymmetric?  Did we design the data structure right to compare integration methods?
  

