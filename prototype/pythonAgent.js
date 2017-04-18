var zerorpc = require("zerorpc");
var Agent = require('./agent.js');
var Game = require('./game.js');
var show = require('./common.js').show;
var sleep = require('sleep');

var buildMoveResponse = require('./protoFuncs').buildMoveResponse;
var decodeMove = require('./protoFuncs').decodeMove;

var fs = require('fs'); // temp for testing
var protobuf = require("protobufjs");  // temp for testing
var Splendor;
protobuf.load("../splendor.proto")
    .then(function(root) {
       Splendor = root;
       console.log(Splendor);
    });

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
        reply(null, "Welcome, " + name + "!");
    },
    newGame: function(reply) {
    	game.reset();
    	var gameStates = game.playUntilPlayerId(0);		//	we are always id 0
    	if(gameStates.length === 0) {
            gameStates = [game.getGameState(0)];
        }
        // console.log(
        //     Splendor.SplendorService.MoveResponse
        //         .decode(buildMoveResponse(gameStates)));
        reply(null, buildMoveResponse(gameStates));
    },
    makeMove: function(board, players, playerIndex, moves) {
    	//	NEVER CALLED AS CURRENTLY DESIGNED
    },
    sendMove: function(moveRequest, reply) {
    	//	"send" is from the client's perspective
    	game.executeDecision(decodeMove(move));
    	game.move++;
    	var gameStates = [game.getGameState(0)].concat(game.playUntilPlayerId(0));
    	reply(null, buildMoveResponse(gameStates));
    }
});

server.bind("tcp://0.0.0.0:4242");
console.log("Listening on port 4242...");

