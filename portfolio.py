from dataclasses import dataclass

from position import Position


@dataclass
class Portfolio:
    name: str
    exchange: str
    positions: dict[str,Position]


    def add_position(self, position):
        self.positions[position.symbol] = position

    def remove_position(self, symbol):
        del self.positions[symbol]

    def total_market_value(self) -> float:
        return sum([position.market_value() for position in self.positions.values()])

    def total_cost_basis(self) -> float:
        return sum([position.cost_basis() for position in self.positions.values()])

    def total_unrealized_pnl(self) -> float:
        return sum([position.unrealized_pnl() for position in self.positions.values()])

    def total_percent_change(self) -> float:
        return self.total_unrealized_pnl() / self.total_cost_basis() * 100.0

    def total_bps_change(self) -> float:
        return self.total_unrealized_pnl() / self.total_cost_basis() * 10000.0

