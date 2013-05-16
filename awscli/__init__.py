# Copyright 2012-2013 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
"""
AWSCLI
----
A Universal Command Line Environment for Amazon Web Services.
"""
import os

__version__ = '0.10.1'

#
# Get our data path to be added to botocore's search path
#
p = os.path.split(__file__)[0]
p = os.path.split(p)[0]
awscli_data_path = [os.path.join(p, 'awscli/data')]
if 'AWS_DATA_PATH' in os.environ:
    for path in os.environ['AWS_DATA_PATH'].split(':'):
        path = os.path.expandvars(path)
        path = os.path.expanduser(path)
        awscli_data_path.append(path)
os.environ['AWS_DATA_PATH'] = ':'.join(awscli_data_path)


EnvironmentVariables = {
    'profile': (None, 'AWS_DEFAULT_PROFILE', None),
    'region': ('region', 'AWS_DEFAULT_REGION', None),
    'data_path': ('data_path', 'AWS_DATA_PATH', None),
    'output': ('output', 'AWS_DEFAULT_OUTPUT', 'json'),
    }
