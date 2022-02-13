import re

UNIPROT_ACCESSION_NUMBER_FORMAT = r"^([A-N,R-Z][0-9]([A-Z][A-Z,0-9][A-Z,0-9][0-9]){1,2})|([O,P,Q][0-9][A-Z,0-9][A-Z,0-9][A-Z,0-9][0-9])(\.\d+)?$"  # noqa: E501
GENBANK_ACCESSION_NUMBER_FORMAT = r"^([A-Za-z0-9]+\d+(\.\d+)?)|((N|X|W|A)P_\d+)$"


def is_fasta_format(v: str) -> bool:
    return v.startswith(">") and len(v.split("\n", 1)) > 1


def is_protein_sequence_format(v: str) -> bool:
    return re.fullmatch(r"^[A-Za-z]+$", v) is not None


def is_accession_format(v: str) -> bool:
    return (
        re.fullmatch(GENBANK_ACCESSION_NUMBER_FORMAT, v) is not None
        or re.fullmatch(UNIPROT_ACCESSION_NUMBER_FORMAT, v) is not None
    )
