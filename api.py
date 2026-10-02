from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from engine.eoq_optimizer import InventoryOptimizationEngine
from engine.monte_carlo_sim import StockoutSimulator

app = FastAPI(title="Supply Chain Inventory Analytics API", version="1.0.0")

class EOQRequest(BaseModel):
    annual_demand: float
    ordering_cost: float
    holding_cost_per_unit: float

class SafetyStockRequest(BaseModel):
    daily_demand_mean: float
    daily_demand_std: float
    lead_time_days_mean: float
    lead_time_days_std: float
    service_level: float = 0.95

class SimulationRequest(BaseModel):
    daily_demand_mean: float
    daily_demand_std: float
    lead_time_days: int
    starting_stock: float
    n_trials: int = 2000

@app.get("/")
def root():
    return {"service": "Supply Chain Inventory Analytics Engine", "status": "ONLINE"}

@app.post("/optimize/eoq")
def optimize_eoq(req: EOQRequest):
    try:
        return InventoryOptimizationEngine.calculate_eoq(req.annual_demand, req.ordering_cost, req.holding_cost_per_unit)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/optimize/safety-stock")
def optimize_safety_stock(req: SafetyStockRequest):
    return InventoryOptimizationEngine.calculate_safety_stock_rop(
        req.daily_demand_mean, req.daily_demand_std, req.lead_time_days_mean, req.lead_time_days_std, req.service_level
    )

@app.post("/simulate/stockout")
def run_simulation(req: SimulationRequest):
    return StockoutSimulator.simulate_lead_time_cycles(
        req.daily_demand_mean, req.daily_demand_std, req.lead_time_days, req.starting_stock, req.n_trials
    )
