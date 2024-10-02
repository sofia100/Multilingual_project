possible_relations = {
    "grandmother": {
        # od done
        "ory_Orya": {
            "ଜେଜେମା": {
                "description": "mother of father",
                "relation": "paternal",
                "relation_code": "M",  # Male or Female Side of me or my immediate family or BOth or None
                "gender": "F",
            },
            "ଆଈ": {
                "description": "mother of mother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
        },
        # bn done
        "ben_Beng": {
            "ঠাকুরমা": {
                "description": "mother of father",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "দিদি মা": {
                "description": "mother of mother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
            
        },
        # guj done
        "guj_Gujr": {
            "દાદી": {
                "description": "mother of father",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "નાની": {
                "description": "mother of mother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
        },
        # done
        "hin_Deva": {
            "दादी": {
                "description": "mother of father",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "नानी": {
                "description": "mother of mother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
             "पितामही": {
                "description": "father of mother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
        },
        # kn done
        "kan_Knda": {
            "ಅಜ್ಜಿ": {
                "description": "mother of father or mother",
                "relation": "both",
                "relation_code": "B",
                "gender": "F",
            }
        },
        # TODO
        "mal_Mlym": {
            "അമ്മൂമ്മ": {
                "description": "mother of father or mother",
                "relation": "both",
                "relation_code": "B",
                "gender": "F",
            }
        },
        "mar_Deva": {
            "आजी": {
                "description": "mother of father or mother",
                "relation": "Both",
                "relation_code": "B",
                "gender": "F",
            },
            "मावस आजी": {
                "description": "sister of mother of father or mother",
                "relation": "Both",
                "relation_code": "B",
                "gender": "F",
            },
        },
        # tam done
        "tam_Taml": {
            "அப்பத்தா": {
                "description": "mother of father",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "அம்மத்தா": {
                "description": "mother of mother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
            "சின்ன பாட்டி": {
                "description": "younger grandmother",
                "relation": "Both",
                "relation_code": "B",
                "gender": "F",
            },
            "பெரிய பாட்டி": {
                "description": "elder grandmother",
                "relation": "Both",
                "relation_code": "B",
                "gender": "F",
            },
            "பாட்டி": {
                "description": "grandmother",
                "relation": "Both",
                "relation_code": "B",
                "gender": "F",
            },
        },
        # telugu done
        "tel_Telu": {
            "నాన్నమ్మ": {
                "description": "mother of father",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "అమ్మమ": {
                "description": "mother of mother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
            "నాన్నమ": {
                "description": "father's mother's sister",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "చిన్న నాన్నమ": {
                "description": "father's mother's younger sister",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "పెద్ద  నాన్నమ": {
                "description": "father's mother's elder sister",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "అమ్మమ": {
                "description": "mother's mother's sister",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
            "చిన్న అమ్మమ": {
                "description": "mother's mother's younger sister",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
            "పెద్ద అమ్మమ": {
                "description": "mother's mother's elder sister",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
        },
        # Punjabi done
        "pan_Guru": {
            "ਦਾਦੀ": {
                "description": "mother of father",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "ਨਾਨੀ": {
                "description": "mother of mother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
        },
    },
    "grandfather": {
        # done
        "ory_Orya": {
            "ଜେଜେବାପା": {
                "description": "father of father",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "ଅଜା": {
                "description": "father of mother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
        },
        # done
        "ben_Beng": {
            "ঠাকুরদা": {
                "description": "father of father",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "দাদু": {
                "description": "father of mother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
        },
        # done
        "guj_Gujr": {
            "દાદા": {
                "description": "father of father",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "નાના": {
                "description": "father of mother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
        },
        # done
        "hin_Deva": {
            "दादा": {
                "description": "father of father",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "नाना": {
                "description": "father of mother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            # "प्रपितामह":{
            #     "description": "father of father of father",
            #     "relation": "paternal",
            #     "relation_code": "M",
            #     "gender": "M",
            # },
            "पितामह": {
                "description": "father of father",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
           

        },
        # done
        "kan_Knda": {
            "ಅಜ್ಜ": {
                "description": "father of father or mother",
                "relation": "Both",
                "relation_code": "B",
                "gender": "M",
            },
        },
        # done
        "mal_Mlym": {
            "അപ്പൂപ്പൻ": {
                "description": "father of father or mother",
                "relation": "Both",
                "relation_code": "B",
                "gender": "M",
            }
        },
        "mar_Deva": {
            "आजोबा": {
                "description": "father of father or mother",
                "relation": "Both",
                "relation_code": "B",
                "gender": "M",
            },
            "चुलत आजोबा": {
                "description": "cousin of father of father or mother",
                "relation": "Both",
                "relation_code": "B",
                "gender": "M",
            },
        },
        # done
        "tam_Taml": {
            "தாத்தா": {
                "description": "father of father or mother",
                "relation": "both",
                "relation_code": "B",
                "gender": "M",
            },
            "சின்ன தாத்தா": {
                "description": "mother's or father's father's younger brother",
                "relation": "both",
                "relation_code": "B",
                "gender": "M",
            },
            "பெரிய தாத்தா": {
                "description": "mother's or father's father's elder brother",
                "relation": "both",
                "relation_code": "B",
                "gender": "M",
            },
        },
        "tel_Telu": {
            "తాతయ్యగారు": {
                "description": "father of father or mother",
                "relation": "both",
                "relation_code": "B",
                "gender": "M",
            },
            "తాతయ్య": {
                "description": "grandfather",
                "relation": "both",
                "relation_code": "B",
                "gender": "M",
            },
            "చిన్న తాతయ్య": {
                "description": "younger grandfather",
                "relation": "both",
                "relation_code": "B",
                "gender": "M",
            },
            "పెద్ద తాతయ్య": {
                "description": "elder grandfather",
                "relation": "both",
                "relation_code": "B",
                "gender": "M",
            },
        },
        "pan_Guru": {
            "ਦਾਦਾ": {
                "description": "father of father",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "ਨਾਨਾ": {
                "description": "father of mother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
        },
    },
    "uncle": {
        "ory_Orya": {
            "ବଡ଼ବାପା": {
                "description": "father's elder brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "ଦାଦା": {
                "description": "father's younger brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "ମାମୁଁ": {
                "description": "mother's brother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "ପିଉସା": {
                "description": "father's sister's husband",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "ମଉସା": {
                "description": "mother's sister's husband",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
        },
        "ben_Beng": {
            "জেঠা মশাই": {
                "description": "father's elder brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "কাকু": {
                "description": "father's younger brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "মামা": {
                "description": "mother's brother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "পিশে মশাই": {
                "description": "father's sister's husband",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "মেশো মশাই": {
                "description": "mother's sister's husband",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
        },
        "guj_Gujr": {
            "કાકા": {
                "description": "Father's elder or younger brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "મામા": {
                "description": "Mother's elder brother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
        },
        "hin_Deva": {
            "ताऊ": {
                "description": "father's elder brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "चाचा": {
                "description": "father's younger brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "मामा": {
                "description": "mother's elder brother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "फूफा": {
                "description": "father's elder or younger sister's husband",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "मौसा": {
                "description": "mother's elder or younger sister's husband",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
        },
        "kan_Knda": {
            "ದೊಡಪ್ಪ": {
                "description": "father's elder brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "ಚಿಕ್ಕಪ್ಪ": {
                "description": "father's younger brother or mother's younger sister's husband",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "ಮಾಮ": {
                "description": "mother's brother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "ಮಾವ": {
                "description": "father's sister's husband",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "ದೊಡ್ಡಪ್ಪ": {
                "description": "mother's elder sister's husband",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
        },
        "mal_Mlym": {
            "അമ്മാവൻ": {
                "description": "uncle",
                "relation": "Both",
                "relation_code": "B",
                "gender": "M",
            },
            "മൂത്ത അച്ഛൻ": {
                "description": "father's elder brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "ചിറ്റപ്പൻ": {
                "description": "father's younger brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "മൂത്തമാമൻ": {
                "description": "mother's elder brother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "ഇളയമാമൻ": {
                "description": "mother's younger brother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "മാമൻ": {
                "description": "father's sister's husband",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "വല്ല്യച്ചൻ": {
                "description": "mother's elder sister's husband",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "ചാച്ചൻ": {
                "description": "mother's younger sister's husband",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
        },
        "mar_Deva": {
            "काका": {
                "description": "father's brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "मामा": {
                "description": "mother's brother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "मावसा": {
                "description": "mother's sister's husband",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
        },
        "tam_Taml": {
            "பெரியப்பா": {
                "description": "father's elder brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "சித்தப்பா": {
                "description": "father's younger brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "பெரியப்பா": {
                "description": "mother's elder brother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "மாமா": {
                "description": "mother's younger brother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "பெரியப்பா": {
                "description": "father's elder sister's husband",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "மாமா": {
                "description": "father's younger sister's husband",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "மாமா": {
                "description": "mother's elder sister's husband",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "சித்தப்பா": {
                "description": "mother's younger sister's husband",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
        },
        "tel_Telu": {
            "పెద్ద నాన్న": {
                "description": "father's elder brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "ఆయగారు": {
                "description": "father's elder brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "మామయ్య": {
                "description": "mother's brother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "మామయ్యగారు": {
                "description": "father's elder sister's husband",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "పెద్ద నాన్న": {
                "description": "mother's elder sister's husband",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "చిన్న  నాన్న": {
                "description": "mother's younger sister's husband",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
        },
        "pan_Guru": {
            "ਤਾਇਆ": {
                "description": "father's elder brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "ਚਾਚਾ": {
                "description": "father's younger brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "ਮਾਮਾ": {
                "description": "mother's brother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "ਫੁੱਫੜ": {
                "description": "father's elder sister's husband",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "ਮਾਸੜ": {
                "description": "mother's elder sister's husband",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
        },
    },
    "aunt": {
        "ory_Orya": {
            "ପିଉସୀ": {
                "description": "father's sister",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "ମାଉସୀ": {
                "description": "mother's sister",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
            "ମାଇଁ": {
                "description": "mother's brother's wife",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
            "ବଡ଼ମାଆ": {
                "description": "father's elder brother's wife",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "ଖୁଡ଼ି": {
                "description": "father's younger brother's wife",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
        },
        "ben_Beng": {
            "পিসি": {
                "description": "father's sister",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "মাসী": {
                "description": "mother's sister",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
            "মামী": {
                "description": "mother's brother's wife",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
            "জেঠি": {
                "description": "father's elder brother's wife",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "কাকি": {
                "description": "father's younger brother's wife",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
        },
        "guj_Gujr": {
            "ફોઈ": {
                "description": "father's sister",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "માસી": {
                "description": "mother's sister",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
            "મામી": {
                "description": "mother's brother's wife",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
            "કાકી": {
                "description": "father's brother's wife",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
        },
        "hin_Deva": {
            "बुआ": {
                "description": "father's sister",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "मौसी": {
                "description": "mother's sister",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
            "मामी": {
                "description": "mother's brother's wife",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
            "ताई": {
                "description": "father's elder brother's wife",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "चाची": {
                "description": "father's younger brother's wife",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
        },
        "kan_Knda": {
            "ಅತ್ತೆ": {
                "description": "father's sister or mother's brother's wife",
                "relation": "Both",
                "relation_code": "B",
                "gender": "F",
            },
            "ದೊಡ್ಡಮ್ಮ": {
                "description": "mother's elder sister or father's elder brother's wife",
                "relation": "Both",
                "relation_code": "B",
                "gender": "F",
            },
            "ಚಿಕ್ಕಮ್ಮ": {
                "description": "father's younger brother's wife or mother's younger sister",
                "relation": "Both",
                "relation_code": "B",
                "gender": "F",
            },
        },
        "mal_Mlym": {
            "മുത്തഅപ്പച്ചി": {
                "description": "father's elder sister",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "ഇളയ അപ്പച്ചി": {
                "description": "father's younger sister",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "വല്യമ്മ": {
                "description": "mother's elder sister",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
            "കുഞ്ഞമ്മ": {
                "description": "mother's younger sister or father's younger brother's wife",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
            "വലിയ മാമി": {
                "description": "mother's elder brother's wife",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
            "ചെറിയ മാമി": {
                "description": "mother's younger brother's wife",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
        },
        "mar_Deva": {
            "आत्या": {
                "description": "father's sister",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "मावशी": {
                "description": "mother's sister",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
            "काकू": {
                "description": "father's brother's wife",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "काकी": {
                "description": "father's brother's wife",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
        },
        "tam_Taml": {
            "அத்தை": {
                "description": "father's elder sister or mother's elder brother's wife or mother's elder sister ",
                "relation": "Both",
                "relation_code": "B",
                "gender": "F",
            },
            "சித்தி": {
                "description": "father's younger brother's wife or mother's younger sister or father's younger sister",
                "relation": "Both",
                "relation_code": "B",
                "gender": "F",
            },
            "பெரியம்மா": {
                "description": "father's elder brother's wife",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "மாமி": {
                "description": "mother's younger brother's wife",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
        },
        "tel_Telu": {
            "అత్త": {
                "description": "father's sister or mother's brother's wife",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "పెద్దమ్మ": {
                "description": "mother's elder sister or father's elder brother's wife",
                "relation": "Both",
                "relation_code": "B",
                "gender": "F",
            },
            "పిన్ని": {
                "description": "mother's younger sister or father's younger brother's wife",
                "relation": "Both",
                "relation_code": "B",
                "gender": "F",
            },
        },
        "pan_Guru": {
            "ਭੂਆ": {
                "description": "father's sister",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "ਮਾਸੀ": {
                "description": "mother's sister",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
            "ਮਾਮੀ": {
                "description": "mother's brother's wife",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
            "ਤਾਈ": {
                "description": "father's brother's wife",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
        },
    },
    "brother-in-law": {
        "ory_Orya": {
            "ବଡ଼ ଶଳା": {
                "description": "wife's elder brother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "ଶଳା": {
                "description": "wife's younger brother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "ଭିଣେଇ": {
                "description": "elder sister's husband",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "ଦେଢ଼ଶୁର": {
                "description": "husband's elder brother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "ଦିଅର": {
                "description": "husband's younger brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
        },
        "ben_Beng": {
            "বড়ো শালা": {
                "description": "wife's elder brother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "ছোট শালা": {
                "description": "wife's younger brother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "শালা": {
                "description": "wife's  brother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "জামাই বাবু": {
                "description": "elder sister's husband",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "জামাই": {
                "description": "elder sister's husband",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "ভাসুর": {
                "description": "husband's elder brother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "দেওর": {
                "description": "husband's younger brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
        },
        "guj_Gujr": {
            "સાળો": {
                "description": "wife's   brother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "બનેવી": {
                "description": " sister's husband",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "જેઠ": {
                "description": "husband's elder brother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "દિયર": {
                "description": "husband's younger brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
        },
        "hin_Deva": {
            "साला": {
                "description": "wife's   brother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "जीजा": {
                "description": " sister's husband",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "जेठ": {
                "description": "husband's elder brother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "देवर": {
                "description": "husband's younger brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "बहनोई": {
                "description": "elder sister's husband",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            }
        },
        "kan_Knda": {
            "ಭಾವ": {
                "description": "wife's elder brother or younger sister's husband",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "ಬಾವ": {
                "description": "wife's younger brother or elder sister's husband or husband's elder brother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "ಮೈದುನ": {
                "description": "husband's younger brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
        },
        "mal_Mlym": {
            "അളിയൻ": {
                "description": "wife's   brother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "ചേട്ടൻ": {
                "description": "elder sister's husband or husband's elder brother",
                "relation": "both",
                "relation_code": "B",
                "gender": "M",
            },
            "അനിയൻ": {
                "description": "younger sister's husband or husband's younger brother",
                "relation": "both",
                "relation_code": "B",
                "gender": "M",
            },
        },
        "mar_Deva": {
            "मेहुणा": {
                "description": "wife's elder brother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "मेव्हणा": {
                "description": "wife's elder brother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "दाजी": {
                "description": "elder sister's husband",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "भाऊजी": {
                "description": "elder sister's husband",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "दीर": {
                "description": "husband's brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
        },
        "tam_Taml": {
            "மைத்துனர்": {
                "description": "wife's   brother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "அத்திம்பேர்": {
                "description": "elder sister's husband ",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "மாமா": {
                "description": "elder sister's husband ",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "மைத்துனன்": {
                "description": "younger sister's husband ",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "கொழுந்தன்": {
                "description": "husband's younger brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
        },
        "tel_Telu": {
            "బావగారు": {
                "description": "wife's elder brother or elder sister's husband or husband's elder brother",
                "relation": "both",
                "relation_code": "B",
                "gender": "M",
            },
            "బావమరిది": {
                "description": "wife's younger brother ",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "మరిదిగారు": {
                "description": "husband's younger brother or younger sister's husband",
                "relation": "both",
                "relation_code": "B",
                "gender": "M",
            },
        },
        "pan_Guru": {
            "ਸਾਲਾ": {
                "description": "wife's  brother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "ਜੀਜਾ": {
                "description": "sister's husband",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "ਜੇਠ": {
                "description": "husband's elder brother",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "ਦੇਵਰ": {
                "description": "husband's younger brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "ਸਾਂਡੂ": {
                "description": "wife's sister's husband",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
        },
    },
    # done till above
    ############################################################################################################
    "sister-in-law": {
        "ory_Orya": {
            "ବଡ଼ ନଣନ୍ଦ": {
                "description": "husband's elder sister",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "ନଣନ୍ଦ": {
                "description": "husband's younger sister",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "ଭାଉଜ": {
                "description": "elder brother's wife",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "ଭାଇବୋହୁ": {
                "description": "younger brother's wife",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "ଦେଢ଼ଶାସୁ": {
                "description": "wife's elder sister",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
            "ଶାଳୀ": {
                "description": "wife's younger sister",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
        },
        "ben_Beng": {
            "বড়ো ননদ": {
                "description": "husband's elder sister",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "ছোট ননদ": {
                "description": "husband's younger sister",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "ননদ": {
                "description": "husband's sister",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "বড়ো জা": {
                "description": "elder brother's wife",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "ছোট জা": {
                "description": "younger brother's wife",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "জা": {
                "description": "brother's wife",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "বড়ো শালী": {
                "description": "wife's elder sister",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
            "ছোট শালী": {
                "description": "wife's younger sister",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
            "শালী": {
                "description": "wife's sister",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
        },
        "guj_Gujr": {
            "નણંદ": {
                "description": "husband's   sister",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "ભાભી": {
                "description": "elder brother's wife",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "સાળી": {
                "description": "wife's   sister",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
        },
        "hin_Deva": {
            "नानद": {
                "description": "husband's   sister",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "भाभी": {
                "description": "  brother's wife",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "साली": {
                "description": "wife's   sister",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
        },
        "kan_Knda": {
            "ಅತ್ತೀಗೆ": {
                "description": "husband's elder sister",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "ನಾಧಿನಿ": {
                "description": "husband's younger sister",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "ಅತ್ತಿಗೆ": {
                "description": "elder brother's wife or wife's elder sister",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "ನಾಧಿನೀ": {
                "description": "younger brother's wife",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "ನಾಧೀನಿ": {
                "description": "wife's younger sister",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
        },
        "mal_Mlym": {
            "മൂത്ത നാത്തൂൻ": {
                "description": "husband's elder sister",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "ഇളയ നാത്തൂൻ": {
                "description": "husband's younger sister",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "ചേട്ടത്തി": {
                "description": "elder brother's wife",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            " അനുജത്തി": {
                "description": "younger brother's wife or wife's younger sister",
                "relation": "both",
                "relation_code": "B",
                "gender": "F",
            },
            "ചേച്ചി": {
                "description": "wife's elder sister",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
        },
        "mar_Deva": {
            "नणंद": {
                "description": "husband's sister",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "वहिनी": {
                "description": "(if person is male) brother's wife",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "भावजय": {
                "description": "(if person is female) brother's wife",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "मेहुणी": {
                "description": "wife's sister",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
            "मेव्हणी": {
                "description": "wife's sister",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
        },
        "tam_Taml": {
            "நாத்தனார்": {
                "description": "husband's sister",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "மைத்துனி": {
                "description": "husband's sister",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "அண்ணி": {
                "description": "elder brother's wife",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "கொழுந்தியாள்": {
                "description": "younger brother's wife",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "அக்கா": {
                "description": "wife's elder sister",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
            "தங்கை": {
                "description": "wife's younger sister",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
        },
        "tel_Telu": {
            "వదినగారు": {
                "description": "husband's elder sister",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "ఆడపడచు": {
                "description": "husband's younger sister",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "వదిన": {
                "description": "elder brother's wife or wife's elder sister",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "మరదలు": {
                "description": "younger brother's wife or wife's younger sister",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
        },
        "pan_Guru": {
            "ਨਣਦ": {
                "description": "husband's   sister",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "ਭਾਬੀ": {
                "description": "  brother's wife",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "ਸਾਲੀ": {
                "description": "wife's   sister",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
            "ਜੇਠਾਣੀ": {
                "description": "husband's brother's wife",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
        },
    },
    "cousin": {
        "ory_Orya": {
            "ଭାଇ": {
                "description": "cousin brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "ଦିଦି": {
                "description": "cousin sister",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
        },
        "ben_Beng": {
            "দাদা": {
                "description": "elder cousin brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "ভাই": {
                "description": "younger cousin brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "দিদি": {
                "description": "elder cousin sister",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
            "বোনষষ": {
                "description": "younger cousin sister",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
        },
        "guj_Gujr": {
            "દીકરો": {
                "description": "cousin brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "દીકરી": {
                "description": "cousin sister",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
        },
        "hin_Deva": {
            "भाई": {
                "description": "cousin brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "बहन": {
                "description": "cousin sister",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
        },
        "kan_Knda": {
            "ಅಣ್ಣ": {
                "description": "cousin elder brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "ಅಕ್ಕ": {
                "description": "cousin elder sister",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
            " ತಮ್ಮ": {
                "description": "cousin younger brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "ತಂಗಿ": {
                "description": "cousin younger sister",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
        },
        "mal_Mlym": {
            "ബന്ധു": {
                "description": "cousin ",
                "relation": "both",
                "relation_code": "B",
                "gender": "M",
            },
        },
        "mar_Deva": {
            "चुलत भाऊ": {
                "description": "father's brother's son",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "मामे भाऊ": {
                "description": "mother's elder brother's son",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
            "आत्ये भाऊ": {
                "description": "father's sister's son",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "मावस भाऊ": {
                "description": "mother's sister's son",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "चुलत बहीण": {
                "description": "father's brother's daughter",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "मामे बहीण": {
                "description": "mother's elder brother's daughter",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
            "आत्ये बहीण": {
                "description": "father's sister's daughter",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "मावस बहीण": {
                "description": "mother's sister's daughter",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
        },
        "tam_Taml": {
            "அண்ணா": {
                "description": "cousin brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "தம்பி": {
                "description": "cousin brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "அக்கா": {
                "description": "cousin sister",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
        },
        "tel_Telu": {
            "అన్నా": {
                "description": "cousin brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "తమ్ముడు": {
                "description": "cousin brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            " అక్కా": {
                "description": "cousin sister",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
        },
        "pan_Guru": {
            "ਭਾਈ": {
                "description": "cousin brother",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "ਭੈਣ": {
                "description": "cousin sister",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
        },
    },
    "child": {
        "ory_Orya": {
            "ପୁଅ": {
                "description": "son",
                "relation": "Both",
                "relation_code": "B",
                "gender": "M",
            },
            "ଝିଅ": {
                "description": "daughter",
                "relation": "Both",
                "relation_code": "B",
                "gender": "F",
            },
            "ପିଲା": {
                "description": "child",
                "relation": "Both",
                "relation_code": "B",
                "gender": "N",  # gender Neutral
            },
        },
        "ben_Beng": {
             "শিশু": {
                "description": "child",
                "relation": "Both",
                "relation_code": "B",
                "gender": "N",  # gender Neutral
            },
            "ছেলে": {
                "description": "son",
                "relation": "Both",
                "relation_code": "B",
                "gender": "M",
            },
            "মেয়ে": {
                "description": "daughter",
                "relation": "Both",
                "relation_code": "B",
                "gender": "F",
            },
        },
        "guj_Gujr": {
            # synthetic data
            "બાળક": {
                "description": "son",
                "relation": "Both",
                "relation_code": "B",
                "gender": "M",
            },
            "બાકિકા": {
                "description": "daughter",
                "relation": "Both",
                "relation_code": "B",
                "gender": "F",
            },
        },
        "hin_Deva": {
            "बच्चा": {
                "description": "son",
                "relation": "Both",
                "relation_code": "B",
                "gender": "M",
            },
            "बच्चे": {
                "description": "son/daughter",
                "relation": "Both",
                "relation_code": "B",
                "gender": "N",
            },
            "बच्ची": {
                "description": "daughter",
                "relation": "Both",
                "relation_code": "B",
                "gender": "F",
            },
            "बालक": {
                "description": "son",
                "relation": "Both",
                "relation_code": "B",
                "gender": "M",
            },
            "बालिका": {
                "description": "daughter",
                "relation": "Both",
                "relation_code": "B",
                "gender": "F",
            },
        },
        "kan_Knda": {
            "ಮಗ": {
                "description": "son",
                "relation": "Both",
                "relation_code": "B",
                "gender": "M",
            },
            "ಮಗಳು": {
                "description": "daughter",
                "relation": "Both",
                "relation_code": "B",
                "gender": "F",
            },
        },
        # synthetic data:
        "mal_Mlym": {
            "ആൺകുട്ടി": {
                "description": "son",
                "relation": "Both",
                "relation_code": "B",
                "gender": "M",
            },
            "പെൺകുട്ടി": {
                "description": "daughter",
                "relation": "Both",
                "relation_code": "B",
                "gender": "F",
            },
            "കുട്ടി": {
                "description": "child",
                "relation": "Both",
                "relation_code": "B",
                "gender": "N",  # gender Neutral
            },
        },
        "mar_Deva": {
            "मुलगा": {
                "description": "son",
                "relation": "Both",
                "relation_code": "B",
                "gender": "M",
            },
            "मुलगी": {
                "description": "daughter",
                "relation": "Both",
                "relation_code": "B",
                "gender": "F",
            },
        },
        "tam_Taml": {
            "சிறுவன்": {
                "description": "son",
                "relation": "Both",
                "relation_code": "B",
                "gender": "M",
            },
            "சிறுமி": {
                "description": "daughter",
                "relation": "Both",
                "relation_code": "B",
                "gender": "F",
            },
        },
        "tel_Telu": {
            "బాలుడు": {
                "description": "son",
                "relation": "Both",
                "relation_code": "B",
                "gender": "M",
            },
            "బాలిక": {
                "description": "daughter",
                "relation": "Both",
                "relation_code": "B",
                "gender": "F",
            },
        },
        "pan_Guru": {
            "ਮੁੰਡਾ": {
                "description": "son",
                "relation": "Both",
                "relation_code": "B",
                "gender": "M",
            },
            "ਕੁੜੀ": {
                "description": "daughter",
                "relation": "Both",
                "relation_code": "B",
                "gender": "F",
            },
        },
    },
    "nephew": {
        "ory_Orya": {
            "ପୁତୁରା": {
                "description": "brother's son",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "ଭଣଜା": {
                "description": "sister's son",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
        },
        "ben_Beng": {
            "ভাইপৌ": {
                "description": "brother's son",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "বোনপৌ": {
                "description": "sister's son",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
        },
        "guj_Gujr": {
            "ભત્રીજો": {
                "description": "brother's son",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "ભાણેજ": {
                "description": "sister's son",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
            "ભાણો": {
                "description": "sister's son",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
        },
        "hin_Deva": {
            "भतीजा": {
                "description": "brother's son",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "भांजा": {
                "description": "sister's son",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
        },
        "kan_Knda": {
            "ಸೋದರ ಅಳಿಯ": {
                "description": "brother's son",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "ಸೋದರ ಮಗ": {
                "description": "sister's son",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
        },
        "mal_Mlym": {
            "അനന്തരവൻ": {
                "description": "brother's son",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "മരുമകൻ": {
                "description": "sister's son",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
        },
        "mar_Deva": {
            "पुतणा": {
                "description": "brother's son",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "भाचा": {
                "description": "sister's son",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
        },
        "tam_Taml": {
            "அண்ணன் மகன்": {
                "description": "brother's son",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "தம்பி மகன்": {
                "description": "brother's son",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "மைத்துனன்": {
                "description": "sister's son",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
        },
        "tel_Telu": {
            "మేనకొడుకు": {
                "description": "brother's son",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "అల్లుడు": {
                "description": "sister's son",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            },
        },
        "pan_Guru": {
            "ਭਤੀਜਾ": {
                "description": "brother's son",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "M",
            },
            "ਭਾਂਜਾ":
            {
                  "description": "sister's son",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "M",
            }
        },
    },
    "niece": {
        "ory_Orya": {
            "ଝିଆରୀ": {
                "description": "brother's daughter",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "ଭାଣିଜୀ": {
                "description": "sister's daughter",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
        },
        "ben_Beng": {
            "ভাইঝী": {
                "description": "brother's daughter",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "বোনঝী": {
                "description": "sister's daughter",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
        },
        "guj_Gujr": {
            "ભત્રીજી": {
                "description": "brother's daughter",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "ભાણેજી": {
                "description": "sister's daughter",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
            "ભાણી": {
                "description": "sister's daughter",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
        },
        "hin_Deva": {
            "भतीजी": {
                "description": "brother's daughter",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "भांजी": {
                "description": "sister's daughter",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
        },
        "kan_Knda": {
            "ಸೋದರ  ಮಗಳು": {
                "description": "brother's daughter",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "ಸೋದರ ಸೊಸೆ": {
                "description": "sister's daughter",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
        },
        "mal_Mlym": {
            "അനന്തരവൾ": {
                "description": "brother's daughter",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "മരുമകൾ": {
                "description": "sister's daughter",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
        },
        "mar_Deva": {
            "पुतणी": {
                "description": "brother's daughter",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "भाची": {
                "description": "sister's daughter",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
        },
        "tam_Taml": {
            "அண்ணன் மகள்": {
                "description": "brother's daughter",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "தம்பி மகள்": {
                "description": "brother's daughter",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "மைத்துனி": {
                "description": "sister's daughter",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
        },
        "tel_Telu": {
            "మేనకోడలు": {
                "description": "brother's daughter",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "అమ్మాయి": {
                "description": "sister's daughter",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            },
        },
        "pan_Guru": {
            "ਭਤੀਜੀ": {
                "description": "brother's daughter",
                "relation": "paternal",
                "relation_code": "M",
                "gender": "F",
            },
            "ਭਾਂਜੀ":{
                 "description": "sister's daughter",
                "relation": "maternal",
                "relation_code": "F",
                "gender": "F",
            }

        },
    },
}
