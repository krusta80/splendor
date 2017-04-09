module.exports = {

    convertCost: function(cost) {
        return cost.reduce(function(convertedCost, stackSize) {
            return (convertedCost << 3) + stackSize;
        }, 0);
    },

    translateChipCount: function(x) {
        var inEnglish = "";
        var colors = ["B", "G", "R", "W", "b", "*"];
        for (var i = 0; i < 6; i++) {
            inEnglish += colors[i] + ": " + (x & 7) + ",  ";
            x = x >> 3;
        }
        return inEnglish;
    },

    getColorIndex : function(color) {
        var colors = {
            B: 0,
            G: 1,
            R: 2,
            W: 3,
            b: 4,
            g: 5
        };
        return colors[color];
    }
};
