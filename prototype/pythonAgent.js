var zerorpc = require("zerorpc");
var Agent = require('./agent.js');
var Game = require('./game.js');
var show = require('./common.js').show;
var sleep = require('sleep');

var game;	//	out here to avoid circular references

const SLEEP =     10;		// set to 10ms for now
const TIMEOUT = 2000;		// set to 1s for now

var server = new zerorpc.Server({
    newSession: function(name, numberOfOpponents, reply) {
        this.name = name.toString();
        this.nextResponse = null;
        var agents = [this];
        console.log(show(this));
        for(var i = 0; i < numberOfOpponents; i++){
        	agents.push(new Agent("Opponent "+(i+1)));
        }
        game = new Game(agents);
        reply(null, JSON.stringify(game.getGameState()));
    },
    newGame: function(reply) {
    	game.reset();
    	game.playUntilPlayerId(0);		//	we are always id 0
    	console.log(game.getGameState().moves);
    	reply(null, JSON.stringify(game.getGameState()));
    },
    makeMove: function(board, players, playerIndex, moves) {
    	//	NEVER CALLED AS CURRENTLY DESIGNED
    },
    sendMove: function(move, reply) {
    	//	"send" is from the client's perspective
    	console.log("Chosen move is", move);
    	game.executeDecision(move);
    	game.move++;
    	game.playUntilPlayerId(0);
    	reply(null, JSON.stringify(game.getGameState()));
    }
});

server.bind("tcp://0.0.0.0:4242");
console.log("Listening on port 4242...");

