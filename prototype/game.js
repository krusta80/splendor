const util = require('util')
var common = require('./common.js');
var Board = require('./board.js');
var Player = require('./player.js');

var Game = function(playerNames) {
	this.playerCount = 0;
	this.players = playerNames.map(function(playerName){
		return new Player(this.playerCount++, playerName);
	}.bind(this));
	this.board = new Board(this.playerCount);
	this.move = 0;
	this.getMoves = require('./moves.js');
};

Game.prototype.getNextPlayer = function(){
	return this.players[this.move%this.playerCount];
};

// if (process.argv.length < 3) {
//     console.log("usage:", process.argv[1], "<center chips> <player chips>");
//     process.exit();
// }
//var center = Number(process.argv[2]); //23404;
//var player = Number(process.argv[3]); //9362;

var game = new Game(["John", "Steve"]);
var currentPlayer = game.getNextPlayer();
var moves = game.getMoves(game.board, currentPlayer);

console.log("currentPlayer", currentPlayer);
console.log("board", game.board);
console.log(util.inspect(moves, false, null));
console.log("Number of moves:", 
	moves.takeChips.length + 
	moves.reserve.exposed.length + 
	moves.reserve.covered.length + 
	moves.purchase.length
);
