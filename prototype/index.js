var Agent = require('./agent.js');
var Game = require('./game.js');

if (process.argv.length < 4) {
    console.log("usage:", process.argv[1], "<number of games> <player 1 name>...<player n name>");
    process.exit();
}

var numberOfGames = process.argv[2];
var agents = process.argv.slice(3).map(function(name) {
    return new Agent(name);
});
var game = new Game(agents);
var outcomes = [];
var stats = {};
var winner;

while (numberOfGames--) {
    if (numberOfGames % 1000 === 0) {
        console.log(numberOfGames);
        //console.log("==== NEW GAME ====");
        //game.logMoves();
    }
    game.reset();
    outcomes.push(game.playUntilEnd());
    winner = game.getWinner();
    if (!stats[winner]) {
        stats[winner] = 0;
    }
    stats[winner]++;
}
console.log(outcomes);
console.log(stats);
