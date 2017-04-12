var Agent = function(name) {
    this.name = name;
};

module.exports = Agent;

Agent.prototype.makeMove = function(board, players, playerIndex, moves) {
    //	For now, we have a random bot.
    if (moves.purchase.length) {
        return {
            label: "PURCHASE",
            action: moves.purchase[0]
        };
    }
    var moveTypes = [moves.takeChips, moves.reserve.exposed, moves.reserve.covered];
    var moveLabels = ["TAKE", "RESERVE_EXPOSED", "RESERVE_COVERED"]
    var totalMoves = moveTypes.reduce(function(a, b) {
        return a + b.length; }, 0);
    var rand = Math.random() * totalMoves;
    var i = -1;

    while (rand > 0) {
        rand -= moveTypes[++i].length;
    }
    return {
        label: moveLabels[Math.min(i, 2)],
        action: moveTypes[Math.min(i, 2)][Math.floor(Math.random() * moveTypes[Math.min(i, 2)].length)]
    };
};

Agent.prototype.takeNoble = function(nobles) {
	//  For now, we just take the first available noble.
	return 0;
};
