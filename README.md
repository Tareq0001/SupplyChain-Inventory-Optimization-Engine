# SupplyChain-Inventory-Optimization-Engine 📦⚡

An enterprise-grade Operations Research & Inventory Analytics MVP. Computes optimal Economic Order Quantity (EOQ), stochastic safety stock with lead-time demand variance, and runs Monte Carlo stockout risk simulations.

## Mathematical Foundations
1. **Classic & Multi-Echelon EOQ:**
   $$Q^* = \sqrt{\frac{2 D S}{H}}$$
   Where $D$ = Annual Demand, $S$ = Ordering Cost, $H$ = Annual Holding Cost per unit.
2. **Stochastic Safety Stock & Reorder Point (ROP):**
   $$SS = Z_{\alpha} \cdot \sqrt{L \cdot \sigma_D^2 + D_{avg}^2 \cdot \sigma_L^2}$$
   $$ROP = (D_{avg} \cdot L_{avg}) + SS$$
3. **Monte Carlo Inventory Depletion Simulation:**
   Stochastic lead-time demand simulation under Poisson/Gaussian arrival distributions.

## MVP Interface
- **CLI Suite:** `python main.py`
- **REST API:** `uvicorn api:app --reload` (Endpoints: `/optimize`, `/simulate-stockout`)
