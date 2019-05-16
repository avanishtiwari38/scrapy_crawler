## Installation

1.Create a python 3 environment. All the dependencies of a project should be ported in a Venv

    virtualenv -p python3 envname

2.Switch to that environment 

    source path-to-env/envname/bin/activate

3.Install requirements from `requirements.txt`.

    pip install -r requirments.txt

4.Run your spider by using command below.

    scrapy crawl angular -o angular.json

    scrapy crawl gitdoc -o gitdoc.json
