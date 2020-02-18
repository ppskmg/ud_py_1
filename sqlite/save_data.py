import rtsql
from get_data import get_data



db_name = rtsql.create('data_set',  
												magnitude='real',
												place='text')

																						
rtsql.insert(db_name, get_data())




