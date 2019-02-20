import os
from . import PATH, CONFIG
def initdb():
    os.system("""
    cd app &&
    cat {}/database/schema.sql |
    yasha -v {} - |
    mysql -uroot
    """.format(PATH, CONFIG))
initdb()