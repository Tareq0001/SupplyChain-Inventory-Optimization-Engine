import numpy as np

class StockoutSimulator:
    @staticmethod
    def simulate_lead_time_cycles(
        daily_demand_mean: float,
        daily_demand_std: float,
        lead_time_days: int,
        starting_stock: float,
        n_trials: int = 5000
    ) -> dict:
        np.random.seed(42)
        total_stockouts = 0
        stockout_quantities = []

        for _ in range(n_trials):
            lead_demand = np.maximum(0, np.random.normal(daily_demand_mean, daily_demand_std, lead_time_days)).sum()
            if lead_demand > starting_stock:
                total_stockouts += 1
                stockout_quantities.append(lead_demand - starting_stock)
            else:
                stockout_quantities.append(0.0)

        prob_stockout = total_stockouts / n_trials
        expected_unmet_demand = np.mean(stockout_quantities)

        return {
            "trials_run": n_trials,
            "stockout_probability": round(float(prob_stockout), 4),
            "fill_rate": round(float(1.0 - prob_stockout), 4),
            "expected_unmet_units": round(float(expected_unmet_demand), 2)
        }
