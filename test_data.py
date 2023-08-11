test_data = [
    {
        "context": """FOR ALL CHANGES 24 HOURS BEFORE DEPARTURE OF A FLIGHT A CHARGE OF 2750 INR MUST BE COLLECTED FOR CHANGE OF RESERVATION. THIS APPLIES PER SECTOR/ROUTE FOR DATE/FLIGHT CHANGE.""",
        "qas": [
            {
                "id": "00001",
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
    },
    {
        "context": """CHANGES
    ANY TIME
      CHANGES PERMITTED FOR REISSUE/REVALIDATION.
         NOTE -
          CHARGE INR 500 PER CHANGE. EXCLUSIVE OF GST
          NO CHANGES PERMITTED WITHIN 2 HR OF DEPARTURE""",
        "qas": [
            {
                "id": "00002",
                "is_impossible": False,
                "question": "CHANGE PRICE BEFORE 2 HOURS?",
                "answers": [
                    {
                        "text": "500",
                        "answer_start": 108,
                    }
                ],
            }
        ],
    },
    {
        "context": """CHANGES
    ANY TIME
      CHARGE CAD 100.00 FOR REISSUE/REVALIDATION.
      WAIVED FOR DEATH OF PASSENGER OR FAMILY MEMBER.
         NOTE -
          FOR ALL CHANGES WITHIN 96 HOURS BEFORE DEPARTURE
          OF A FLIGHT A CHARGE OF 110 CAD MUST BE COLLECTED
          FOR CHANGE OF RESERVATION.""",
        "qas": [
            {
                "id": "00003",
                "is_impossible": False,
                "question": "CHANGE PRICE BEFORE 96 HOURS?",
                "answers": [
                    {
                        "text": "100.00",
                        "answer_start": 145,
                    }
                ],
            }
        ],
    },
    {
        "context": """CHANGES
    ANY TIME
      CHARGE CAD 300.00 FOR REISSUE/REVALIDATION.
      WAIVED FOR DEATH OF PASSENGER OR FAMILY MEMBER.
         NOTE -
          FOR ALL CHANGES WITHIN 96 HOURS BEFORE DEPARTURE
          OF A FLIGHT A CHARGE OF 330 CAD MUST BE COLLECTED
          FOR CHANGE OF RESERVATION.""",
        "qas": [
            {
                "id": "00004",
                "is_impossible": False,
                "question": "CHANGE PRICE BEFORE 96 HOURS?",
                "answers": [
                    {
                        "text": "300.00",
                        "answer_start": 145,
                    }
                ],
            }
        ],
    }
]

