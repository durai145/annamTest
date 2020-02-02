#sudo apt-get install pipenv -y
pipenv install requests
pip install pyyaml
PYTHONPATH=$PYTHONPATH:$PWD/lib/
sudo ln -fs lib/* /usr/local/lib/python2.7/site-packages/

