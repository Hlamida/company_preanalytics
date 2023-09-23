import os
import pickle

import numpy as np
from tensorflow.keras.models import load_model

from inn_analitic.settings import BASE_DIR


def local_model_predict(year, base_okved, nalog, okfs, okopf, smsp):
    loaded_model = load_model(
        os.path.join(
            BASE_DIR,
            'ai_models/h5/simple/simple_model-0.92.h5',
        )
    )

    with open(
        os.path.join(
            BASE_DIR,
            'ai_models/tokenizer.pickle'
        ),
            'rb',
            ) as handle:
        tokenizer = pickle.load(handle)
    data_test = [
        [
            str(year),
            str(base_okved),
            str(nalog),
            str(okfs),
            str(okopf),
            str(smsp),
        ]
    ]
    primer2_indexes = tokenizer.texts_to_sequences(data_test)
    primer2 = tokenizer.sequences_to_matrix(primer2_indexes)

    deal = ['участвует', 'не участвует']

    pred2 = loaded_model.predict(primer2)
    pred_deal = deal[np.argmax(pred2)]
    pred_persent = int(pred2[:, np.argmax(pred2)]*100)

    return (f'{pred_deal} - {pred_persent}%')
