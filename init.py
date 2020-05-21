import os
for o in ['data','data/livres','img']:
    os.mkdir(o)
for o in ['authors','reservation','title']:
    open(o,'x')