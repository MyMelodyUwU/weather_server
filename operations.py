#!/usr/bin/env python3

import sys
import random

temp_list = []
def operation_average(values):
	for i in values:
		temp_list.append(int(i))
	return sum(temp_list) / len(temp_list)