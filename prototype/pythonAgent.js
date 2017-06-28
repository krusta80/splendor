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
   });

var game;	//	out here to avoid circular references

const SLEEP =     10;		// set to 10ms for now
const TIMEOUT = 2000;		// set to 1s for now

var playTime = 0;
var buildTime = 0;
var transmitTime = 0;
var tic;
var TIC;
var gameCount = 0;

var server = new zerorpc.Server({
    newSession: function(name, numberOfOpponents, reply) {
        this.name = name.toString();
        this.nextResponse = null;
        var agents = [this];
        for(var i = 0; i < numberOfOpponents; i++){
        	agents.push(new Agent("Opponent "+(i+1)));
        }
        game = new Game(agents);
        reply(null, "Welcome, " + name + "!");
    },
    newGame: function(reply) {
        if(gameCount++ % 100 == 0) {
            console.log(playTime, buildTime, transmitTime, 100/(Date.now()-TIC));
            TIC = Date.now();
        }
        game.reset();
        tic = Date.now();
    	var gameStates = game.playUntilPlayerId(0);		//	we are always id 0
    	playTime += Date.now() - tic;
        if(gameStates.length === 0) {
            gameStates = [game.getGameState(0)];
        }
        tic = Date.now();
        var resp = buildMoveResponse(gameStates);
        buildTime += Date.now() - tic;
        tic = Date.now();
        reply(null, resp);
        //
    },
    makeMove: function(board, players, playerIndex, moves) {
    	//	NEVER CALLED AS CURRENTLY DESIGNED
    },
    sendMove: function(moveRequest, reply) {
    	//	"send" is from the client's perspective
        transmitTime += Date.now() - tic;
        tic = Date.now();
        var move = decodeMove(moveRequest);
        buildTime += Date.now() - tic;
        tic = Date.now();
        game.executeDecision(move);
        playTime += Date.now() - tic;
    	game.move++;
        tic = Date.now();
    	var gameStates = [game.getGameState(0)].concat(game.playUntilPlayerId(0));
        playTime += Date.now() - tic;
    	tic = Date.now();
        var resp = buildMoveResponse(gameStates);
        buildTime += Date.now() - tic;
        tic = Date.now();
        reply(null, resp);
    }
});

server.bind("tcp://0.0.0.0:4242");
console.log("Listening on port 4242...");

