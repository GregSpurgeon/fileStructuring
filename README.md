# Folder Structuring

## Description
This application is all about structuing your files into a tree format for easier navigation of your files.

## Packages to Install 
Use package manager pipenv to install django-mptt

```bash
    pipenv install django-mptt
```

## Usage
Use the Django admin panel to create different instances of the Folder model in hierarchy_system.models.py

Your top level folders will not have a parent node(leave blank) but if you want to make subfolders, make the parent of your subfolder whichever folder you want this subfolder to live in.



