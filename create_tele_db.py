import pickle
dict1={12345:'John',56478:'Arun',21458:'Bala',121357:['Fred','smith']}
pickle_out = open("dict.pickle","wb")
pickle.dump(dict1, pickle_out)
pickle_out.close()