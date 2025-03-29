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
  - [x] get all available markets.
  - [x] getApiV3Currencies
  - [ ] getApiV3Timestamp
  - [ ] getApiV3K
  - [ ] getApiV3Depth
  - [ ] getApiV3Trades
  - [x] v2 tickers
  - [x] v3 ticker
- Wallet
- Order
  - [x] open orders
  - [x] closed orders
  - [ ] order history by order id
  - [x] submit order
  - [ ] cancel all orders
  - [ ] order detail
  - [ ] cancel an order
- Trade
- Transaction
