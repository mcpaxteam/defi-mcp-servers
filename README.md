# MCP DeFi Servers

This repository contains a collection of Model Context Protocol (MCP) servers for various DeFi use cases. These servers are built using FastAPI and can be deployed to a decentralized compute platform like 0G/Akash.

## What are MCPs and why are they valuable?

Model Context Protocols (MCPs) are a new paradigm for building decentralized applications. They allow developers to create specialized servers that provide specific data and functionality to dApps. This approach offers several advantages:

*   **Improved Scalability:** By offloading complex computations and data retrieval to specialized MCP servers, dApps can scale more efficiently.
*   **Enhanced Security:** MCP servers can be deployed in secure enclaves, protecting sensitive data and computations from unauthorized access.
*   **Increased Flexibility:** MCPs can be easily customized and updated to meet the evolving needs of dApps.
*   **Quantum-Safe Compute:** MCPs can be configured to use quantum-resistant cryptographic algorithms, protecting dApps from future quantum threats.

## MCP Servers

The following MCP servers are included in this repository:

*   **DeFi Risk:** Provides a DeFi risk score based on input parameters. [README](./defi_risk/README.md)
*   **DAO Voting:** Simulates a DAO voting process and returns the result based on voter weights. [README](./dao_voting/README.md)
*   **NFT Valuation:** Provides an NFT valuation based on input parameters. [README](./nft_valuation/README.md)
*   **Lending Rates:** Provides lending rates based on input parameters. [README](./lending_rates/README.md)
*   **Stablecoin APY:** Provides a stablecoin APY based on input parameters. [README](./stablecoin_apy/README.md)

## Usage

To use these MCP servers, you will need to:

1.  Install Python 3.7+
2.  Install FastAPI and Uvicorn:

    ```bash
    pip install fastapi uvicorn
    ```
3.  Run the server using Uvicorn:

    ```bash
    uvicorn mcp_defi_risk:app --host 0.0.0.0 --port 8000
    ```

    Replace `mcp_defi_risk` with the name of the MCP server you want to run, and adjust the port number accordingly.  See the individual README files for each server for specific instructions.

## Deployment

These MCP servers can be deployed to a decentralized compute platform like 0G/Akash. Refer to the MCPAX documentation for more information on how to deploy MCP servers.

## Contributing

Contributions to this repository are welcome. Please submit a pull request with your changes.
