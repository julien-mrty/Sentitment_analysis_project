import pandas as pd


def load_data(file_path):
    df = pd.read_csv(file_path)

    sentiments_list = df.iloc[:, 2].tolist()
    messages_list = df.iloc[:, 3].tolist()

    return sentiments_list, messages_list


def pre_process_phrases(messages_list):
    messages_list_unicode = [str(phrase) for phrase in messages_list]

    return messages_list_unicode