def print_metrics(metrics):
    """
    Print model evaluation metrics.
    """

    print("\nModel Performance")
    print("-" * 30)

    for metric, value in metrics.items():
        print(f"{metric}: {value:.4f}")