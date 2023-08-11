import logging
from train_data import * 
from test_data import *
from simpletransformers.question_answering import QuestionAnsweringModel, QuestionAnsweringArgs
model_type="bert"
model_name= "bert-base-cased"
if model_type == "bert":
    model_name = "bert-base-cased"

elif model_type == "roberta":
    model_name = "roberta-base"

elif model_type == "distilbert":
    model_name = "distilbert-base-cased"

elif model_type == "distilroberta":
    model_type = "roberta"
    model_name = "distilroberta-base"

elif model_type == "electra-base":
    model_type = "electra"
    model_name = "google/electra-base-discriminator"

elif model_type == "electra-small":
    model_type = "electra"
    model_name = "google/electra-small-discriminator"

elif model_type == "xlnet":
    model_name = "xlnet-base-cased"
# Configure the model
model_args = QuestionAnsweringArgs()
model_args.train_batch_size = 16
model_args.evaluate_during_training = True
model_args.n_best_size=3
model_args.num_train_epochs=5

### Advanced Methodology
train_args = {
    "reprocess_input_data": True,
    "overwrite_output_dir": True,
    "use_cached_eval_features": True,
    "output_dir": f"outputs/{model_type}",
    "best_model_dir": f"outputs/{model_type}/best_model",
    "evaluate_during_training": True,
    "max_seq_length": 128,
    "num_train_epochs": 5,
    "evaluate_during_training_steps": 1000,
    "wandb_project": "Question Answer Application",
    "wandb_kwargs": {"name": model_name},
    "save_model_every_epoch": False,
    "save_eval_checkpoints": False,
    "n_best_size":3,
    # "use_early_stopping": True,
    # "early_stopping_metric": "mcc",
    # "n_gpu": 2,
    # "manual_seed": 4,
    # "use_multiprocessing": False,
    "train_batch_size": 128,
    "eval_batch_size": 64,
    # "config": {
    #     "output_hidden_states": True
    # }
}

model = QuestionAnsweringModel(
    model_type,model_name, args=train_args
)


key = "34a082d80e2e7194f25a46856cadb2658673fc00"
# Train the model
model.train_model(train_data, eval_data=test_data)
# Evaluate the model
result, texts = model.eval_model(test_data)
to_predict = [
    {
        "context": """CHANGES
CHARGE INR 2750 FOR REISSUE.
NOTE -
ABOVE CHARGES ARE EXCLUSIVE OF GST K3.
APPLICABLE GST RATE TO BE COLLECTED AND SHOWN
SEPARATELY UNDER TAX CODE K3.
CHARGE INR 3250 WITHIN 24 HOURS AND BEFORE 2
HOURS OF DEPARTURE OF FLIGHT.""",
        "qas": [
            {
                "question": "CANCELLATION PRICE BEFORE 24 HOURS?",
                "id": "0",
            }
        ],
    }
]
answers, probabilities = model.predict(to_predict)

price = answers[-1]['answer']
for i in price:
  print(i)
