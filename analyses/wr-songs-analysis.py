import pandas as pd


def getData():
    df = pd.read_csv("sample-data/wr-songs.csv", delimiter=",")
    # set NaN clip rows to empty string
    df.loc[df["Clip"].isnull(), "Clip"] = ""
    # map Retired rows to bool
    df.loc[df["Retired"].isna(), "Retired"] = False
    df.loc[df["Retired"] == 1, "Retired"] = True
    return df


def main():
    df = getData()
    print(df)

    # get ones that most need a clip
    needs_clip = df.loc[(df["Clip"] == "") & (df["Retired"] != 1), ["Song", "Artist"]]
    print(needs_clip)

    # group by decade
    print(df["Decade", "Song"].groupby("Decade", sort=True).count())

    # group by artist
    # grouped = df.groupby("Artist", sort=True).count()
    # print(grouped)
    # print(grouped.loc[df["Song"] > 1])


main()
