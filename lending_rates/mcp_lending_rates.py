from fastapi import FastAPI, Query
from typing import Optional
import random

app = FastAPI(
    title="MCP Lending Rates",
    description="A simple MCP server that provides lending rates based on input parameters.",
    version="0.1.0",
)

@app.get("/mcp/defi/lending_rate")
async def get_lending_rate(
    collateral_type: str = Query(..., description="The type of collateral being used (e.g., ETH, BTC)."),
    loan_duration: int = Query(..., description="The duration of the loan in days."),
    loan_amount: float = Query(..., description="The amount of the loan."),
    market_conditions: Optional[str] = Query(None, description="The current market conditions (e.g., bullish, bearish).")
):
    """
    Calculates a lending rate based on the provided parameters.
    """

    # Basic lending rate calculation (replace with a more sophisticated model)
    base_rate = 0.05  # 5% base rate
    rate = base_rate + (loan_duration / 365) * 0.02 + (loan_amount / 100000) * 0.01

    # Adjust rate based on collateral type
    if collateral_type == "ETH":
        rate -= 0.005
    elif collateral_type == "BTC":
        rate -= 0.0025

    # Adjust rate based on market conditions
    if market_conditions == "bullish":
        rate -= 0.005
    elif market_conditions == "bearish":
        rate += 0.01

    # Ensure the rate is within a reasonable range
    rate = max(0.01, min(rate, 0.20))

    return {
        "lending_rate": rate,
        "collateral_type": collateral_type,
        "loan_duration": loan_duration,
        "loan_amount": loan_amount,
        "market_conditions": market_conditions,
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8003)
