import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DATA_DIR = os.path.join(BASE_DIR, 'data', 'raw')
PROCESSED_DATA_DIR = os.path.join(BASE_DIR, 'data', 'processed')

OUTPUT_FILENAME = 'output.csv'

REQUIRED_COLUMNS = [
    'cat_periodo',
    'mrun',
    'gen_alu',
    'rango_edad',
    'tipo_inst_1',
    'modalidad',
    'jornada'
]

GENDER_MAP = {
    1: 'Masculino',
    2: 'Femenino'
}

MIN_YEAR = 2019
