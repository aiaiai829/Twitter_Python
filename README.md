Twitter API Usage:

1. Getting Twitter API keys
To start with, you will need to have a Twitter account and obtain credentials (i.e. API key, API secret, Access
token and Access token secret) on the Twitter developer site to access the Twitter API, following these steps:
Create a Twitter user account if you do not already have one.
Go to https://apps.twitter.com/ (https://apps.twitter.com/) and log in with your Twitter user account. This
step gives you a Twitter dev account under the same name as your user account.
Click "Create New App"
Fill out the form, agree to the terms, and click "Create your Twitter application"
In the next page, click on "Keys and Access Tokens" tab, and copy your "API key" and "API secret".
Scroll down and click "Create my access token", and copy your "Access token" and "Access token
secret".

2. Installing a Twitter library
We will be using a Python library called Python Twitter Tools (https://pypi.python.org/pypi/twitter) to connect to
Twitter API and downloading the data from Twitter. There are many other libraries
(https://dev.twitter.com/overview/api/twitter-libraries>) in various programming languages that let you use
Twitter API. We choose the Python Twitter Tools for this tutorial, because it is simple to use yet fully supports
the Twitter API.
Download the Python Twitter tools at https://pypi.python.org/pypi/twitter (https://pypi.python.org/pypi/twitter).
Install the Python Twitter Tools package by typing in commands:
$ python setup.py --help
$ python setup.py build     
$ python setup.py install

3. Run the program