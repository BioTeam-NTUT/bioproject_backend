#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: schemas.py
    Author: guyleaf
    Contact: ychhua1@gmail.com
    Time: 2021/8/8 5:46 PM
"""
import re
from enum import Enum
from typing import Any, Dict, Optional

from pydantic import BaseModel, EmailStr, Field, validator

from app.helpers import (
    is_accession_format,
    is_fasta_format,
    is_protein_sequence_format,
)


class LEVoting(BaseModel):
    threshold: int = Field(ge=1, le=6, description="The threshold of votes")
    minLength: int = Field(ge=1, description="The minimum length of residues")


class DataType(str, Enum):
    sequence = "sequence"
    fasta = "fasta"
    accession = "accession"


class FormArgs(BaseModel):
    type: DataType = Field(description="The type of the data")
    data: str = Field(
        min_length=1,
        max_length=2000,
        description="Fasta, Bare Sequence, GenBank/UniProt accession are acceptable",  # noqa: E501
    )
    email: Optional[EmailStr] = Field(None, description="Email address")
    makeTaxonomy: bool = Field(description="Make taxonomy tree")
    leVote: LEVoting = Field(
        description="Linear Epitope Voting System parameters"
    )
    hostTaxonId: str = Field(description="Host taxonomy ID for analysis")

    @validator("data")
    def check_data_format(cls, v: str, values: Dict[str, Any]) -> None:
        data_type: DataType = DataType(values.get("type"))
        if data_type is DataType.fasta and not is_fasta_format(v):
            raise ValueError("Incorrect fasta format.")
        elif data_type is DataType.sequence and not is_protein_sequence_format(
            v
        ):
            raise ValueError("Incorrect bare protein sequence format.")
        elif data_type is DataType.accession and not is_accession_format(v):
            raise ValueError("Incorrect accession number format.")

    @validator("hostTaxonId")
    def check_taxonomy_id_format(cls, v: str) -> str:
        if re.fullmatch(r"^[A-Za-z0-9]+$", v) is None:
            raise ValueError("Incorrect taxonomy ID format.")
        return v

    class Config:
        schema_extra = {
            "example": {
                "type": "sequence",
                "data": "vngglipeae",
                "makeTaxonomy": True,
                "leVote": {"threshold": 3, "minLength": 1},
                "hostTaxonId": "163117",
            }
        }


class SimpleResponse(BaseModel):
    code: int = Field(200, title="HTTP Status Code")
    message: str = Field(title="Message")
