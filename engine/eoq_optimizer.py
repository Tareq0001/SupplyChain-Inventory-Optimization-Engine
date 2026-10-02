import numpy as np

class InventoryOptimizationEngine:
    @staticmethod
    def calculate_eoq(annual_demand: float, ordering_cost: float, holding_cost_per_unit: float) -> dict:
        if annual_demand <= 0 or ordering_cost <= 0 or holding_cost_per_unit <= 0:
            raise ValueError("All parameters must be strictly positive.")
            
        eoq = np.sqrt((2.0 * annual_demand * ordering_cost) / holding_cost_per_unit)
        total_orders_per_year = annual_demand / eoq
        annual_order_cost = total_orders_per_year * ordering_cost
        annual_holding_cost = (eoq / 2.0) * holding_cost_per_unit
        total_annual_cost = annual_order_cost + annual_holding_cost
        
        return {
            "optimal_order_quantity_units": round(float(eoq), 2),
            "annual_orders_count": round(float(total_orders_per_year), 2),
            "annual_order_cost": round(float(annual_order_cost), 2),
            "annual_holding_cost": round(float(annual_holding_cost), 2),
            "total_inventory_cost": round(float(total_annual_cost), 2)
        }

    @staticmethod
    def calculate_safety_stock_rop(
        daily_demand_mean: float,
        daily_demand_std: float,
        lead_time_days_mean: float,
        lead_time_days_std: float,
        service_level: float = 0.95
    ) -> dict:
        from scipy.stats import norm
        z = norm.ppf(service_level)
        
        # Combined lead time and demand variance
        variance = (lead_time_days_mean * (daily_demand_std ** 2)) + ((daily_demand_mean ** 2) * (lead_time_days_std ** 2))
        safety_stock = z * np.sqrt(variance)
        reorder_point = (daily_demand_mean * lead_time_days_mean) + safety_stock
        
        return {
            "service_level": service_level,
            "z_factor": round(float(z), 3),
            "safety_stock_units": round(float(safety_stock), 2),
            "reorder_point_units": round(float(reorder_point), 2)
        }
