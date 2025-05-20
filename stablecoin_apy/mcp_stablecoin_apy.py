from fastapi import FastAPI, Query
from typing import Optional
import random

app = FastAPI(
    title="MCP Stablecoin APY",
    description="A simple MCP server that provides a stablecoin APY based on input parameters.",
    version="0.1.0",
)

@app.get("/mcp/defi/stablecoin_apy")
async def get_stablecoin_apy(
    stablecoin_name: str = Query(..., description="The name of the stablecoin (e.g., USDT, USDC)."),
    deposit_amount: float = Query(..., description="The amount of stablecoin being deposited."),
    lockup_period: int = Query(..., description="The lockup period in days."),
    platform_risk: Optional[float] = Query(None, description="The risk score of the platform offering the APY.")
):
    """
    Calculates a stablecoin APY based on the provided parameters.
    """

    # Basic APY calculation (replace with a more sophisticated model)
    base_apy = 0.02  # 2% base APY
    apy = base_apy + (deposit_amount / 100000) * 0.005 + (lockup_period / 365) * 0.01

    # Adjust APY based on platform risk
    if platform_risk is not None:
        apy -= platform_risk * 0.002

    # Ensure the APY is within a reasonable range
    apy = max(0.01, min(apy, 0.15))

    return {
        "stablecoin_apy": apy,
        "stablecoin_name": stablecoin_name,
        "deposit_amount": deposit_amount,
        "lockup_period": lockup_period,
        "platform_risk": platform_risk,
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004)
