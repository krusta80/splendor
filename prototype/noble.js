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

module.exports = shuffle(nobleStats.map(common.convertCost.bind(this)));
