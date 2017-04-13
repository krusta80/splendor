//  Code responsible for enumerating all valid chip-taking (and returning)
//  moves for a player, indexed by middle chip counts (and player counts)
var singleChipArray = generateSingleChipPileArray();
var doubleChipArray = generateDoubleChipPileArray();
var giveBackArray = generateGiveBacks();

module.exports = {
    getChipTakingOptions: function(middleChipsCount, playerChipsCount) {
        var combinedTakeAndGiveBack = [];
        var combinedTakeArray =
            singleChipArray[getSingles(middleChipsCount)]
            .concat(doubleChipArray[getDoubles(middleChipsCount)]);

        combinedTakeArray.forEach(function(takeOption) {
            var giveBackOptions = giveBackArray[playerChipsCount + takeOption];

            if (!giveBackOptions) {
                return combinedTakeAndGiveBack.push(takeOption + ',' + 0);
            }
            giveBackOptions.forEach(function(giveBackOption) {
                if (takeOption != giveBackOption) {
                    combinedTakeAndGiveBack.push(takeOption + ',' + giveBackOption);
                }
            });
        });
        return combinedTakeAndGiveBack;
    },
    getReserveOptions: function(middleChipsCount, playerChipsCount) {
        var take = (middleChipsCount >> 15) & 1;
        var options = [];

        if (take === 0) {
            return ['0,0'];
        } else if (countChips(playerChipsCount) < 10) {
            return [(1 << 15) + ',0'];
        }
        for (var colorIndex = 0; colorIndex < 5; colorIndex++) {
            if ((playerChipsCount & (7 << (3 * colorIndex))) > 0) {
                options.push((1 << 15) + ',' + (1 << (3 * colorIndex)));
            }
        }
        return options;
    }
};

function getSingles(x) {
    var singles = 0;

    for (var colorIndex = 0; colorIndex < 5; colorIndex++) {
        singles = singles << 1;
        if ((x & 7) > 0) {
            singles++;
        }
        x = x >> 3;
    }
    return singles;
}

function getDoubles(x) {
    var doubles = 0;

    for (var colorIndex = 0; colorIndex < 5; colorIndex++) {
        doubles = doubles << 1;
        if ((x & 7) > 3) {
            doubles++;
        }
        x = x >> 3;
    }
    return doubles;
}

function generateSingleChipPileArray() {
    var singleChipPileCombos = [];

    for (var x = 0; x < 32; x++) {
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

    for (var x = 0; x < (1 << 18) - 2; x++) {
        chipCount = countChips(x);
        if (chipCount >= 11 && chipCount <= 13) {
            giveBacks[x] = generateGiveBackCombos(x);
        }
    }
    return giveBacks;
}

function countChips(x) {
    var totalChips = 0;

    for (var i = 0; i < 6; i++) {
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

    for (var i = 0; i < 6; i++) {
        for (var j = 0; j < (x & 7); j++) {
            chips.push(1 << (3 * i));
        }
        x = x >> 3;
    }
    return chips;
}

function findGiveBackCombos(chips, nextChipIndex, combo, overflow, giveBackCombos) {
    if (overflow <= 0) {
        return giveBackCombos[combo] = combo;
    }
    for (var i = nextChipIndex; i < chips.length - overflow + 1; i++) {
        findGiveBackCombos(chips, i + 1, combo + chips[i], overflow - 1, giveBackCombos);
    }
}
