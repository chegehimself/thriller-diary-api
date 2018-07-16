# thriller-diary-api

An online journal where users can pen down their thoughts and feelings. This is the implementation of the Restful API.

# Status
__Badge-build badge-coverage badge-codacy__

__Live version: [comming soon ...]()__

### Local Installation

Fork this repository to your github account and clone from there(_NB: clone from your github account - after forking_).This will help you to contribute to this project.

[Create a python Virtual environment and Activate it](https://virtualenv.pypa.io/en/stable/).A virtual environment is effective when working on multiple projects. Each project will have its own development enviroment.

__Install Dependencies__(_Note: This should be done in the created virtual environment_)
```
$ pip install -r requirements.txt
```
__Set environment variable__
```
$ export APP_SETTINGS="development"
```

__Start Server__
```
python run.py
```

[__Use postman app to send request to app.__](https://www.getpostman.com/)
### Endpoints

The following is a list of available endpoints in this application

|EndPoint | Functionality|
| ------------ | ------------ |
|GET api/v1/entries |Fetch all entries|
|PUT api/v1/entries/<entryId> |Fetch a single entry|
|POST api/v1/entries|Create an entry|
|GET api/v1/entries/<entryId> |Modify an entry|

# Testing
- comming soon...

### Contributing
Create A Pull request to develop branch

### Authors
* [James Chege](https://www.github.com/james-chege)

### License

This app is licensed under MIT [LICENSE](LICENSE)
