import matplotlib.pyplot as plt
import pandas as pd

def plot_daily_calories(meals):
    df = pd.DataFrame([m.to_dict() for m in meals])
    df["date"] = pd.to_datetime(df["date"])
    daily = df.groupby("date")["calories"].sum()

    plt.figure(figsize=(10, 5))
    daily.plot(kind="line", marker="o", color="tomato")
    plt.title("일별 칼로리 섭취량")
    plt.ylabel("칼로리")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
