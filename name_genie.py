
import random

import character_sets as char


def Generate_name(
    culture="default",
    syllables_min=1,
    syllables_max=9,
    dipthong_ratio=.5,
    praenomen_prefix_list=False,
    praenomen_prefix_ratio=.4,
    praenomen_suffix_list=False,
    praenomen_suffix_ratio=.4


    ):


    ##praenomen syllabic loop 
    ## Prefixes for first name
        if bool(praenomen_prefix_list) != False and random.random() <= praenomen_prefix_ratio:
            praenomen=random.choice(praenomen_prefix_list)
        else:
            praenomen=""
        ## first name randomizinator
        for i in range(random.randint(syllables_min,syllables_max)):
            random.choice(char.consonants_all)+random.choice(char.vowels)
            if (random.random()) < dipthong_ratio :      #if dipthong
                proc_syl=(random.choice(char.consonants_all)+random.choice(char.dipthongs))
            else:
                proc_syl=(random.choice(char.consonants_all)+random.choice(char.vowels))

            praenomen=(praenomen + proc_syl)
        ## Firstname suffix
        if bool(praenomen_suffix_list) != False and random.random() <= praenomen_suffix_ratio:
            praenomen=praenomen + random.choice(praenomen_suffix_list)
        else:
            pass
     
        return(culture,praenomen) 