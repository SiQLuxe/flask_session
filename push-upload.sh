git add .
git commit -m "udpate setup"
git push origin master
git tag -d 0.3.0
git tag 0.3.0 -m "put on PyPI"
git push origin :0.3.0
git push --tags origin master

# http://akagi201.org/blog/how-to-submit-package-to-pypi/
