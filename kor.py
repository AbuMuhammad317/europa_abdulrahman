# KÖR: hela flödet i ordning. Starta med "python kor.py".
from hamta import hamta_data
from rensa import rensa_data
from spara import spara_data

# Arbetslöshet i procent av arbetskraften, 25-74 år, båda könen.
bred = hamta_data("une_rt_a", {"sex": ["T"], "age": ["Y25-74"], "unit": ["PC_ACT"]})
lang = rensa_data(bred)
spara_data(lang, "arbetsloshet")
