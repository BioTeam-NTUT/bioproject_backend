import re

UNIPROT_ACCESSION_NUMBER_FORMAT = r"[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2}"  # noqa: E501
GENBANK_ACCESSION_NUMBER_FORMAT = r"[A-Z]{3}([0-9]{5}|[0-9]{7})"


def is_fasta_format(v: str) -> bool:
    return v.startswith(">") and len(v.split("\n", 1)) > 1


def is_protein_sequence_format(v: str) -> bool:
    return re.fullmatch(r"^[A-Za-z]+$", v) is not None


def is_accession_format(v: str) -> bool:
    return (
        re.fullmatch(GENBANK_ACCESSION_NUMBER_FORMAT, v.upper()) is not None
        or re.fullmatch(UNIPROT_ACCESSION_NUMBER_FORMAT, v.upper()) is not None
    )
