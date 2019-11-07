#tuple
from collections import namedtuple

patient = namedtuple("patient", ["pid","name","phone", "payment","problem","ward", "docname","date"])
report  = namedtuple("report", ["test_u", "test_r", "dod","pid"])
doctor = namedtuple("doctor",["name","dept","availabity"])
med=namedtuple("med",["med_name","quant","pid"])
login=namedtuple("login",["i_d","name","un","pwd"])
test=namedtuple("test",["pid","name","problem","doc","test_u","test_r","dod"])
update = namedtuple("update", ["name","phone", "payment","problem","ward", "docname","pid"])
med_p=namedtuple("med_p",["pid","name","docname","med","quant"])
