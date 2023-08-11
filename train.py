train_data = [
    {
        "context": """CHANGES
PER COUPON CHARGE INR 3000 FOR REISSUE/REVALIDATION.
NOTE -
TEXT BELOW NOT VALIDATED FOR AUTOPRICING.
CHANGES FEE APPLIES AS BELOW
NO CHARGE FOR CHANGES MADE BEFORE 72 HOURS OF
DEPARTURE WITHIN 72 AND UNTIL 02 HOURS BEFORE
SCHEDULED DEPARTURE OF THE FLIGHT AGAINST A
CHANGE FEE OF INR 3000 PER COUPON OR BASIC FARE
WHICH EVER IS LOWER.""",
        "qas": [
            {
                "id": "00001",
                "is_impossible": False,
                "question": "CHANGE PRICE BEFORE 72 HOURS?",
                "answers": [
                    {
                        "text": "NO CHARGE",
                        "answer_start": 138,
                    }
                ],
            }
        ],
    },
    {
        "context": """CHANGES
PER COUPON CHARGE INR 3000 FOR REISSUE/REVALIDATION.
NOTE -
TEXT BELOW NOT VALIDATED FOR AUTOPRICING.
CHANGES FEE APPLIES AS BELOW
NO CHARGE FOR CHANGES MADE BEFORE 72 HOURS OF
DEPARTURE WITHIN 72 AND UNTIL 02 HOURS BEFORE
SCHEDULED DEPARTURE OF THE FLIGHT AGAINST A
CHANGE FEE OF INR 3000 PER COUPON OR BASIC FARE
WHICH EVER IS LOWER.""",
        "qas": [
            {
                "id": "00002",
                "is_impossible": False,
                "question": "CHANGE PRICE BEFORE 02 HOURS?",
                "answers": [
                    {
                        "text": "3000",
                        "answer_start": 292,
                    }
                ],
            }
       ]
},
{
        "context": """CANCELLATIONS
PER COUPON CHARGE INR 3500 FOR CANCEL.
NOTE 
TEXT BELOW NOT VALIDATED FOR AUTOPRICING.
CANCELLATION FEE APPLIES AS BELOW
WHEN CANCELLATION  ARE MADE BEFORE 72 HOURS OF
DEPARTURE A CHANGE FEE OF INR 2500 PER COUPON
WILL APPLY CANCELLATION MADE WITHIN 72 HOURS UNTILL
02 HOURS BEFORE SCHEDULED DEPARTURE OF
THE FLIGHT AGAINST A CHANGE FEE OF INR 3500 PER""",
        "qas": [
            {
                "id": "00003",
                "is_impossible": False,
                "question": "CANCELLATION PRICE BEFORE 72 HOURS?",
                "answers": [
                    {
                        "text": "2500",
                        "answer_start": 212,
                    }
                ],
            }
        ],
    },
{
        "context": """CANCELLATIONS
PER COUPON CHARGE INR 3500 FOR CANCEL.
NOTE -
TEXT BELOW NOT VALIDATED FOR AUTOPRICING.
CANCELLATION FEE APPLIES AS BELOW
WHEN CANCELLATION  ARE MADE BEFORE 72 HOURS OF
DEPARTURE A CHANGE FEE OF INR 2500 PER COUPON
WILL APPLY CANCELLATION MADE WITHIN 72 HOURS UNTILL
02 HOURS BEFORE SCHEDULED DEPARTURE OF
THE FLIGHT AGAINST A CHANGE FEE OF INR 3500 PER""",
        "qas": [
            {
                "id": "00004",
                "is_impossible": False,
                "question": "CANCELLATION PRICE BEFORE 02 HOURS?",
                "answers": [
                    {
                        "text": "3500",
                        "answer_start": 360,
                    }
                ],
            }
        ],
    },
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
                "id": "00005",
                "is_impossible": False,
                "question": "CHANGE PRICE BEFORE 24 HOURS?",
                "answers": [
                    {
                        "text": "2750",
                        "answer_start": 19,
                    }
                ],
            }
        ],
    },
{
        "context": """CHANGES
CHARGE INR 2750 FOR REISSUE.
NOTE -
ABOVE CHARGES ARE EXCLUSIVE OF GST K3.
APPLICABLE GST RATE TO BE COLLECTED AND SHOW
SEPARATELY UNDER TAX CODE K3.
CHARGE INR 3250 WITHIN 24 HOURS AND BEFORE 2
HOURS OF DEPARTURE OF FLIGHT.""",
        "qas": [
            {
                "id": "00006",
                "is_impossible": False,
                "question": "CHANGE PRICE BEFORE 2 HOURS?",
                "answers": [
                    {
                        "text": "3250",
                        "answer_start": 169,
                    }
                ],
            }
        ],
    },
{
        "context": """CANCELLATIONS
CHARGE INR 3250 FOR CANCEL/REFUND.
NOTE -
ABOVE CHARGES ARE EXCLUSIVE OF GST K3 AND APPLIE
PER FARE COMPONENT.
APPLICABLE GST RATE TO BE COLLECTED AND
ADDED TO THE PENALTY AMOUNT.
CHARGE INR 3750 WITHIN 24 HOURS AND BEFORE 2
HOURS OF DEPARTURE OF FLIGHT.""",
        "qas": [
            {
                "id": "00007",
                "is_impossible": False,
                "question": "CANCELLATION PRICE BEFORE 24 HOURS?",
                "answers": [
                    {
                        "text": "3250",
                        "answer_start": 25,
                    }
                ],
            }
        ],
    },
{
        "context": """CANCELLATIONS
CHARGE INR 3250 FOR CANCEL/REFUND.
NOTE -
ABOVE CHARGES ARE EXCLUSIVE OF GST K3 AND APPLIES
PER FARE COMPONENT.
APPLICABLE GST RATE TO BE COLLECTED AND
ADDED TO THE PENALTY AMOUNT.
CHARGE INR 3750 WITHIN 24 HOURS AND BEFORE 2
HOURS OF DEPARTURE OF FLIGHT.""",
        "qas": [
            {
                "id": "00008",
                "is_impossible": False,
                "question": "CANCELLATION PRICE BEFORE 2 HOURS?",
                "answers": [
                    {
                        "text": "3750",
                        "answer_start": 205,
                    }
                ],
            }
        ],
    }
]