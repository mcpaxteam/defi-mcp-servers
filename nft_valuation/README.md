# MCP NFT Valuation Server

This MCP server provides an NFT valuation based on input parameters such as rarity score, market cap, and trading volume.

## Purpose

The purpose of this MCP server is to provide a simple and easily accessible way to estimate the value of an NFT. This can be used by NFT collectors and investors to make more informed decisions.

## Usage

To use this MCP server, you will need to:

1.  Install Python 3.7+
2.  Install FastAPI and Uvicorn:

    ```bash
    pip install fastapi uvicorn
    ```
3.  Run the server using Uvicorn:

    ```bash
    uvicorn mcp_nft_valuation:app --host 0.0.0.0 --port 8002
    ```

4.  Send a GET request to the `/mcp/nft/valuation` endpoint with the following query parameters:

    *   `rarity_score`: The rarity score of the NFT.
    *   `market_cap`: The market capitalization of the NFT collection.
    *   `trading_volume`: The trading volume of the NFT.
    *   `artist_reputation` (optional): The reputation score of the artist.

    Example:

    ```
    http://localhost:8002/mcp/nft/valuation?rarity_score=0.9&market_cap=1000000&trading_volume=10000&artist_reputation=0.7
    ```

5.  The server will return a JSON response containing the valuation and the input parameters.

## Example Response

```json
{
    "valuation": 850.0,
    "rarity_score": 0.9,
    "market_cap": 1000000,
    "trading_volume": 10000,
    "artist_reputation": 0.7
}
