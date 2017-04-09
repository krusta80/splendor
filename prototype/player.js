var Player = function(id, name) {
    this.id = id;
    this.name = name;
    this.reset();
};

Player.prototype.reset = function() {
    this.purchasedCards = [];
    this.cardChipValues = [0, 0, 0, 0, 0];
    this.points = 0;
    this.reservedCards = [];
    this.chips = 0;
    this.chipsAndCards = 0;
};

Player.prototype.buyCard = function(card) {
    if (card.buy(this.id, this.chipsAndCards)) {
        this.payForCard(card);
        this.purchasedCards.push(card);
    }
};

Player.prototype.payForCard = function(card) {
    var chipTotal = this.chips;
    var goldChipsNeeded = 0;

    for (var colorIndex = 0; colorIndex < 5; colorIndex++) {
        var colorBalanceAfterCards =
            Math.max(0, ((card.cost >> (3 * colorIndex)) & 3) - this.cardChipValues[colorIndex]);
        
        this.chips = (this.chips & (((1 << 18) - 1) - (3 << (3 * colorIndex)))) + 
        				Math.max(0, (chipTotal & 3) - colorBalanceAfterCards);        
        goldChipsNeeded += Math.max(0,  colorBalanceAfterCards - (chipTotal & 3));
        chipTotal = chipTotal >> 3;
    }
    this.chips -= (goldChipsNeeded << 15);
};
