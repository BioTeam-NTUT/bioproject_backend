#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: schemas.py
    Author: guyleaf
    Contact: ychhua1@gmail.com
    Time: 2021/8/8 5:46 PM
"""
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class LEVoting(BaseModel):
    threshold: int = Field(ge=1, le=6, description="The threshold of votes")
    minLength: int = Field(ge=1, description="The minimum length of residues")


class FormArgs(BaseModel):
    data: str = Field(
        min_length=1,
        max_length=2000,
        description="Fasta, Bare Sequence, NCBI gi/UniProt ID are acceptable",  # noqa: E501
    )
    email: Optional[EmailStr] = Field(None, description="Email address")
    makeTaxonomy: bool = Field(description="Make taxonomy tree")
    leVote: LEVoting = Field(description="Linear Epitope Voting System parameters")
    hostId: str = Field(description="Host target ID for analysis")


class Host(BaseModel):
    id: str
    name: str


class SimpleResponse(BaseModel):
    code: int = Field(200, title="HTTP Status Code")
    msg: str = Field(title="Message")
