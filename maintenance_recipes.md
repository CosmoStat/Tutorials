# Recipes for maintenance tasks on this repo

This file serves as a collection of git magic recipes that were used to build
this repo.

## Hosting a new tutorial website on github pages

Only the master/docs folder is served on gh-pages, so we use submodules to link
to docs that can be hosted on other branches.

Here is an example of how we did it for the tensorflow tutorial using submodules:

```
$ git checkout master
$ cd docs
$ git submodule add -b tensorflow-tutorial  https://github.com/CosmoStat/Tutorials.git tensorflow-introduction
```
