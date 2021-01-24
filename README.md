# PureHealth COVID-19 PCR test results checker
This is a simple and dull Python3 tool to automatically check COVID-19 PCR test results conducted by [PureHealth](http://purehealth.ae/).


## Build & run & example
Python3 is required to run the tool.

Install `urllib3` and `requests` are also required. Install them like this:
```shell script
pip3 install -r requirements.txt
```

Example run:
```shell script
./purechecker.py 001234567 2001-01-25
```

See help for details:
```shell script
./purechecker.py --help
```


## Motivation
All tourists coming to **United Arab Emirates** are required to pass a COVID-19 PCR test. As of January 2021, tests are conducted by PureHealth, and their results should be checked manually at https://icrs.purehealth.ae/results/.

Until the negative test result is confirmed, travellers are required to quarantine. Obviously, [I](https://github.com/leskin-in) and my [friend](https://github.com/vladislav27) want to know the results ASAP to have fun and enjoy the holiday.

However, the form at https://icrs.purehealth.ae/results/ requires the users to re-enter passport number and birth date each time, and this is especially inconvenient on mobile devices.


## Implementation description
The tool issues a `GET` request periodically (each `30` seconds by default) and checks the response. When the response differs from "result is not known", it is printed, and a notification to OS is sent (via `notify-send`, which works on Ubuntu).



