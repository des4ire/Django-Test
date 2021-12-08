#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 21:05:34 2021

@author: dev
"""

import csv

from .models import Visit


def read_and_decode_csv(csv_file, encoding='utf-8'):

    decoded_file = csv_file.read().decode(encoding).splitlines()
    return decoded_file


def create_visit_from_csv_row(csv_row):

    visit = Visit(
        visitor=csv_row['visitor'],
        reason=csv_row['reason'],
        date_time=csv_row['date_time'],
        email=csv_row['email'],
    )

    visit.save()


def visit_csv_rows_to_db(decoded_csv_file):

    csv_reader = csv.DictReader(decoded_csv_file)

    for row in csv_reader:
        create_visit_from_csv_row(row)