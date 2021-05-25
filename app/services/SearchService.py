#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: SearchService.py
    Author: guyleaf
    Contact: ychhua1@gmail.com
    Time: 2021/5/11 11:20 AM
"""
from flask import current_app
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import Entrez
from ratelimit import limits, sleep_and_retry
from typing import Union, Optional
import urllib.parse
import urllib.request

UNIPROT_ID_MAP = ["EMBL", "P_GI"]


class SearchService:
    @staticmethod
    def get_info_from_uniprot_by_id(seq_id: str) -> Optional[SeqRecord]:
        print(UNIPROT_ID_MAP)
        return

    @staticmethod
    def get_info_from_uniprot_by_seq(seq: Union[Seq, str]) -> Optional[SeqRecord]:
        print(seq)
        return

    @staticmethod
    @sleep_and_retry
    @limits(calls=2, period=1)
    def get_info_from_ncbi_by_id(seq_id: str) -> Optional[SeqRecord]:
        with current_app.app_context():
            Entrez.email = current_app.config.EMAIL_ADDRESS
        handle = Entrez.efetch(db="protein", id=seq_id, rettype="gp", retmode="text")
        return

    @staticmethod
    @sleep_and_retry
    @limits(calls=2, period=1)
    def get_info_from_ncbi_by_seq(seq: Union[Seq, str]) -> Optional[SeqRecord]:
        print(seq)
        return
