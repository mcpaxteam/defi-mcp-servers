from fastapi import FastAPI, Query
from typing import Optional
import random

app = FastAPI(
    title="MCP NFT Valuation",
    description="A simple MCP server that provides an NFT valuation based on input parameters.",
    version="0.1.0",
)

@app.get("/mcp/nft/valuation")
async def get_nft_valuation(
    rarity_score: float = Query(..., description="The rarity score of the NFT."),
    market_cap: float = Query(..., description="The market capitalization of the NFT collection."),
    trading_volume: float = Query(..., description="The trading volume of the NFT."),
    artist_reputation: Optional[float] = Query(None, description="The reputation score of the artist.")
):
    """
    Calculates an NFT valuation based on the provided parameters.
    """

    # Basic valuation calculation (replace with a more sophisticated model)
    valuation = (rarity_score * 0.3 + market_cap * 0.4 + trading_volume * 0.3) * random.uniform(0.8, 1.2)

    # Adjust valuation based on artist reputation (if available)
    if artist_reputation is not None:
        valuation *= (1 + artist_reputation * 0.1)

    return {
        "valuation": valuation,
        "rarity_score": rarity_score,
        "market_cap": market_cap,
        "trading_volume": trading_volume,
        "artist_reputation": artist_reputation,
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
