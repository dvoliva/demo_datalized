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
                encoding='utf-8',
                dtype={'mrun': str, 'cat_periodo': int}
            )

            filtered_df = current_df[current_df['cat_periodo'] >= config.MIN_YEAR]

            if not filtered_df.empty:
                data_frames.append(filtered_df)
                print('archivo cargado: ' + os.path.basename(file_path))
        except Exception as e:
            print('error en la carga ' + file_path + ': ' + str(e))
    
    if not data_frames:
        return pd.DataFrame()

    return pd.concat(data_frames, ignore_index=True)

if __name__ == "__main__":
    df_test = load_data()
    
    if not df_test.empty:
        print(df_test.head())
    else:
        print("error")