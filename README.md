# BachService
Microservice for getting BWV Entries.

The Service returns json Data for a given BWV Number or parts of a title (works only)

The Service exposes two REST Endpoints:
- /works
- /chorales

## Examples
- GET Requests to the /works endpoint can be queried with a ```titel``` and/or a ```bwv``` URL-parameter. E.g.: http://somehost:8005/bwv-service/works?bwv=10&titel=Meine

- The /chorales endpoint takes only a ```bwv``` parameter: http://somehost:8005/bwv-service/works?bwv=10

## Requirements
The service is based on flask and sqlalchemy. It uses a sqlite database.

## Installation
- Create a python environment (python 3.10 recommended)
- Install the requirements with: ```pip install requirements.txt```
- For local testing run: ```python run.py```