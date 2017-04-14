var zerorpc = require("zerorpc");
var Agent = require('./agent.js');
var Game = require('./game.js');
var show = require('./common.js').show;

var server = new zerorpc.Server({
    newSession: function(name, numberOfOpponents, reply) {
        this.name = name.toString();
        var agents = [this];
        for(var i = 0; i < numberOfOpponents; i++){
        	agents.push(new Agent("Opponent "+(i+1)));
        }
        this.game = new Game(agents);
        reply(null, "Hello, " + name + show(this.game.players));
        console.log(show(this.game));
    },
    newGame: function() {
    	this.game.reset();
    	this.game.playUntilEnd();
    },
    makeMove: function(board, players, playerIndex, moves) {
    	//	TODO(jgruska): Need to make game wait for agent to move...
    }
});

server.bind("tcp://0.0.0.0:4242");
console.log("Listening on port 4242...");
