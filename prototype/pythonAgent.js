var zerorpc = require("zerorpc");
var Agent = require('./agent.js');
var Game = require('./game.js');
var show = require('./common.js').show;
var sleep = require('sleep');

var server = new zerorpc.Server({
    newSession: function(name, numberOfOpponents, reply) {
        this.name = name.toString();
        this.nextResponse = null;
        var agents = [this];
        console.log(show(this));
        for(var i = 0; i < numberOfOpponents; i++){
        	agents.push(new Agent("Opponent "+(i+1)));
        }
        this.game = new Game(agents);
        reply(null, "Hello, " + name + show(this.game.players));
        console.log(show(this.game));
    },
    newGame: function(reply) {
    	this.game.reset();
    	reply(null, "New game: " + show(this.game));
    	setTimeout(this.game.playUntilEnd.bind(this.game), 0);
    },
    makeMove: function(board, players, playerIndex, moves) {
    	//	TODO(jgruska): Need to make game wait for agent to move...
    	console.log("Python make move!!");
    	var timeout = 0;
    	while(timeout++ < 1000 && !this.nextResponse) {
    		sleep.msleep(10);
    	}
    }
});

server.bind("tcp://0.0.0.0:4242");
console.log("Listening on port 4242...");
