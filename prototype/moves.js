const util = require('util')
var chips = require('./chipMoves.js');
var translateChipCount = chips.translateChipCount;
var getChipTakingOptions = chips.getChipTakingOptions;
var common = require('./common.js');
var Board = require('./board.js');
var Player = require('./player.js');

if (process.argv.length < 3) {
    console.log("usage:", process.argv[1], "<center chips> <player chips>");
    process.exit();
}
var center = Number(process.argv[2]); //23404;
var player = Number(process.argv[3]); //9362;
var chipTakingOptions = getChipTakingOptions(center, player);
var players = [new Player(0,"Player A"), new Player(1,"Player B")];
var board = new Board(2);

console.log(board);
