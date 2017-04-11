const util = require('util')
var chips = require('./chipMoves.js');
var translateChipCount = chips.translateChipCount;
var getChipTakingOptions = chips.getChipTakingOptions;
var Deck = require('./deck.js');
var nobles = require('./noble.js');
var common = require('./common.js');
var Player = require('./player.js');

if (process.argv.length < 3) {
    console.log("usage:", process.argv[1], "<center chips> <player chips>");
    process.exit();
}
var center = Number(process.argv[2]); //23404;
var player = Number(process.argv[3]); //9362;
var chipTakingOptions = getChipTakingOptions(center, player);
var decks = [new Deck(0), new Deck(1), new Deck(2)];
var players = [new Player(0,"Player A"), new Player(1,"Player B")];

// console.log(util.inspect(decks, false, null));
// console.log("Center chips:", common.translateChipCount(center));
// console.log("Player chips:", common.translateChipCount(player));
// console.log("Chip Moves  :", chipTakingOptions);
// console.log("Nobles      :", nobles.map(common.translateChipCount));

var ctr = 0;
var lastCount = 0;
var gold = 5;
while(ctr++ < 500 && players[0].purchasedCards.length < 3){
	if(players[0].reservedCards.length){
		players[0].activateCard(players[0].reservedCards[0]);
		console.log("XXXXXXX");	
	}
	console.log(players[0]);
	players[0].addChips(1<<(3*Math.floor(Math.random()*5)));
	players[0].buyCard(decks[0].cards[0]);
	if(players[0].purchasedCards.length > lastCount){
		console.log("*******");
		decks[0].cards.shift();
		players[0].reserveCard(decks[0].cards.pop(), gold--);
	}
	lastCount = players[0].purchasedCards.length;
	console.log(players[0]);
}
