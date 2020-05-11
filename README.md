# battery-calc

Copyright 2020 Muhammad Mansoor

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Description

Homework Assignment for Open Source Energy Modelling Course

### Getting Started

This repository contains two Python coding files: batteryfunctions.py and test_batteryfunctions.py

The batteryfunctions.py file contains three different functions to perform basic calculations of Battery Energy Storage equipped with Solar PV module and feeding energy to electric load. The test_batteryfunctions.py file contains unit tests for each of the functions written in batteryfunctions.py file

The char_batt() function calculates the charging input energy to the battery when PV output is greater than the electric load, the dischar_batt() function claculates the discharging output from the battery when the PV output is lower than the electric load and the battery_SOC() function claculates the updated State-of-Charge (SOC) of the battery from the charging input, discharging output, previous SOC and the losses. The battery capcaity has been fixed for the simplicity and the losses are assumed to be 5% of the capacity.

### Running the tests

The tests are executed on travis-ci. The tests are written in **pytest** testing configuration. There are no additional dependencies/packages needed to run the tests
