import pandas as pd


def getData():
    df = pd.read_csv("sample-data/website-data.csv", delimiter=",")
    df = df[["Session source", "Users", "Sessions"]]
    return df


def main():
    df = getData()

    # get FB rows
    fb_rows = df[df["Session source"].str.match(".*facebook.*|.*fb.*")]
    # drop them from the original df
    df = df.drop(fb_rows.index)

    fb_rows = fb_rows.reset_index()

    df.loc[0, :] = fb_rows.sum()
    df.sort_values(by=["Users"], ascending=False, inplace=True)

    print(df)

    # df.to_csv("sample-data/website-data-processed.csv", index=False)


main()
