from dataclasses import dataclass


@dataclass
class Position:
    symbol: str
    quantity: int
    average_price: float
    current_price: float

    def market_value(self) -> float:
        return self.quantity * self.current_price

    def cost_basis(self) -> float:
        return self.quantity * self.average_price

    def unrealized_pnl(self) -> float:
        return self.market_value() - self.cost_basis()

    def percent_change(self) -> float:
        return (self.current_price - self.average_price) / self.average_price * 100.0
    
    def bps_change(self) -> float:
        return (self.current_price - self.average_price) / self.average_price * 10000.0
    
    def update_position(self, quantity, average_price, current_price):
        self.quantity = quantity
        self.average_price = average_price
        self.current_price = current_price
