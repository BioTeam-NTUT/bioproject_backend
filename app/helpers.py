#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: helpers.py
    Author: guyleaf
    Contact: ychhua1@gmail.com
    Time: 2021/5/25 8:27 PM
"""
import re

UNIPROT_ACCESSION_NUMBER_FORMAT = r"[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2}"
GENBANK_ACCESSION_NUMBER_FORMAT = r"[A-Z]{3}([0-9]{5}|[0-9]{7})"


def is_uniProt_accession_number(accession: str) -> bool:
    return re.fullmatch(UNIPROT_ACCESSION_NUMBER_FORMAT, accession.upper()) is not None


def is_genBank_accession_number(accession: str) -> bool:
    return re.fullmatch(GENBANK_ACCESSION_NUMBER_FORMAT, accession.upper()) is not None


if __name__ == "__main__":
    print(is_uniProt_accession_number("P01013"))
    print(is_genBank_accession_number("ATE90961"))
