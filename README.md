# Automated Stock Update

> A personalized Python process that sends an email to you daily at a specified time giving updates on stocks you would like to follow.

## Author

> By **Sarah Marion**

> -----------------------------------------------------------

## Description

> Created a personalized Python process that sends an email to you daily at a specified time giving updates on stocks that a user would like to follow utilizing the IEX stock exchange API.

## User Stories

As a user I would like:

> * to retrieve stock symbols & stock name.
> * to exchange stock.
> * to view links to the latest article found that mentions your stocks.
> * to build an email template based off the information recieved and send to yourself.

## Technologies Used

> * Python3.6
> * Python libraries
> * Google Client Library

## Setup/Installation Requirements

### Prerequisites

> * Internet access
> * Gmail account
> * Text Editor (vscode) N?B any would do
> * Amazon AWS account
> * IEX API
> * ```git clone https://github.com/sarah-marion/Automated_Stock_Update.git```
> * ```cd Automated_Stock_Update```

#### To install a virtual environment

> * ```python3.6 -m venv virtual``` 
> * ```source virtual/bin/activate```

#### To install all dependencies

> * ```python3.6 -m pip install -r requirements.txt```

## Dependancy Installments

> * ```pip3 install python3.6```
> * ```pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib```

### Installing Python Libraries needed

> * ```pip3 install datetime requests jinja2```

## Running the application

> Configure gmail.py email settings to your preference

> Configure symbols in app.py for the stocks you want to receive.

> run ```python3 app.py`` to get the application running and send the email to your desired destination

> ```python3 quickstart.py``` to check your email configurations via the terminal

## Known Bugs

> It does not have bugs.But if any problems should occur, email me at devsarahmarion@gmail.com

> * N/B Also it is not finished yet...more features and functionalities are still being worked on for it to be utilized in a Windows task scheduler.

## Support and Contact Details

> You can reach out to me at devsarahmarion@gmail.com
for Reviews, Advice, Collaborations and Comments

## Licence

> MIT License

> Copyright (c) 2018 **Dev Sarah Marion**

> Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

> The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

> --------------------------------------------------------
