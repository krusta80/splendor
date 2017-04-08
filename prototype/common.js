module.exports = {
	
	convertCost: function(cost){
		return cost.reduce(function(convertedCost,stackSize){
			return (convertedCost<<3) + stackSize;
		},0);
	},
	
	translateChipCount : function(x) {
	    var inEnglish = "";
	    var colors = ["B", "G", "R", "W", "b", "*"];
	    for (var i = 0; i < 6; i++) {
	        inEnglish += colors[i] + ": " + (x & 7) + ",  ";
	        x = x >> 3;
	    }
	    return inEnglish;
	},
};
