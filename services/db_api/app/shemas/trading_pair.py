from pydantic import BaseModel

class TradingPairIn(BaseModel):
    symbol: str
    ref: str
    spot:bool
    inverse:bool
    linear:bool
    option:bool
    base_coin: str
    quote_coin: str
    contract_type: str
    use: bool