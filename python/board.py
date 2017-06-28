__all__ = ['board']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([u'Board', u'Deck'])
var.put(u'Deck', var.get(u'require')(Js(u'./deck.js')))
@Js
def PyJs_anonymous_0_(playerCount, this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments, u'playerCount':playerCount}, var)
    var.registers([u'playerCount'])
    var.get(u"this").put(u'playerCount', var.get(u'playerCount'))
    var.get(u"this").callprop(u'reset')
PyJs_anonymous_0_._set_name(u'anonymous')
var.put(u'Board', PyJs_anonymous_0_)

@Js
def PyJs_anonymous_1_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([])
    var.get(u"this").put(u'nobles', var.get(u'require')(Js(u'./noble.js')).get(u'nobles').callprop(u'slice', Js(0.0), (var.get(u"this").get(u'playerCount')+Js(1.0))))
    var.get(u"this").put(u'decks', Js([var.get(u'Deck').create(Js(0.0)), var.get(u'Deck').create(Js(1.0)), var.get(u'Deck').create(Js(2.0))]))
    var.get(u"this").put(u'chips', var.get(u"this").callprop(u'getStartingChips'))
PyJs_anonymous_1_._set_name(u'anonymous')
var.get(u'Board').get(u'prototype').put(u'reset', PyJs_anonymous_1_)
@Js
def PyJs_anonymous_2_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([u'startingChips', u'startingChipCounts', u'colorIndex'])
    var.put(u'startingChipCounts', Js([Js(0.0), Js(0.0), Js(4.0), Js(5.0), Js(7.0)]))
    var.put(u'startingChips', (Js(5.0)<<Js(15.0)))
    #for JS loop
    var.put(u'colorIndex', Js(0.0))
    while (var.get(u'colorIndex')<Js(5.0)):
        try:
            var.put(u'startingChips', (var.get(u'startingChipCounts').get(var.get(u"this").get(u'playerCount'))<<(Js(3.0)*var.get(u'colorIndex'))), u'+')
        finally:
                (var.put(u'colorIndex',Js(var.get(u'colorIndex').to_number())+Js(1))-Js(1))
    return var.get(u'startingChips')
PyJs_anonymous_2_._set_name(u'anonymous')
var.get(u'Board').get(u'prototype').put(u'getStartingChips', PyJs_anonymous_2_)
@Js
def PyJs_anonymous_3_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([u'exposedCards', u'row'])
    var.put(u'exposedCards', Js([]))
    var.put(u'row', Js(0.0))
    @Js
    def PyJs_anonymous_4_(deck, this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments, u'deck':deck}, var)
        var.registers([u'i', u'deck'])
        #for JS loop
        var.put(u'i', Js(0.0))
        while (var.get(u'i')<var.get(u'Math').callprop(u'min', Js(4.0), var.get(u'deck').get(u'cards').get(u'length'))):
            try:
                PyJs_Object_5_ = Js({u'row':var.get(u'row'),u'index':((var.get(u'deck').get(u'cards').get(u'length')-var.get(u'i'))-Js(1.0)),u'card':var.get(u'deck').get(u'cards').get(((var.get(u'deck').get(u'cards').get(u'length')-var.get(u'i'))-Js(1.0)))})
                var.get(u'exposedCards').callprop(u'push', PyJs_Object_5_)
            finally:
                    (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))
        (var.put(u'row',Js(var.get(u'row').to_number())+Js(1))-Js(1))
    PyJs_anonymous_4_._set_name(u'anonymous')
    var.get(u"this").get(u'decks').callprop(u'forEach', PyJs_anonymous_4_)
    return var.get(u'exposedCards')
PyJs_anonymous_3_._set_name(u'anonymous')
var.get(u'Board').get(u'prototype').put(u'getExposedCards', PyJs_anonymous_3_)
@Js
def PyJs_anonymous_6_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([u'topCards', u'row'])
    var.put(u'topCards', Js([]))
    var.put(u'row', Js(0.0))
    @Js
    def PyJs_anonymous_7_(deck, this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments, u'deck':deck}, var)
        var.registers([u'deck'])
        if (var.get(u'deck').get(u'cards').get(u'length')>Js(4.0)):
            PyJs_Object_8_ = Js({u'row':var.get(u'row'),u'index':(var.get(u'deck').get(u'cards').get(u'length')-Js(5.0)),u'card':var.get(u'deck').get(u'cards').get((var.get(u'deck').get(u'cards').get(u'length')-Js(5.0)))})
            var.get(u'topCards').callprop(u'push', PyJs_Object_8_)
        (var.put(u'row',Js(var.get(u'row').to_number())+Js(1))-Js(1))
    PyJs_anonymous_7_._set_name(u'anonymous')
    var.get(u"this").get(u'decks').callprop(u'forEach', PyJs_anonymous_7_)
    return var.get(u'topCards')
PyJs_anonymous_6_._set_name(u'anonymous')
var.get(u'Board').get(u'prototype').put(u'getTopCards', PyJs_anonymous_6_)
@Js
def PyJs_anonymous_9_(row, index, this, arguments, var=var):
    var = Scope({u'this':this, u'index':index, u'arguments':arguments, u'row':row}, var)
    var.registers([u'index', u'row'])
    return var.get(u"this").get(u'decks').get(var.get(u'row')).get(u'cards').callprop(u'splice', var.get(u'index'), Js(1.0))
PyJs_anonymous_9_._set_name(u'anonymous')
var.get(u'Board').get(u'prototype').put(u'removeCard', PyJs_anonymous_9_)
@Js
def PyJs_anonymous_10_(chips, this, arguments, var=var):
    var = Scope({u'this':this, u'chips':chips, u'arguments':arguments}, var)
    var.registers([u'chips'])
    var.get(u"this").put(u'chips', var.get(u'chips'), u'+')
PyJs_anonymous_10_._set_name(u'anonymous')
var.get(u'Board').get(u'prototype').put(u'addChips', PyJs_anonymous_10_)
@Js
def PyJs_anonymous_11_(chips, this, arguments, var=var):
    var = Scope({u'this':this, u'chips':chips, u'arguments':arguments}, var)
    var.registers([u'chips'])
    var.get(u"this").put(u'chips', var.get(u'chips'), u'-')
PyJs_anonymous_11_._set_name(u'anonymous')
var.get(u'Board').get(u'prototype').put(u'removeChips', PyJs_anonymous_11_)
@Js
def PyJs_anonymous_12_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([])
    return var.get(u"this").get(u'decks')
PyJs_anonymous_12_._set_name(u'anonymous')
var.get(u'Board').get(u'prototype').put(u'getDecks', PyJs_anonymous_12_)
pass


# Add lib to the module scope
board = var.to_python()