__all__ = ['game']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([u'Noble', u'shuffle', u'show', u'Player', u'Game', u'common', u'Board'])
var.put(u'Board', var.get(u'require')(Js(u'./board.js')))
var.put(u'Noble', var.get(u'require')(Js(u'./noble.js')))
var.put(u'Player', var.get(u'require')(Js(u'./player.js')))
var.put(u'common', var.get(u'require')(Js(u'./common.js')))
var.put(u'show', var.get(u'common').get(u'show'))
var.put(u'shuffle', var.get(u'require')(Js(u'shuffle-array')))
@Js
def PyJs_anonymous_0_(agents, this, arguments, var=var):
    var = Scope({u'this':this, u'agents':agents, u'arguments':arguments}, var)
    var.registers([u'agents'])
    var.get(u"this").put(u'playerCount', Js(0.0))
    @Js
    def PyJs_anonymous_1_(agent, this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments, u'agent':agent}, var)
        var.registers([u'player', u'agent'])
        var.put(u'player', var.get(u'Player').create((var.get(u"this").put(u'playerCount',Js(var.get(u"this").get(u'playerCount').to_number())+Js(1))-Js(1)), var.get(u'agent').get(u'name')))
        var.get(u'player').put(u'agent', var.get(u'agent'))
        return var.get(u'player')
    PyJs_anonymous_1_._set_name(u'anonymous')
    var.get(u"this").put(u'players', var.get(u'agents').callprop(u'map', PyJs_anonymous_1_.callprop(u'bind', var.get(u"this"))))
    var.get(u"this").put(u'board', var.get(u'Board').create(var.get(u"this").get(u'playerCount')))
    var.get(u"this").put(u'getMoves', var.get(u'require')(Js(u'./moves.js')))
    var.get(u"this").callprop(u'reset')
PyJs_anonymous_0_._set_name(u'anonymous')
var.put(u'Game', PyJs_anonymous_0_)
var.get(u'module').put(u'exports', var.get(u'Game'))
@Js
def PyJs_anonymous_2_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([])
    var.get(u'shuffle')(var.get(u"this").get(u'players'))
    @Js
    def PyJs_anonymous_3_(player, this, arguments, var=var):
        var = Scope({u'this':this, u'player':player, u'arguments':arguments}, var)
        var.registers([u'player'])
        var.get(u'player').callprop(u'reset')
    PyJs_anonymous_3_._set_name(u'anonymous')
    var.get(u"this").get(u'players').callprop(u'forEach', PyJs_anonymous_3_)
    var.get(u"this").get(u'board').callprop(u'reset')
    var.get(u"this").put(u'move', Js(0.0))
    var.get(u"this").put(u'movesMade', Js([]))
PyJs_anonymous_2_._set_name(u'anonymous')
var.get(u'Game').get(u'prototype').put(u'reset', PyJs_anonymous_2_)
@Js
def PyJs_anonymous_4_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([])
    return var.get(u"this").get(u'players').get((var.get(u"this").get(u'move')%var.get(u"this").get(u'playerCount')))
PyJs_anonymous_4_._set_name(u'anonymous')
var.get(u'Game').get(u'prototype').put(u'getCurrentPlayer', PyJs_anonymous_4_)
@Js
def PyJs_anonymous_5_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([])
    var.get(u'console').callprop(u'log', var.get(u'JSON').callprop(u'stringify', var.get(u"this").get(u'movesMade'), var.get(u"null"), Js(2.0)))
PyJs_anonymous_5_._set_name(u'anonymous')
var.get(u'Game').get(u'prototype').put(u'logMoves', PyJs_anonymous_5_)
@Js
def PyJs_anonymous_6_(id, this, arguments, var=var):
    var = Scope({u'this':this, u'id':id, u'arguments':arguments}, var)
    var.registers([u'player', u'decision', u'id', u'gameStates'])
    pass
    pass
    var.put(u'gameStates', Js([]))
    while (((var.get(u"this").get(u'move')<Js(200.0)) and var.get(u"this").callprop(u'isOver').neg()) and (var.get(u"this").callprop(u'getCurrentPlayer').get(u'id')!=var.get(u'id'))):
        var.put(u'player', var.get(u"this").callprop(u'getCurrentPlayer'))
        var.put(u'decision', var.get(u'player').get(u'agent').callprop(u'makeMove', var.get(u"this").get(u'board'), var.get(u"this").get(u'players'), (var.get(u"this").get(u'move')%var.get(u"this").get(u'playerCount')), var.get(u"this").callprop(u'getMoves', var.get(u"this").get(u'board'), var.get(u'player'))))
        PyJs_Object_7_ = Js({u'turn':var.get(u"this").get(u'move'),u'player':var.get(u"this").callprop(u'gatherPlayerStats', var.get(u'player')),u'move':var.get(u'decision')})
        var.get(u"this").get(u'movesMade').callprop(u'push', PyJs_Object_7_)
        var.get(u"this").callprop(u'executeDecision', var.get(u'decision'))
        var.get(u'gameStates').callprop(u'push', var.get(u"this").callprop(u'getGameState', var.get(u'id')))
        (var.get(u"this").put(u'move',Js(var.get(u"this").get(u'move').to_number())+Js(1))-Js(1))
    return var.get(u'gameStates')
PyJs_anonymous_6_._set_name(u'anonymous')
var.get(u'Game').get(u'prototype').put(u'playUntilPlayerId', PyJs_anonymous_6_)
@Js
def PyJs_anonymous_8_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([])
    return (PyJsStrictEq((var.get(u"this").get(u'move')%var.get(u"this").get(u'playerCount')),Js(0.0)) and (var.get(u"this").callprop(u'getTopScore')>=Js(15.0)))
PyJs_anonymous_8_._set_name(u'anonymous')
var.get(u'Game').get(u'prototype').put(u'isOver', PyJs_anonymous_8_)
@Js
def PyJs_anonymous_9_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([])
    @Js
    def PyJs_anonymous_10_(topScore, player, this, arguments, var=var):
        var = Scope({u'this':this, u'player':player, u'topScore':topScore, u'arguments':arguments}, var)
        var.registers([u'player', u'topScore'])
        return var.get(u'Math').callprop(u'max', var.get(u'topScore'), var.get(u'player').get(u'points'))
    PyJs_anonymous_10_._set_name(u'anonymous')
    return var.get(u"this").get(u'players').callprop(u'reduce', PyJs_anonymous_10_, Js(0.0))
PyJs_anonymous_9_._set_name(u'anonymous')
var.get(u'Game').get(u'prototype').put(u'getTopScore', PyJs_anonymous_9_)
@Js
def PyJs_anonymous_11_(decision, this, arguments, var=var):
    var = Scope({u'this':this, u'decision':decision, u'arguments':arguments}, var)
    var.registers([u'decision'])
    if PyJsStrictEq(var.get(u'decision').get(u'label'),Js(u'PURCHASE')):
        return var.get(u"this").callprop(u'executePurchase', var.get(u'decision').get(u'action'))
    if PyJsStrictEq(var.get(u'decision').get(u'label'),Js(u'TAKE')):
        return var.get(u"this").callprop(u'executeTake', var.get(u'decision').get(u'action'))
    if PyJsStrictEq(var.get(u'decision').get(u'label'),Js(u'RESERVE_EXPOSED')):
        return var.get(u"this").callprop(u'executeReserve', var.get(u'decision').get(u'action'), Js(False))
    if PyJsStrictEq(var.get(u'decision').get(u'label'),Js(u'RESERVE_COVERED')):
        return var.get(u"this").callprop(u'executeReserve', var.get(u'decision').get(u'action'), var.get(u'true'))
PyJs_anonymous_11_._set_name(u'anonymous')
var.get(u'Game').get(u'prototype').put(u'executeDecision', PyJs_anonymous_11_)
@Js
def PyJs_anonymous_12_(action, this, arguments, var=var):
    var = Scope({u'action':action, u'this':this, u'arguments':arguments}, var)
    var.registers([u'prePurchasePlayerChips', u'action'])
    var.put(u'prePurchasePlayerChips', var.get(u"this").callprop(u'getCurrentPlayer').get(u'chips'))
    if var.get(u'action').get(u'card').get(u'isReserved'):
        var.get(u"this").callprop(u'getCurrentPlayer').callprop(u'activateCard', var.get(u'action').get(u'card'))
    else:
        var.get(u"this").callprop(u'getCurrentPlayer').callprop(u'buyCard', var.get(u'action').get(u'card'))
        var.get(u"this").get(u'board').callprop(u'removeCard', var.get(u'action').get(u'row'), var.get(u'action').get(u'index'))
    var.get(u"this").get(u'board').callprop(u'addChips', (var.get(u'prePurchasePlayerChips')-var.get(u"this").callprop(u'getCurrentPlayer').get(u'chips')))
    var.get(u"this").callprop(u'checkNobles')
PyJs_anonymous_12_._set_name(u'anonymous')
var.get(u'Game').get(u'prototype').put(u'executePurchase', PyJs_anonymous_12_)
@Js
def PyJs_anonymous_13_(action, this, arguments, var=var):
    var = Scope({u'action':action, u'this':this, u'arguments':arguments}, var)
    var.registers([u'action', u'giveBack', u'take'])
    var.put(u'take', var.get(u'Number')(var.get(u'action').callprop(u'split', Js(u',')).get(u'0')))
    var.put(u'giveBack', var.get(u'Number')(var.get(u'action').callprop(u'split', Js(u',')).get(u'1')))
    var.get(u"this").callprop(u'makeChipExchange', var.get(u'take'), var.get(u'giveBack'))
PyJs_anonymous_13_._set_name(u'anonymous')
var.get(u'Game').get(u'prototype').put(u'executeTake', PyJs_anonymous_13_)
@Js
def PyJs_anonymous_14_(action, isCovered, this, arguments, var=var):
    var = Scope({u'action':action, u'this':this, u'arguments':arguments, u'isCovered':isCovered}, var)
    var.registers([u'action', u'giveBack', u'take', u'card', u'isCovered'])
    var.put(u'card', var.get(u'action').get(u'card').get(u'card'))
    var.put(u'take', var.get(u'Number')(var.get(u'action').get(u'chips').callprop(u'split', Js(u',')).get(u'0')))
    var.put(u'giveBack', var.get(u'Number')(var.get(u'action').get(u'chips').callprop(u'split', Js(u',')).get(u'1')))
    var.get(u"this").get(u'board').callprop(u'removeCard', var.get(u'action').get(u'card').get(u'row'), var.get(u'action').get(u'card').get(u'index'))
    var.get(u"this").callprop(u'getCurrentPlayer').callprop(u'reserveCard', var.get(u'card'), Js(0.0))
    var.get(u"this").callprop(u'makeChipExchange', var.get(u'take'), var.get(u'giveBack'))
PyJs_anonymous_14_._set_name(u'anonymous')
var.get(u'Game').get(u'prototype').put(u'executeReserve', PyJs_anonymous_14_)
@Js
def PyJs_anonymous_15_(take, giveBack, this, arguments, var=var):
    var = Scope({u'this':this, u'giveBack':giveBack, u'take':take, u'arguments':arguments}, var)
    var.registers([u'giveBack', u'take'])
    var.get(u"this").callprop(u'getCurrentPlayer').callprop(u'addChips', var.get(u'take'))
    var.get(u"this").get(u'board').callprop(u'removeChips', var.get(u'take'))
    var.get(u"this").callprop(u'getCurrentPlayer').callprop(u'removeChips', var.get(u'giveBack'))
    var.get(u"this").get(u'board').callprop(u'addChips', var.get(u'giveBack'))
PyJs_anonymous_15_._set_name(u'anonymous')
var.get(u'Game').get(u'prototype').put(u'makeChipExchange', PyJs_anonymous_15_)
@Js
def PyJs_anonymous_16_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([u'winner'])
    var.put(u'winner', var.get(u"this").callprop(u'getWinner'))
    PyJs_Object_17_ = Js({u'winner':var.get(u'winner'),u'score':var.get(u"this").callprop(u'getTopScore'),u'moves':var.get(u"this").get(u'move')})
    return PyJs_Object_17_
PyJs_anonymous_16_._set_name(u'anonymous')
var.get(u'Game').get(u'prototype').put(u'getOutcome', PyJs_anonymous_16_)
@Js
def PyJs_anonymous_18_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([])
    @Js
    def PyJs_anonymous_19_(a, b, this, arguments, var=var):
        var = Scope({u'a':a, u'this':this, u'b':b, u'arguments':arguments}, var)
        var.registers([u'a', u'b'])
        return ((((var.get(u'a').get(u'points')-var.get(u'b').get(u'points'))*Js(100.0))+var.get(u'b').get(u'purchasedCards').get(u'length'))-var.get(u'a').get(u'purchasedCards').get(u'length'))
    PyJs_anonymous_19_._set_name(u'anonymous')
    var.get(u"this").get(u'players').callprop(u'sort', PyJs_anonymous_19_)
    if (PyJsStrictEq(var.get(u"this").get(u'players').get(u'0').get(u'points'),var.get(u"this").get(u'players').get(u'1').get(u'points')) and PyJsStrictEq(var.get(u"this").get(u'players').get(u'0').get(u'purchasedCards').get(u'length'),var.get(u"this").get(u'players').get(u'1').get(u'purchasedCards').get(u'length'))):
        return (-Js(1.0))
    return var.get(u"this").get(u'players').get(u'0').get(u'id')
PyJs_anonymous_18_._set_name(u'anonymous')
var.get(u'Game').get(u'prototype').put(u'getWinner', PyJs_anonymous_18_)
@Js
def PyJs_anonymous_20_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([u'takeableNobles', u'index'])
    var.put(u'index', Js(0.0))
    @Js
    def PyJs_anonymous_21_(noble, this, arguments, var=var):
        var = Scope({u'this':this, u'noble':noble, u'arguments':arguments}, var)
        var.registers([u'noble'])
        return var.get(u'Noble').callprop(u'canGetNoble', var.get(u'noble').get(u'noble'), var.get(u"this").callprop(u'getCurrentPlayer').get(u'cardChipValues'))
    PyJs_anonymous_21_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_22_(noble, this, arguments, var=var):
        var = Scope({u'this':this, u'noble':noble, u'arguments':arguments}, var)
        var.registers([u'noble'])
        PyJs_Object_23_ = Js({u'index':(var.put(u'index',Js(var.get(u'index').to_number())+Js(1))-Js(1)),u'noble':var.get(u'noble')})
        return PyJs_Object_23_
    PyJs_anonymous_22_._set_name(u'anonymous')
    var.put(u'takeableNobles', var.get(u"this").get(u'board').get(u'nobles').callprop(u'map', PyJs_anonymous_22_).callprop(u'filter', PyJs_anonymous_21_.callprop(u'bind', var.get(u"this"))))
    if (var.get(u'takeableNobles').get(u'length')>Js(0.0)):
        var.get(u"this").callprop(u'getCurrentPlayer').callprop(u'addNoble', var.get(u"this").get(u'board').get(u'nobles').callprop(u'splice', var.get(u"this").callprop(u'getCurrentPlayer').get(u'agent').callprop(u'takeNoble', var.get(u'takeableNobles')).get(u'index'), Js(1.0)).get(u'0'))
PyJs_anonymous_20_._set_name(u'anonymous')
var.get(u'Game').get(u'prototype').put(u'checkNobles', PyJs_anonymous_20_)
@Js
def PyJs_anonymous_24_(player, this, arguments, var=var):
    var = Scope({u'this':this, u'player':player, u'arguments':arguments}, var)
    var.registers([u'player'])
    PyJs_Object_25_ = Js({u'id':var.get(u'player').get(u'id'),u'name':var.get(u'player').get(u'name'),u'points':var.get(u'player').get(u'points'),u'cardSummary':var.get(u'player').callprop(u'getCardChipValues'),u'reserves':var.get(u'player').callprop(u'getReservedCards'),u'chips':var.get(u'common').callprop(u'translateChipCount', var.get(u'player').get(u'chips')),u'nobles':var.get(u'player').callprop(u'getNobles')})
    return PyJs_Object_25_
PyJs_anonymous_24_._set_name(u'anonymous')
var.get(u'Game').get(u'prototype').put(u'gatherPlayerStats', PyJs_anonymous_24_)
@Js
def PyJs_anonymous_26_(playerId, this, arguments, var=var):
    var = Scope({u'playerId':playerId, u'this':this, u'arguments':arguments}, var)
    var.registers([u'playerId'])
    PyJs_Object_27_ = Js({u'turn':var.get(u"this").get(u'move'),u'board':var.get(u"this").get(u'board'),u'players':var.get(u"this").get(u'players'),u'moves':var.get(u"this").callprop(u'getMoves', var.get(u"this").get(u'board'), var.get(u"this").callprop(u'getCurrentPlayer')),u'isOver':var.get(u"this").callprop(u'isOver'),u'currentPlayer':var.get(u'playerId'),u'winner':var.get(u"this").callprop(u'getWinner'),u'didWin':(var.get(u"this").callprop(u'getWinner')==var.get(u'playerId'))})
    return PyJs_Object_27_
PyJs_anonymous_26_._set_name(u'anonymous')
var.get(u'Game').get(u'prototype').put(u'getGameState', PyJs_anonymous_26_)
pass


# Add lib to the module scope
game = var.to_python()