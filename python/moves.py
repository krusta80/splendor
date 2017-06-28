__all__ = ['moves']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([u'util', u'getPurchaseOptions', u'getChipTakingOptions', u'ChipMoves', u'getReserveOptions'])
@Js
def PyJsHoisted_getPurchaseOptions_(exposedCards, reservedCards, playerChipsAndCards, this, arguments, var=var):
    var = Scope({u'this':this, u'exposedCards':exposedCards, u'reservedCards':reservedCards, u'arguments':arguments, u'playerChipsAndCards':playerChipsAndCards}, var)
    var.registers([u'exposedCards', u'reservedCards', u'playerChipsAndCards'])
    @Js
    def PyJs_anonymous_9_(card, this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments, u'card':card}, var)
        var.registers([u'card'])
        return var.get(u'card').get(u'card').callprop(u'canBeBought', var.get(u'playerChipsAndCards'))
    PyJs_anonymous_9_._set_name(u'anonymous')
    @Js
    def PyJs_anonymous_10_(card, this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments, u'card':card}, var)
        var.registers([u'card'])
        PyJs_Object_11_ = Js({u'card':var.get(u'card')})
        return PyJs_Object_11_
    PyJs_anonymous_10_._set_name(u'anonymous')
    return var.get(u'exposedCards').callprop(u'concat', var.get(u'reservedCards').callprop(u'map', PyJs_anonymous_10_)).callprop(u'filter', PyJs_anonymous_9_)
PyJsHoisted_getPurchaseOptions_.func_name = u'getPurchaseOptions'
var.put(u'getPurchaseOptions', PyJsHoisted_getPurchaseOptions_)
@Js
def PyJsHoisted_getReserveOptions_(exposedCards, topCards, boardChips, reservedCards, playerChips, this, arguments, var=var):
    var = Scope({u'exposedCards':exposedCards, u'boardChips':boardChips, u'reservedCards':reservedCards, u'arguments':arguments, u'topCards':topCards, u'playerChips':playerChips, u'this':this}, var)
    var.registers([u'boardChips', u'topCards', u'exposedCards', u'reservedCards', u'reserveChipOptions', u'playerChips', u'options'])
    var.put(u'reserveChipOptions', var.get(u'ChipMoves').callprop(u'getReserveOptions', var.get(u'boardChips'), var.get(u'playerChips')))
    PyJs_Object_2_ = Js({u'exposed':Js([]),u'covered':Js([])})
    var.put(u'options', PyJs_Object_2_)
    if PyJsStrictEq(var.get(u'reservedCards').get(u'length'),Js(3.0)):
        return var.get(u'options')
    @Js
    def PyJs_anonymous_3_(card, this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments, u'card':card}, var)
        var.registers([u'card'])
        @Js
        def PyJs_anonymous_4_(option, this, arguments, var=var):
            var = Scope({u'this':this, u'option':option, u'arguments':arguments}, var)
            var.registers([u'option'])
            PyJs_Object_5_ = Js({u'card':var.get(u'card'),u'chips':var.get(u'option')})
            var.get(u'options').get(u'exposed').callprop(u'push', PyJs_Object_5_)
        PyJs_anonymous_4_._set_name(u'anonymous')
        var.get(u'reserveChipOptions').callprop(u'forEach', PyJs_anonymous_4_)
    PyJs_anonymous_3_._set_name(u'anonymous')
    var.get(u'exposedCards').callprop(u'forEach', PyJs_anonymous_3_)
    @Js
    def PyJs_anonymous_6_(card, this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments, u'card':card}, var)
        var.registers([u'card'])
        @Js
        def PyJs_anonymous_7_(option, this, arguments, var=var):
            var = Scope({u'this':this, u'option':option, u'arguments':arguments}, var)
            var.registers([u'option'])
            PyJs_Object_8_ = Js({u'card':var.get(u'card'),u'chips':var.get(u'option')})
            var.get(u'options').get(u'covered').callprop(u'push', PyJs_Object_8_)
        PyJs_anonymous_7_._set_name(u'anonymous')
        var.get(u'reserveChipOptions').callprop(u'forEach', PyJs_anonymous_7_)
    PyJs_anonymous_6_._set_name(u'anonymous')
    var.get(u'topCards').callprop(u'forEach', PyJs_anonymous_6_)
    return var.get(u'options')
PyJsHoisted_getReserveOptions_.func_name = u'getReserveOptions'
var.put(u'getReserveOptions', PyJsHoisted_getReserveOptions_)
var.put(u'util', var.get(u'require')(Js(u'util')))
var.put(u'ChipMoves', var.get(u'require')(Js(u'./chipMoves.js')))
var.put(u'getChipTakingOptions', var.get(u'ChipMoves').get(u'getChipTakingOptions'))
@Js
def PyJs_anonymous_0_(board, player, this, arguments, var=var):
    var = Scope({u'this':this, u'player':player, u'board':board, u'arguments':arguments}, var)
    var.registers([u'exposedCards', u'board', u'player'])
    var.put(u'exposedCards', var.get(u'board').callprop(u'getExposedCards'))
    PyJs_Object_1_ = Js({u'takeChips':var.get(u'getChipTakingOptions')(var.get(u'board').get(u'chips'), var.get(u'player').get(u'chips')),u'reserve':var.get(u'getReserveOptions')(var.get(u'exposedCards'), var.get(u'board').callprop(u'getTopCards'), var.get(u'board').get(u'chips'), var.get(u'player').get(u'reservedCards'), var.get(u'player').get(u'chips')),u'purchase':var.get(u'getPurchaseOptions')(var.get(u'exposedCards'), var.get(u'player').get(u'reservedCards'), var.get(u'player').get(u'chipsAndCards'))})
    return PyJs_Object_1_
PyJs_anonymous_0_._set_name(u'anonymous')
var.get(u'module').put(u'exports', PyJs_anonymous_0_)
pass
pass
pass


# Add lib to the module scope
moves = var.to_python()