#!/usr/bin/env python3

from urllib.request import urlopen
import json

JENKINS_URL = 'http://systemview.ddns.net:8080/api/json?tree=jobs[name,jobs[name]]'

with urlopen(JENKINS_URL) as response:
    print(dir(response))
    res = json.load(response.read())
    print(res)

# ### Status
#
# #### Build
# VSI: [![Build Status](http://systemview.ddns.net:8080/buildStatus/icon?job=build/vsi)](http://systemview.ddns.net:8080/job/build/vsi)
#
# #### Integration
# CPP API: [![Build Status](http://systemview.ddns.net:8080/buildStatus/icon?job=integration/cxx_api)](http://systemview.ddns.net:8080/job/integration/cxx_api)
#
# CPP API: [![Build Status](http://systemview.ddns.net:8080/buildStatus/icon?job=integration/cxx_api)](http://systemview.ddns.net:8080/job/integration/cxx_api)
