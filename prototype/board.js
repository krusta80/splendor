var Deck = require('./deck.js');

var Board = function(playerCount) {
	this.playerCount = playerCount;
	this.reset();
};

module.exports = Board;

Board.prototype.reset = function() {
	this.nobles = require('./noble.js');
	this.decks = [new Deck(0), new Deck(1), new Deck(2)];
	this.chips = this.getStartingChips();
};

Board.prototype.getStartingChips = function() {
	var startingChipCounts = [0,0,4,5,7];
	var startingChips = (5<<15);

	for(var colorIndex = 0; colorIndex < 5; colorIndex++){
		startingChips += (startingChipCounts[this.playerCount]<<(3*colorIndex));
	}
	return startingChips;
};

Board.prototype.getExposedCards = function() {
	var exposedCards = [];
	var row = 0;

	this.decks.forEach(function(deck){
		for(var i = 0; i < Math.min(4, deck.cards.length); i++){
			exposedCards.push({
				row: row,
				index: i,
				card: deck.cards[deck.cards.length-i-1]
			});
		}
		row++;
	});
	return exposedCards;
};

Board.prototype.getTopCards = function() {
	var topCards = [];

	this.decks.forEach(function(deck){
		if(deck.cards.length > 4) {
			topCards.push(deck.cards[deck.cards.length-6]);
		} else {
			topCards.push(null);
		}
	});
	return topCards;
};

Board.prototype.removeCard = function(row,index) {
	return decks[row].cards.splice(index,1);
};

Board.prototype.addChips = function(chips) {
	this.chips += chips;
};

Board.prototype.removeChips = function(chips) {
	this.chips -= chips;
};
