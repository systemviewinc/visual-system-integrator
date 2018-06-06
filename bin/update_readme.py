#!/usr/bin/env python3

import requests

JENKINS_URL = 'http://systemview.ddns.net:8080'
JENKINS_API = '/api/json?tree=jobs[name,jobs[name]]'

JOBS_TO_MONITOR=['build', 'integration']

response = requests.get(JENKINS_URL + JENKINS_API).json()

print('### Status')

for jobs in response['jobs']:
    if (jobs['name'] in JOBS_TO_MONITOR):
        folder_name = jobs['name']
        print('\n#### {}'.format(folder_name.title()))
        for job in jobs['jobs']:
            job_name = job['name']
            print('\n{}: [![Build Status]({}/buildStatus/icon?job={}/{})]({}/job/{}/{})'.format(job_name.replace('_', ' ').title(), JENKINS_URL, folder_name, job_name, JENKINS_URL, folder_name, job_name))


# #### Build
# VSI: [![Build Status](http://systemview.ddns.net:8080/buildStatus/icon?job=build/vsi)](http://systemview.ddns.net:8080/job/build/vsi)
#
# #### Integration
# CPP API: [![Build Status](http://systemview.ddns.net:8080/buildStatus/icon?job=integration/cxx_api)](http://systemview.ddns.net:8080/job/integration/cxx_api)
#
# CPP API: [![Build Status](http://systemview.ddns.net:8080/buildStatus/icon?job=integration/cxx_api)](http://systemview.ddns.net:8080/job/integration/cxx_api)
