# mcp-server-max

[MaiCoin MAX API](https://max.maicoin.com/documents/api_list/v3)

### GitHub

```json
{
  "mcpServers": {
    "mcp-server-max": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/narumiruna/mcp-server-max",
        "mcp-server-max"
      ]
    }
  }
}
```

### Local

```json
{
  "mcpServers": {
    "mcp-server-max": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/home/<user>/workspace/mcp-server-max",
        "mcp-server-max"
      ]
    }
  }
}
```

## TODO

- Public API
  - [ ] index prices
  - [ ] historical index prices
  - [ ] available loan amount
  - [ ] interest rates
  - [ ] get all available markets.
  - [ ] getApiV3Currencies
  - [ ] getApiV3Timestamp
  - [ ] getApiV3K
  - [ ] getApiV3Depth
  - [ ] getApiV3Trades
  - [ ] getApiV3Tickers
- Wallet
- Order
- Trade
- Transaction
