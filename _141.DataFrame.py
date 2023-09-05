#DataFrame:multi dimensinal tabel
import pandas as pd
a={'paper code':[22,4,567,78,7890],'subject':['maths','automata','IOT','FDS',"CN"]}
a1=pd.DataFrame(a)
print(a1)
print('\n')
print(a1.loc[0])
print('-----------------------')
print(a1.loc[[1,2]])#[] if you add then returns dataframe format result