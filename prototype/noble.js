var common = require('./common.js');
var shuffle = require('shuffle-array');

var nobleStats = [
    [4, 0, 0, 4, 0],
    [0, 0, 4, 0, 4],
    [4, 4, 0, 0, 0],
    [0, 4, 4, 0, 0],
    [0, 0, 0, 4, 4],
    [0, 0, 3, 3, 3],
    [3, 3, 3, 0, 0],
    [3, 3, 0, 3, 0],
    [3, 0, 0, 3, 3],
    [0, 3, 3, 0, 3],
];

module.exports = {
    nobles: shuffle(nobleStats.map(common.convertCost.bind(this))),
    canGetNoble: function(nobleStats, playerStats) {
        for(var i = 0; i < 5; i++){
            if(nobleStats[i] > playerStats[i]){
                return false;
            }
        }
        return true;
    }
};
