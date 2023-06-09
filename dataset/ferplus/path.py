import pandas as pd
import os

# 1: active, 0: fatigue

def labeling(dirpath, mode):
    df = pd.DataFrame(columns=["path"])
    for dir, _, files in os.walk(dirpath):
        for file in files:
            img_path = os.path.relpath(os.path.join(dir, file), start="data\FERPlus")
            df.loc[len(df.index)] = [img_path]
    df.to_csv(f"data\\FERPlus\\ferplus\\{mode}.csv", index=False)

if __name__ == "__main__":
    labeling("data\\FERPlus\\ferplus\\images\\train", mode="train")
    labeling("data\\FERPlus\\ferplus\\images\\val", mode="val")