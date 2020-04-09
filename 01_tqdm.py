

from tqdm import tqdm
import pandas as pd
import numpy as np

# from tqdm.notebook import tqdm # notebook에서 사용할 때는 tqdm.notebook도 가능

for i in tqdm(range(100)):
    pass

a = list()
for i in tqdm(range(1000000), desc = "progress ... : "):
    a.append(i)
        
df = pd.DataFrame(np.array(a).reshape(1000,1000))
tqdm.pandas(desc = "progress ... : ")
df.progress_apply(lambda x: x*10)


