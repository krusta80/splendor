var Card = function(color, points, cost, tier) {
    this.color = color;
    this.points = points;
    this.cost = cost;
    this.tier = tier;
    this.owner = -1;
    this.isReserved = false;
};

module.exports = Card;

Card.prototype.buy = function(player, chips) {
    return this.canBeBought(chips) && this.possess(player);
};

Card.prototype.reserve = function(player) {
    if (this.possess(player)) {
        this.isReserved = true;
        return true;
    }
};

Card.prototype.activate = function() {
    if (!this.isReserved) {
        console.log("Error:  This card is not currently reserved.", this.owner);
        return false;
    }
    this.isReserved = false;
    return true;
};

Card.prototype.possess = function(player) {
    if (this.owner != -1 && (this.owner != player || !this.isReserved)) {
        console.log("Error:  This card cannot be transfered.", this.owner);
        return false;
    }
    this.owner = player;
    return true;
};

Card.prototype.canBeBought = function(chips) {
    var numberOfChipsShortBy = 0;

    for (var colorIndex = 0; colorIndex < 5; colorIndex++) {
        numberOfChipsShortBy += Math.max(0, ((this.cost >> (3 * colorIndex)) & 7) - (chips & 7));
        chips = chips >> 3;
    }
    return (chips & 7) >= numberOfChipsShortBy;
};
