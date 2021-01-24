#!/usr/bin/env python3

import requests
import json
import argparse
import time
import datetime
import urllib3
import subprocess


# PureHealth uses non-verifiable SSL certificate for APIs
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def pure_request(passport_number: str, birth_date: str):
    """
    Request PureHealth backend. They use pure GET request for this. The original
    frontend also sets a header
    \p birth_date: Must be in format 'YYYY-MM-DD'
    """
    params = {
        'passportNumber': passport_number,
        'dob': birth_date,
        'testCode': 'COVID19PCR'
    }
    result_req = requests.get('https://pureprod.purehealth.ae/cvdpdfrpt/api/PDFResults/getPatResult', params=params, verify=False)
    result_raw = result_req.text
    result = json.loads(result_raw)
    if result['Status'] == 'Error Result API: Patient does not have authorized result':
        print(datetime.datetime.now(), 'Not ready yet :-(')
        return False
    else:
        print(datetime.datetime.now(), result, sep='\n')
        return True

def main():
    parser = argparse.ArgumentParser(description='A simple "PureHealth COVID PCR test" results checker')
    parser.add_argument('passport_number', help='passport number')
    parser.add_argument('birth_date', help='date of birth, in YYYY-MM-DD format')
    parser.add_argument('-i', help='interval between requests (seconds)', type=int, default=30)
    args = parser.parse_args()
    
    subprocess.Popen(['notify-send', 'Tracking PureHealth COVID test results...'])

    while True:
        if (pure_request(args.passport_number, args.birth_date)):
            subprocess.Popen(['notify-send', 'PureHealth COVID test results ready!'])
            return
        try:
            time.sleep(args.i)
        except KeyboardInterrupt:
            print()
            return

if __name__ == '__main__':
    main()
