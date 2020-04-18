@echo off
rmdir /s /q build dist lock.egg-info
python setup.py sdist bdist_wheel