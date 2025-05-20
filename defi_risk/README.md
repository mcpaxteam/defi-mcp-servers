# MCP DeFi Risk Server

This MCP server provides a DeFi risk score based on input parameters such as collateral ratio, liquidity, and volatility.

## Purpose

The purpose of this MCP server is to provide a simple and easily accessible way to assess the risk of a DeFi position. This information can be used by DeFi users to make more informed decisions about their investments.

## Usage

To use this MCP server, you will need to:

1.  Install Python 3.7+
2.  Install FastAPI and Uvicorn:

    ```bash
    pip install fastapi uvicorn
    ```
3.  Run the server using Uvicorn:

    ```bash
    uvicorn mcp_defi_risk:app --host 0.0.0.0 --port 8000
    ```

4.  Send a GET request to the `/mcp/defi/risk` endpoint with the following query parameters:

    *   `collateral_ratio`: The collateral ratio of the DeFi position.
    *   `liquidity`: The liquidity of the underlying asset.
    *   `volatility`: The volatility of the underlying asset.
    *   `market_cap` (optional): The market capitalization of the underlying asset.

    Example:

    ```
    http://localhost:8000/mcp/defi/risk?collateral_ratio=0.8&liquidity=0.9&volatility=0.2&market_cap=1000000000
    ```

5.  The server will return a JSON response containing the DeFi risk score and the input parameters.

## Example Response

```json
{
    "risk_score": 65.23,
    "collateral_ratio": 0.8,
    "liquidity": 0.9,
    "volatility": 0.2,
    "market_cap": 1000000000
}
