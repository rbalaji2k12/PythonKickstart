import pandas as pd
df = pd.read_csv("sec_bhavdata_full.csv")
df.set_index("SYMBOL", inplace = True)

index_set = list(set(df.index.tolist()))

print(index_set.__len__())

for index in range(len(index_set)):
        print(index_set[index])
        result = df.loc[index_set[index]]
        if(index_set[index] == "SGBNOV26"):
            print(result)

