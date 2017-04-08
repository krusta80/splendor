const util = require('util')
var chips = require('./chipMoves.js');
var translateChipCount = chips.translateChipCount;
var getChipTakingOptions = chips.getChipTakingOptions;
var Deck = require('./deck.js');
var nobles = require('./noble.js');
var common = require('./common.js');

if(process.argv.length < 3){
	console.log("usage:", process.argv[1], "<center chips> <player chips>");
	process.exit();
}
var center = process.argv[2];//23404;
var player = process.argv[3];//9362;
var chipTakingOptions = getChipTakingOptions(center, player);
var decks = [new Deck(0), new Deck(1), new Deck(2)];

console.log(util.inspect(decks, false, null));
console.log("Center chips:", common.translateChipCount(center));
console.log("Player chips:", common.translateChipCount(player));
console.log("Chip Moves  :", chipTakingOptions);
console.log("Nobles      :", nobles.map(common.translateChipCount));
