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
                dtype={'mrun': str}
            )

            data_frames.append(current_df)
            print(f'archivo: {os.path.basename(file_path)} | filas: {len(data_frames)}')
        
        except Exception as e:
            print(f'error en {os.path.basename(file_path)}: {e}')
    
    if not data_frames:
        return pd.DataFrame()
    
    return pd.concat(data_frames, ignore_index=True)

def transform_data(df_input):
    df = df_input.copy()

    df = df[~df['anio_ing_carr_act'].isin(config.INVALID_ADMISSION_YEARS)]

    text_cols = ['tipo_inst_1', 'modalidad', 'jornada', 'rango_edad']
    for col in text_cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.title().str.strip()

    is_not_presential = ~df['modalidad'].str.contains('Presencial', case=False, na=False)
    is_vesp = df['jornada'].str.contains('Vespertino|A Distancia', case=False, na=False)

    df['segmento'] = 'Tradicional'

    df.loc[is_not_presential | is_vesp, 'segmento'] = 'Flexible'

    df['gen_alu'] = df['gen_alu'].map(config.GENDER_MAP)

    return df


if __name__ == "__main__":
    df_test = load_data()
    df_mrun = df_test["mrun"].nunique()
    print(f'Unique cat_periodo values: {df_mrun}')
    if not df_test.empty:
        print(df_test.head())
    else:
        print("error")
