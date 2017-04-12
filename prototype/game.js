var Agent = require('./agent.js');
var Board = require('./board.js');
var Player = require('./player.js');
var common = require('./common.js');
var show = common.show;
var shuffle = require('shuffle-array');

var Game = function(agents) {
    this.playerCount = 0;
    this.players = agents.map(function(agent) {
        var player = new Player(this.playerCount++, agent.name);
        player.agent = agent;
        return player;
    }.bind(this));
    this.board = new Board(this.playerCount);
    this.getMoves = require('./moves.js');
    this.reset();
};

Game.prototype.reset = function(){
    shuffle(this.players);
    this.players.forEach(function(player){
        player.reset();
    });
    this.board.reset();
    this.move = 0;
};

Game.prototype.getCurrentPlayer = function() {
    return this.players[this.move % this.playerCount];
};

// if (process.argv.length < 3) {
//     console.log("usage:", process.argv[1], "<center chips> <player chips>");
//     process.exit();
// }
//var center = Number(process.argv[2]); //23404;
//var player = Number(process.argv[3]); //9362;

var game = new Game([new Agent("John"), new Agent("Steve")]);
var currentPlayer = game.getCurrentPlayer();
var moves = game.getMoves(game.board, currentPlayer);

console.log("currentPlayer", currentPlayer);
console.log("board", game.board);
console.log(show(moves));
console.log("Number of moves:",
    moves.takeChips.length +
    moves.reserve.exposed.length +
    moves.reserve.covered.length +
    moves.purchase.length
);
console.log(show(currentPlayer.agent.makeMove(game.board, game.players, game.move%game.playerCount, moves)));
