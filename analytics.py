import pandas as pd
from matplotlib import pyplot as plt

from file_loader import load_orders_from_csv
from main import OrderItem


def convert_orders_to_list_of_dict(orders: list[OrderItem]) -> list[dict]:
    return [item.to_dict() for item in orders]


def convert_orders_to_summary(orders: list[dict]) -> pd.DataFrame:
    """
    Converts a list of orders to a summary of Pandas DataFrame records
    :param orders:
    :return:
    """
    df = pd.DataFrame(orders)

    summary = df.groupby("customer")["total_cost"].agg(["sum", "mean", "count"]).reset_index()
    summary.columns = ["Customer", "Total amount, UAH", "Average amount, UAH", "Number of orders"]

    return summary


def store_summary_to_csv(summary: pd.DataFrame, output_csv: str) -> None:
    """
    Stores a summary as an output CSV file
    :param summary:
    :param output_csv:
    :return:
    """
    summary.to_csv(output_csv, index=False, encoding="utf-8")


def visualize_summary_to_png(summary: pd.DataFrame, output_png: str) -> None:
    """
    Visualizes a summary as a PNG sales chart file
    :param summary:
    :param output_png:
    :return:
    """
    plt.figure(figsize=(10, 6))
    bars = plt.bar(summary["Customer"], summary["Total amount, UAH"], align="center", color="#1A365D")

    plt.title("Sales report (UAH)", fontsize=14)
    plt.xlabel("Customer", fontsize=12)
    plt.ylabel("Total amount, UAH", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    for bar in bars:
        y_value = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, y_value + 100, f"{y_value:.2f}", ha="center", va="bottom", fontsize=12)
    plt.tight_layout()
    plt.savefig(output_png, format="png", dpi=150)
    plt.close()


def run_sales_report_analytics(input_csv: str, output_csv: str, output_png: str) -> None:
    """
    Runs sales report analytics:
    - store summary to csv report file
    - visualize summary to png sales chart file
    :param input_csv:
    :param output_csv:
    :param output_png:
    :return:
    """
    order_items = load_orders_from_csv(input_csv)
    orders = convert_orders_to_list_of_dict(order_items)
    print(f"Total number of orders: {len(orders)}")

    summary = convert_orders_to_summary(orders)
    store_summary_to_csv(summary, output_csv)
    print(f"Summary written to {output_csv}")

    visualize_summary_to_png(summary, output_png)
    print(f"Summary plotted on {output_png}")


if __name__ == "__main__":
    run_sales_report_analytics("sales.csv", "sales_report.csv", "sales_report.png")