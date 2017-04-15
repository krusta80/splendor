var zerorpc = require("zerorpc");
var Agent = require('./agent.js');
var Game = require('./game.js');
var show = require('./common.js').show;
var sleep = require('sleep');

var game;	//	out here to avoid circular references
var rpc; 	//  out here to avoid circular references

const SLEEP =     10;		// set to 10ms for now
const TIMEOUT = 2000;		// set to 1s for now

var server = new zerorpc.Server({
    resetRPC: function() {
    	return {
	    	id: 0,
	    	clientMove: null,
	    	gameState: null
	    }
    },
    newSession: function(name, numberOfOpponents, reply) {
        this.name = name.toString();
        this.nextResponse = null;
        var agents = [this];
        console.log(show(this));
        for(var i = 0; i < numberOfOpponents; i++){
        	agents.push(new Agent("Opponent "+(i+1)));
        }
        game = new Game(agents);
        rpc = this.resetRPC();
        //console.log(JSON.stringify(game.getGameState()));
        reply(null, JSON.stringify(game.getGameState()));
    },
    newGame: function(reply) {
    	game.reset();
    	this.getGameState(reply);
    	//reply(null, "New game started...");
    },
    tellAgentGameIsOver: function(board, players, playerIndex, moves, thisAgentDidWin) {
    	rpc.gameState = game.getGameState();
    },
    makeMove: function(board, players, playerIndex, moves) {
    	//	Called by Game.
    	var moveMade;

    	console.log("making move...");
    	rpc.gameState = game.getGameState();
    	this.waitFor(rpc.clientMove, "client");
    	moveMade = rpc.clientMove;
    	rpc.clientMove = null;
    	rpc.gameState = null;
    	return moveMade;
    },
    sendMove: function(move, reply) {
    	//	"send" is from the client's perspective
    	rpc.clientMove = move;
    	this.waitFor(rpc.gameState, "server");
    	reply(null, JSON.stringify(rpc.gameState));
    },
    getGameState: function(reply) {
    	// "get" is from the client's perspective
    	console.log("getting game state...");
    	this.waitFor(rpc.gameState, "server");
    	reply(null, JSON.stringify(rpc.gameState));
    },
    waitFor: function(action, clientOrServer) {
    	var timeout = 0;

    	while(timeout < TIMEOUT && action == null) {
    		sleep.msleep(SLEEP);
    		timeout += SLEEP;
    	}
    	if(action == null) {
    		console.log("ERROR:  Timeout reached (" + clientOrServer + ")!");
    		process.exit(-1);
    	}
    }
});

server.bind("tcp://0.0.0.0:4242");
console.log("Listening on port 4242...");

