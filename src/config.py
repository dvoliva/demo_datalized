import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DATA_DIR = os.path.join(BASE_DIR, 'data', 'raw')
PROCESSED_DATA_DIR = os.path.join(BASE_DIR, 'data', 'processed')

OUTPUT_FILENAME = 'output.csv'

REQUIRED_COLUMNS = [
    'CAT_PERIODO',
    'MRUN',
    'GEN_ALU',
    'RANGO_EDAD',
    'TIPO_INST_1',
    'MODALIDAD',
    'JORNADA'
]

GENDER_MAP = {
    1: 'Male',
    2: 'Female'
}

MIN_YEAR = 2019
