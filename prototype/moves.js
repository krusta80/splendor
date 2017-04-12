const util = require('util')
var ChipMoves = require('./chipMoves.js');

var getChipTakingOptions = ChipMoves.getChipTakingOptions;

module.exports = function(board, player) {
	var exposedCards = board.getExposedCards();

	return {
		takeChips : getChipTakingOptions(board.chips, player.chips),
		reserve   : getReserveOptions(
						exposedCards, board.getTopCards(), board.chips,
						player.reservedCards, player.chips
						),
		purchase  : getPurchaseOptions(exposedCards, player.chipsAndCards)
	};
};

function getReserveOptions(exposedCards, topCards, boardChips, reservedCards, playerChips) {
	var reserveChipOptions = ChipMoves.getReserveOptions(boardChips, playerChips);
	var options = {
		exposed : [],
		covered : []
	};

	if(reservedCards.length === 3){
		return null;
	}
	exposedCards.forEach(function(card){
		reserveChipOptions.forEach(function(option){
			options.exposed.push({
				card  : card,
				chips : option
			});
		});
	});
	topCards.forEach(function(card){
		reserveChipOptions.forEach(function(option){
			options.covered.push({
				card  : card,
				chips : option
			});
		});
	});
	return options;
}

function getPurchaseOptions(exposedCards, playerChipsAndCards) {
	return exposedCards.filter(function(card){
		return card.card.canBeBought(playerChipsAndCards);
	});
}
