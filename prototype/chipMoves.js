//	Code responsible for enumerating all valid chip-taking (and returning)
//	moves for a player, indexed by middle chip counts (and player counts)
function generateSingleChipPileArray(){
	var singleChipPileCombos = [];

	for(var x = 0; x < 32; x++){
		singleChipPileCombos.push(generateSingleChipCombos(x));
	}
	return singleChipPileCombos;
}

function generateDoubleChipPileArray() {
    var doubleChipPileCombos = [];

    for (var x = 0; x < 32; x++) {
        doubleChipPileCombos.push(generateDoubleChipCombos(x));
    }
    return doubleChipPileCombos;
}

function generateSingleChipCombos(x) {
    var singleChipCombos = [];

    for (var i = 0; i <= x; i++) {
        if (hasThreeOrFewerBits(i)) {
            singleChipCombos.push(interweaveZeroes(i));
        }
    }
    return singleChipCombos;
}

function generateDoubleChipCombos(x) {
    var doubleChipCombos = [];

    for (var i = 0; i < 5; i++) {
        if (x & (1 << i) > 0) {
            doubleChipCombos.push(1 << (3 * i + 1));
        }
    }
    return doubleChipCombos;
}

function hasThreeOrFewerBits(i) {
    var bitCount = 0;

    while (i > 0) {
        bitCount += i & 1;
        i = i >> 1;
    }
    return bitCount <= 3;
}

function interweaveZeroes(i) {
    var interwoven = 0;
    var maskBit = 0;

    while (i > 0) {
        interwoven = interwoven | ((i & 1) << (3 * maskBit++));
        i = i >> 1;
    }
    return interwoven;
}

function generateGiveBacks() {
    var giveBacks = [];
    var chipCount;

    for (var x = 0; x < (1 << 15); x++) {
        chipCount = countChips(x);
        if (chipCount >= 11 && chipCount <= 13) {
            giveBacks[x] = generateGiveBackCombos(x);
        }
    }
    return giveBacks;
}

function countChips(x) {
    var totalChips = 0;

    for (var i = 0; i < 5; i++) {
        totalChips += (x & 7);
        x = x >> 3;
    }
    return totalChips;
}

function generateGiveBackCombos(x) {
    var giveBackCombos = {};

    findGiveBackCombos(extractChips(x), 0, 0, countChips(x) - 10, giveBackCombos);
    return Object.keys(giveBackCombos);
}

function extractChips(x) {
    var chips = [];

    for (var i = 0; i < 5; i++) {
        for (var j = 0; j < (x & 7); j++) {
            chips.push(1 << (3 * i));
        }
        x = x >> 3;
    }
    return chips;
}

function findGiveBackCombos(chips, nextChipIndex, combo, overflow, giveBackCombos) {
    if (!overflow) {
        return giveBackCombos[combo] = combo;
    }
    for (var i = nextChipIndex; i < chips.length - overflow + 1; i++) {
        findGiveBackCombos(chips, i + 1, combo + chips[i], overflow - 1, giveBackCombos);
    }
}

function translateChipCount(x) {
    var inEnglish = "";
    var colors = ["B", "G", "R", "W", "X"];
    for (var i = 0; i < 5; i++) {
        inEnglish += colors[i] + ": " + (x & 7) + ",  ";
        x = x >> 3;
    }
    return inEnglish;
}

//var singleChipPileArray = generateSingleChipPileArray();
//console.log(generateSingleChipCombos(31).map(function(combo){
//  return combo.toString(2);
//}));
//console.log("=======");
//console.log(generateDoubleChipCombos(31).map(function(combo){
//  return combo.toString(2);
//}));
//console.log(generateGiveBacks());
//console.log(generateGiveBackCombos(9435).map(translateChipCount));  // 2, 2, 2, 3, 3
