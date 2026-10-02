from engine.eoq_optimizer import InventoryOptimizationEngine
from engine.monte_carlo_sim import StockoutSimulator

def run_supply_chain_pipeline():
    print("=" * 64)
    print("   SUPPLY CHAIN INVENTORY & STOCHASTIC OPTIMIZATION ENGINE     ")
    print("=" * 64)

    # 1. Economic Order Quantity
    eoq_res = InventoryOptimizationEngine.calculate_eoq(
        annual_demand=24000.0,
        ordering_cost=150.0,
        holding_cost_per_unit=4.50
    )
    print("\n[1] EOQ Economic Cost Curve Result:")
    for k, v in eoq_res.items():
        print(f"  --> {k}: {v}")

    # 2. Safety Stock & Reorder Point
    rop_res = InventoryOptimizationEngine.calculate_safety_stock_rop(
        daily_demand_mean=80.0,
        daily_demand_std=15.0,
        lead_time_days_mean=10.0,
        lead_time_days_std=2.0,
        service_level=0.98
    )
    print("\n[2] Stochastic Safety Stock & ROP (98% Service Level):")
    for k, v in rop_res.items():
        print(f"  --> {k}: {v}")

    # 3. Monte Carlo Stockout Risk
    sim_res = StockoutSimulator.simulate_lead_time_cycles(
        daily_demand_mean=80.0,
        daily_demand_std=15.0,
        lead_time_days=10,
        starting_stock=rop_res["reorder_point_units"],
        n_trials=5000
    )
    print("\n[3] Monte Carlo Stockout Simulation Verification:")
    for k, v in sim_res.items():
        print(f"  --> {k}: {v}")

    print("\n" + "=" * 64)
    print("         SUPPLY CHAIN ANALYTICS BENCHMARK COMPLETE (100%)       ")
    print("=" * 64)

if __name__ == "__main__":
    run_supply_chain_pipeline()
