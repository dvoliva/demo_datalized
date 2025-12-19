import pandas as pd
import glob
import os
import config

def load_data():
    search_path = os.path.join(config.RAW_DATA_DIR, '*.csv')
    file_list = glob.glob(search_path)
    data_frames = []

    for file_path in file_list:
        try:
            current_df = pd.read_csv(
                file_path,
                sep=';',
                usecols=config.REQUIRED_COLUMNS,
                encoding='latin1',
                dtype={'MRUN': str, 'CAT_PERIODO': str}
            )

            filtered_df = current_df[current_df['CAT_PERIODO'] >= config.MIN_YEAR]

            if not filtered_df.empty:
                data_frames.append(filtered_df)
                print('archivo cargado: ' + os.path.basename(file_path))
        except Exception as e:
            print('error en la carga ' + file_path + ': ' + str(e))
    
    if not data_frames:
        return pd.DataFrame()

    return pd.concat(data_frames, ignore_index=True)