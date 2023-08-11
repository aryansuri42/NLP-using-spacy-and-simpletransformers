import os
from DataCleaning import * 
dir_path = r'C:\Users\ARYAN SURI\Desktop\Minirules'
train = []
res = []
for file in os.listdir(dir_path):
    if file.endswith('.txt'):
        res.append(file)
id = 00000
cancel_id = 00000
for files in res:
    id+=1
    cancel_id+=1
    farerules = FileCleaning(str(files))
    rules = farerules.changes_split()[0]
    cancel_rules = farerules.cancellation_split()[0]
    test_data_dict_change = {
            "context": str(rules),
            "qas": [
                {
                    "id": id,
                    "is_impossible": False,
                    "question": "CHANGE PRICE BEFORE 24 HOURS?",
                    "answers": [
                        {
                            "text": "2750",
                            "answer_start": 66,
                        }
                    ],
                }
            ],
        }
    test_data_dict_cancel = {
            "context": str(cancel_rules),
            "qas": [
                {
                    "id": cancel_id,
                    "is_impossible": False,
                    "question": "CHANGE PRICE BEFORE 24 HOURS?",
                    "answers": [
                        {
                            "text": "2750",
                            "answer_start": 66,
                        }
                    ],
                }
            ],
        }
    train.append(test_data_dict_change)
    train.append(test_data_dict_cancel)
print(train)