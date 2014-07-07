# -*- coding: utf-8 -*-

# Copyright 2014 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


def write_config(filename, data):
    with open(filename, "w") as f:
        f.write(str(data))


def get_file_data(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except IOError:
        return ""


def diff(filename, data):
    return not get_file_data(filename) == data
