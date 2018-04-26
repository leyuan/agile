NAME_LIST_PATH = "src-data/name_list.txt"
EN_FILE_PATH = "src-data/en_list3.txt"
DATA_FOLDERS = ["src-data/news2018/news2018/data/", "src-data/news2015/news2015/"]

EN_STOP_WORDS = {
    "a" : 1,
    "aboard" : 1,
    "about" : 1,
    "above" : 1,
    "across" : 1,
    "after" : 1,
    "afterwards" : 1,
    "again" : 1,
    "against" : 1,
    "albeit" : 1,
    "all" : 1,
    "almost" : 1,
    "alone" : 1,
    "along" : 1,
    "already" : 1,
    "also" : 1,
    "although" : 1,
    "always" : 1,
    "am" : 1,
    "amid" : 1,
    "amidst" : 1,
    "among" : 1,
    "amongst" : 1,
    "amount" : 1,
    "an" : 1,
    "and" : 1,
    "another" : 1,
    "any" : 1,
    "anybody" : 1,
    "anyhow" : 1,
    "anyone" : 1,
    "anything" : 1,
    "anyway" : 1,
    "anywhere" : 1,
    "are" : 1,
    "around" : 1,
    "as" : 1,
    "at" : 1,
    "back" : 1,
    "be" : 1,
    "because" : 1,
    "been" : 1,
    "before" : 1,
    "beforehand" : 1,
    "behind" : 1,
    "being" : 1,
    "below" : 1,
    "beneath" : 1,
    "beside" : 1,
    "besides" : 1,
    "between" : 1,
    "beyond" : 1,
    "both" : 1,
    "but" : 1,
    "by" : 1,
    "can" : 1,
    "cannot" : 1,
    "cant" : 1,
    "circa" : 1,
    "co" : 1,
    "concerning" : 1,
    "could" : 1,
    "despite" : 1,
    "did" : 1,
    "do" : 1,
    "does" : 1,
    "done" : 1,
    "down" : 1,
    "due" : 1,
    "during" : 1,
    "each" : 1,
    "eg" : 1,
    "eight" : 1,
    "either" : 1,
    "else" : 1,
    "elsewhere" : 1,
    "enough" : 1,
    "etc" : 1,
    "even" : 1,
    "ever" : 1,
    "every" : 1,
    "everybody" : 1,
    "everyone" : 1,
    "everything" : 1,
    "everywhere" : 1,
    "except" : 1,
    "excepting" : 1,
    "few" : 1,
    "for" : 1,
    "from" : 1,
    "front" : 1,
    "further" : 1,
    "get" : 1,
    "give" : 1,
    "go" : 1,
    "had" : 1,
    "has" : 1,
    "have" : 1,
    "he" : 1,
    "hence" : 1,
    "her" : 1,
    "here" : 1,
    "hereafter" : 1,
    "hereby" : 1,
    "herein" : 1,
    "hereupon" : 1,
    "hers" : 1,
    "herself" : 1,
    "him" : 1,
    "himself" : 1,
    "his" : 1,
    "how" : 1,
    "however" : 1,
    "i" : 1,
    "ie" : 1,
    "if" : 1,
    "in" : 1,
    "inc" : 1,
    "indeed" : 1,
    "instead" : 1,
    "into" : 1,
    "is" : 1,
    "it" : 1,
    "its" : 1,
    "itself" : 1,
    "just" : 1,
    "latter" : 1,
    "latterly" : 1,
    "least" : 1,
    "less" : 1,
    "lest" : 1,
    "let" : 1,
    "like" : 1,
    "ltd" : 1,
    "made" : 1,
    "many" : 1,
    "may" : 1,
    "me" : 1,
    "meanwhile" : 1,
    "might" : 1,
    "mine" : 1,
    "more" : 1,
    "moreover" : 1,
    "most" : 1,
    "mostly" : 1,
    "move" : 1,
    "much" : 1,
    "must" : 1,
    "my" : 1,
    "myself" : 1,
    "namely" : 1,
    "near" : 1,
    "neither" : 1,
    "never" : 1,
    "nevertheless" : 1,
    "next" : 1,
    "no" : 1,
    "nobody" : 1,
    "none" : 1,
    "noone" : 1,
    "nor" : 1,
    "not" : 1,
    "nothing" : 1,
    "now" : 1,
    "nowhere" : 1,
    "of" : 1,
    "off" : 1,
    "often" : 1,
    "on" : 1,
    "once" : 1,
    "one" : 1,
    "oneself" : 1,
    "only" : 1,
    "onto" : 1,
    "or" : 1,
    "other" : 1,
    "others" : 1,
    "otherwise" : 1,
    "ought" : 1,
    "our" : 1,
    "ours" : 1,
    "ourselves" : 1,
    "out" : 1,
    "over" : 1,
    "past" : 1,
    "per" : 1,
    "perhaps" : 1,
    "please" : 1,
    "rather" : 1,
    "re" : 1,
    "regarding" : 1,
    "same" : 1,
    "sans" : 1,
    "seem" : 1,
    "seemed" : 1,
    "seeming" : 1,
    "seems" : 1,
    "several" : 1,
    "shall" : 1,
    "she" : 1,
    "should" : 1,
    "since" : 1,
    "so" : 1,
    "some" : 1,
    "somebody" : 1,
    "somehow" : 1,
    "someone" : 1,
    "something" : 1,
    "sometime" : 1,
    "sometimes" : 1,
    "somewhat" : 1,
    "somewhere" : 1,
    "still" : 1,
    "such" : 1,
    "than" : 1,
    "that" : 1,
    "the" : 1,
    "their" : 1,
    "theirs" : 1,
    "them" : 1,
    "themselves" : 1,
    "then" : 1,
    "thence" : 1,
    "there" : 1,
    "thereafter" : 1,
    "thereby" : 1,
    "therefore" : 1,
    "therein" : 1,
    "thereupon" : 1,
    "these" : 1,
    "they" : 1,
    "this" : 1,
    "those" : 1,
    "though" : 1,
    "through" : 1,
    "throughout" : 1,
    "thru" : 1,
    "thus" : 1,
    "till" : 1,
    "to" : 1,
    "together" : 1,
    "too" : 1,
    "top" : 1,
    "toward" : 1,
    "towards" : 1,
    "under" : 1,
    "underneath" : 1,
    "unless" : 1,
    "until" : 1,
    "up" : 1,
    "upon" : 1,
    "us" : 1,
    "versus" : 1,
    "very" : 1,
    "via" : 1,
    "was" : 1,
    "we" : 1,
    "well" : 1,
    "were" : 1,
    "what" : 1,
    "whatever" : 1,
    "whatsoever" : 1,
    "when" : 1,
    "whence" : 1,
    "whenever" : 1,
    "where" : 1,
    "whereafter" : 1,
    "whereas" : 1,
    "whereby" : 1,
    "wherein" : 1,
    "whereupon" : 1,
    "wherever" : 1,
    "whether" : 1,
    "which" : 1,
    "whichever" : 1,
    "while" : 1,
    "whilst" : 1,
    "whither" : 1,
    "who" : 1,
    "whoever" : 1,
    "whole" : 1,
    "whom" : 1,
    "whose" : 1,
    "why" : 1,
    "will" : 1,
    "with" : 1,
    "within" : 1,
    "without" : 1,
    "would" : 1,
    "yet" : 1,
    "you" : 1,
    "your" : 1,
    "yours" : 1,
    "yourself" : 1,
    "yourselves" : 1
}

import os
import re
import string

def get_file_path(lang):
    folders = DATA_FOLDERS
    paths = []
    for f_path in folders:
        folder = os.listdir(f_path)
        for file in folder:
            target_lang = file[2:4]
            if target_lang == lang:
                paths.append(os.path.join(f_path, file))
    return paths

def count_chart_for_lang(lang, path):
    file = open(path, 'r').read()
    uni_chars = set(file)
    lang_count = LANG_CHAR_COUNT[lang]
    for c in uni_chars:
        if c in LANG_CHAR_COUNT[lang]:
            lang_count[c] = int(lang_count[c]) + file.count(c)
        else:
            lang_count[c] = file.count(c)

def get_en_name_list():
    en_file = open(EN_FILE_PATH, "w+")

    en_punc = string.punctuation
    en_punc = re.sub("[']", '', en_punc) # keep Apostrophe for En
    translator = str.maketrans(en_punc, ' '*len(en_punc))
    translator2 = str.maketrans('', '', string.digits)
    en_set = set(LANG_CHAR_COUNT["En"])

    with open(NAME_LIST_PATH, "r") as name_file:
        for (idx,name) in enumerate(name_file):
            name = name.translate(translator) # convert punctuations into space, except for Apostrophe
            name = name.translate(translator2) # remove digits
            name = name.strip() # remove leading and ending char like \n
            name = name.lower() # to lowercase
            if set(name).issubset(en_set):
                names = name.split(' ')

                for n in names:
                    if len(n) <= 1:
                        continue
                    if n in EN_STOP_WORDS:
                        continue
                    en_file.write("%s\n" % n)

            # if idx == 100:
            #     break

TARGET_LANGS = ['Ta', 'En', 'Th', 'Ka', 'Hi', 'Ba', 'Ch', 'Vi', 'Pe', 'He']
LANG_CHAR_COUNT = {}

for lang in TARGET_LANGS:
    LANG_CHAR_COUNT[lang] = {}
    folder_paths = get_file_path(lang)

    for p in folder_paths:
        target_suffix = ".trg"
        for f in os.listdir(p):
            if f.endswith(target_suffix):
                char_count = count_chart_for_lang(lang, os.path.join(p, f))

get_en_name_list()
