# WIP: MaiCoin MAX Exchange MCP Server

[MaiCoin MAX API](https://max.maicoin.com/documents/api_list/v3)

## Tools

- get_markets
- get_currencies
- get_accounts
- get_tickers
- submit_order
- cancel_orders

## Usage

From PyPI:
```json
{
  "mcpServers": {
    "maxmcp": {
      "command": "uvx",
      "args": ["maxmcp"],
      "env": {
        "MAX_API_KEY": "",
        "MAX_API_SECRET": ""
      }
    }
  }
}
```

From GitHub repository:
```json
{
  "mcpServers": {
    "maxmcp": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/narumiruna/max-mcp",
        "maxmcp"
      ],
      "env": {
        "MAX_API_KEY": "",
        "MAX_API_SECRET": ""
      }
    }
  }
}
```

## TODO?

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
  - [x] accounts
  - [ ] ad ratio
  - [ ] submit loan
  - [ ] loan history
  - [ ] submit repayment
  - [ ] repayment history
  - [ ] liquidation history
  - [ ] liquidation detail
  - [ ] interest history of your m-wallet
  - [ ] withdraw_addresses
  - [ ] deposit_address
- Order
  - [x] open orders
  - [x] closed orders
  - [ ] order history by order id
  - [x] submit order
  - [x] cancel all orders
  - [ ] order detail
  - [x] cancel an order
- Trade
  - [ ] trade history
  - [ ] trade detail
- Transaction
