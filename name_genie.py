
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
    praenomen_suffix_ratio=.4,
    nomen_prefix_list=False,
    nomen_prefix_ratio=.4,
    nomen_suffix_list=False,
    nomen_suffix_ratio=.4,
    force_alliteration=False,
    cognomen_ratio=.1,
    cognomen_list=False,
    title_ratio= .1,
    title_list=False

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
####Nomen 
        nomen=""
    ## surname randomizinator
        for i in range(random.randint(syllables_min,syllables_max)):
            random.choice(char.consonants_all)+random.choice(char.vowels)
            if (random.random()) <= dipthong_ratio :      #if dipthong
                proc_syl=(random.choice(char.consonants_all)+random.choice(char.dipthongs))
            else:
                proc_syl=(random.choice(char.consonants_all)+random.choice(char.vowels))
            nomen=(nomen + proc_syl)
    ##  alliteration between prae and nomen             
        if force_alliteration==True:
            nomen=praenomen[0]+nomen[1:]
        ##Nomen prefix
        if bool(nomen_prefix_list) != False and random.random() <= nomen_prefix_ratio:
            nomen_prefix=random.choice(nomen_prefix_list)
            nomen=nomen_prefix + nomen
            nomen_suffix_ratio / 2
    ## surname suffix
        if bool(nomen_suffix_list) != False and random.random() <= nomen_suffix_ratio:
            nomen=nomen + random.choice(nomen_suffix_list)
        else:
            if random.randint(0,9) <= 4 and ((len(nomen)/2) - 2) > syllables_min:
                print(nomen, " became ", nomen[:-1])
                nomen=nomen[:-1]
##Cognomen 

        if (random.random()) <= cognomen_ratio and bool(cognomen_list) != False:
            cognomen_list=(random.choice(cognomen_list).title())
        else:
            cognomen_list=""
##Titles
        if (random.random()) <= title_ratio and bool(title_list) != False:
            title_list=(random.choice(title_list).title())
        else:
            title_list=""

        return{'culture':culture,'praenomen':praenomen,'nomen':nomen,'cognomen':cognomen_list,'title':title_list} 

