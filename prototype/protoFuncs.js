var common = require('./common.js');
var fs = require('fs');
var protobuf = require("protobufjs");

// Proto
var Splendor;
protobuf.load("../splendor.proto")
    .then(function(root) {
       Splendor = root;
       console.log(Splendor);
    });

module.exports = {
	buildMoveResponse : function(gameStates) {
		var moveResponse = {
			gameStateChanges: gameStates.map(buildGameState),
			availableMoves: buildAvailableMoves(gameStates.pop().moves)
		};
		var isDirty = Splendor.SplendorService.MoveResponse.verify(moveResponse);
		
		if(isDirty) {
			console.log("Verification error:", isDirty);
			process.exit(-1);
		}
		return Splendor.SplendorService.MoveResponse.encode(moveResponse).finish();
	},
	decodeMove : function(moveRequest) {
		return Splendor.SplendorService.MoveRequest.decode(moveRequest).move;
	}
};

function buildGameState(simulatorGameState) {
	return {
		board: buildBoard(simulatorGameState.board),
		players: simulatorGameState.players.map(buildPlayer),
		status : {
			isOver: simulatorGameState.isOver,
			winner: simulatorGameState.winner,
			currentPlayer: simulatorGameState.currentPlayer
		}
	};
}

function buildBoard(simulatorBoard) {
	return {
		chips: simulatorBoard.chips,
		exposedCardRows: simulatorBoard.decks.map(buildExposedCardRow),
		coveredCards: simulatorBoard.decks.map(buildCoveredCard),
		nobles: simulatorBoard.nobles.map(buildNoble)
	};
}

function buildExposedCardRow(deck) {
	return {
		tier: deck.tier,
		cards: deck.cards.slice(deck.cards.length-Math.min(4,deck.cards.length)).map(buildExposedCard)
	};
}

function buildCoveredCard(deck) {
	if(deck.cards.length < 5) {
		return null;
	}
	return {
		tier: deck.tier,
		isCovered: true
	};
}

function buildExposedCard(card) {
	return {
		tier: card.tier,
		isCovered: false,
		cost: card.cost,
		isReserved: false,
		victoryPoints: card.points,
		chipBenefit: 1 << (3*common.getColorIndex(card.color))
	};
}

function buildNoble(noble) {
	return {
		cardCost: common.convertCost(noble)
	};
}

function buildPlayer(player) {
	return {
		id: player.id,
		name: player.name,
		chips: player.chips,
		purchasedCards: player.purchasedCards.map(buildPurchasedCard),
		reservedCards: player.reservedCards.map(buildReservedCard),
		victoryPoints: player.points,
		nobles: player.nobles.map(buildNoble)
	};
}

function buildPurchasedCard(purchasedCard) {
	return {
		tier: purchasedCard.tier,
		isCovered: false,
		cost: purchasedCard.cost,
		isReserved: false,
		victoryPoints: purchasedCard.points,
		chipBenefit: 1 << (3*common.getColorIndex(purchasedCard.color))
	};
}

function buildReservedCard(reservedCard) {
	return {
		tier: reservedCard.tier,
		isCovered: false,
		cost: reservedCard.cost,
		isReserved: true,
		victoryPoints: reservedCard.points,
		chipBenefit: 1 << (3*common.getColorIndex(reservedCard.color))
	};
}

function buildAvailableMoves(moves) {
	return {
		chipMoves: moves.takeChips.map(buildTakeChipMove),
		purchaseMoves: moves.purchase.map(buildPurchaseMove),
		reserveMoves: moves.reserve.exposed.map(buildReserveExposedMove)
			.concat(moves.reserve.covered.map(buildReserveCoveredMove))
	};
}

function buildTakeChipMove(takeChip) {
	return {
		chipMove: {
			chipsToTake: Number(takeChip.split(',')[0]),
			chipsToGiveBack: Number(takeChip.split(',')[1])
		}
	};
}

function buildPurchaseMove(purchaseMove) {
	return {
		purchaseMove: {
			rowIndex: purchaseMove.card.row,
			cardIndex: purchaseMove.card.index
		}
	};
}

function buildReserveExposedMove(reserveExposedMove) {
	return {
		reserveMove: {
			isCovered: false,
			rowIndex: reserveExposedMove.card.row,
			cardIndex: reserveExposedMove.card.index	
		}
	};
}

function buildReserveCoveredMove(reserveCoveredMove) {
	return {
		reserveMove: {
			isCovered: true,
			rowIndex: reserveCoveredMove.card.row,
			cardIndex: reserveCoveredMove.card.index
		}
	};
}
