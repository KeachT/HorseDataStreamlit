import pandas as pd
import time
from tqdm import tqdm

def scrape(horse_id_list):
    #horse_idをkeyにしてDataFrame型を格納
    horse_results = {}
    for horse_id in tqdm(horse_id_list):
        time.sleep(1)
        try:
            url = 'https://db.netkeiba.com/horse/' + horse_id
            df = pd.read_html(url)[3]
            #受賞歴がある馬の場合、3番目に受賞歴テーブルが来るため、4番目のデータを取得する
            if df.columns[0]=='受賞歴':
                df = pd.read_html(url)[4]
            df.index = [horse_id] * len(df)
            horse_results[horse_id] = df
        except IndexError:
            continue
        except Exception as e:
            print(e)
            break
        except:
            break

    #pd.DataFrame型にして一つのデータにまとめる
    horse_results_df = pd.concat([horse_results[key] for key in horse_results])
    return horse_results_df
