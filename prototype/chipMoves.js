//	Code responsible for enumerating all valid chip-taking (and returning)
//	moves for a player, indexed by middle chip counts (and player counts)

function generateGiveBacks(){
	var giveBacks = [];
	var chipCount;

	for(var x = 0; x < (1<<15); x++){
		chipCount = countChips(x);
		if(chipCount >= 11 && chipCount <= 13){
			giveBacks[x] = generateGiveBackCombos(x);
		}
	}
	return giveBacks;
}

function countChips(x){
	var totalChips = 0;

	for(var i = 0; i < 5; i++){
		totalChips += (x&7);
		x = x>>3;
	}
	return totalChips;
}

function generateGiveBackCombos(x){
	var giveBackCombos = {};

	findGiveBackCombos(extractChips(x), 0, 0, countChips(x)-10, giveBackCombos);
	return Object.keys(giveBackCombos);
}

function extractChips(x){
	var chips = [];

	for(var i = 0; i < 5; i++){
		for(var j = 0; j < (x&7); j++){
			chips.push(1<<(3*i));
		}
		x = x>>3;
	}
	return chips;
}

function findGiveBackCombos(chips, nextChipIndex, combo, overflow, giveBackCombos){
	if(!overflow){
		return giveBackCombos[combo] = combo;
	}
	for(var i = nextChipIndex; i < chips.length-overflow+1; i++){
		findGiveBackCombos(chips, i+1, combo+chips[i], overflow-1, giveBackCombos);
	}
}

function translateChipCount(x){
	var inEnglish = "";
	var colors = ["B", "G", "R", "W", "X"];
	for(var i = 0; i < 5; i++){
		inEnglish += colors[i]+": "+(x&7)+",  ";
		x = x>>3;
	}
	return inEnglish;	
}

//console.log(generateGiveBacks());
//console.log(generateGiveBackCombos(9435).map(translateChipCount));  // 2, 2, 2, 3, 3