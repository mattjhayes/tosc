#!/usr/bin/python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
tosc - Time Operating System Command

Simple script that runs an OS command and writes the start and
end times to files, so that they can be used as measurements in
experiments.

Pass it three parameters:
    1) The directory/filename to write the start timestamp to
    2) The command to run
    3) The directory/filename to write the end timestamp to

Example:
./tosc.py /tmp/start.txt 'ls -la' /tmp/end.txt

$ cat /tmp/start.txt
1460623489.084451170
$ cat /tmp/end.txt
1460623489.152492636

"""

import os, sys

#*** Must have 3 parameters passed to it (first parameter is script)
assert len(sys.argv) == 4

#*** Get parameters from command line
FILENAME_START_TIMESTAMP = sys.argv[1]
OS_COMMAND = sys.argv[2]
FILENAME_END_TIMESTAMP = sys.argv[3]

#*** Build calls:
TIMESTAMP_START_CALL = "date +%s.%N > " + FILENAME_START_TIMESTAMP
TIMESTAMP_END_CALL = "date +%s.%N > " + FILENAME_END_TIMESTAMP

#*** Write start timestamp to file:
os.system(TIMESTAMP_START_CALL)

#*** Run OS command:
os.system(OS_COMMAND)

#*** Write end timestamp to file:
os.system(TIMESTAMP_END_CALL)


