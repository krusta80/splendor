__all__ = ['card']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([u'Card'])
@Js
def PyJs_anonymous_0_(color, points, cost, tier, this, arguments, var=var):
    var = Scope({u'tier':tier, u'points':points, u'cost':cost, u'arguments':arguments, u'color':color, u'this':this}, var)
    var.registers([u'color', u'tier', u'points', u'cost'])
    var.get(u"this").put(u'color', var.get(u'color'))
    var.get(u"this").put(u'points', var.get(u'points'))
    var.get(u"this").put(u'cost', var.get(u'cost'))
    var.get(u"this").put(u'tier', var.get(u'tier'))
    var.get(u"this").put(u'owner', (-Js(1.0)))
    var.get(u"this").put(u'isReserved', Js(False))
PyJs_anonymous_0_._set_name(u'anonymous')
var.put(u'Card', PyJs_anonymous_0_)

@Js
def PyJs_anonymous_1_(player, chips, this, arguments, var=var):
    var = Scope({u'this':this, u'player':player, u'chips':chips, u'arguments':arguments}, var)
    var.registers([u'player', u'chips'])
    return (var.get(u"this").callprop(u'canBeBought', var.get(u'chips')) and var.get(u"this").callprop(u'possess', var.get(u'player')))
PyJs_anonymous_1_._set_name(u'anonymous')
var.get(u'Card').get(u'prototype').put(u'buy', PyJs_anonymous_1_)
@Js
def PyJs_anonymous_2_(player, this, arguments, var=var):
    var = Scope({u'this':this, u'player':player, u'arguments':arguments}, var)
    var.registers([u'player'])
    if var.get(u"this").callprop(u'possess', var.get(u'player')):
        var.get(u"this").put(u'isReserved', var.get(u'true'))
        return var.get(u'true')
PyJs_anonymous_2_._set_name(u'anonymous')
var.get(u'Card').get(u'prototype').put(u'reserve', PyJs_anonymous_2_)
@Js
def PyJs_anonymous_3_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([])
    if var.get(u"this").get(u'isReserved').neg():
        var.get(u'console').callprop(u'log', Js(u'Error:  This card is not currently reserved.'), var.get(u"this").get(u'owner'))
        return Js(False)
    var.get(u"this").put(u'isReserved', Js(False))
    return var.get(u'true')
PyJs_anonymous_3_._set_name(u'anonymous')
var.get(u'Card').get(u'prototype').put(u'activate', PyJs_anonymous_3_)
@Js
def PyJs_anonymous_4_(player, this, arguments, var=var):
    var = Scope({u'this':this, u'player':player, u'arguments':arguments}, var)
    var.registers([u'player'])
    if ((var.get(u"this").get(u'owner')!=(-Js(1.0))) and ((var.get(u"this").get(u'owner')!=var.get(u'player')) or var.get(u"this").get(u'isReserved').neg())):
        var.get(u'console').callprop(u'log', Js(u'Error:  This card cannot be transfered.'), var.get(u"this").get(u'owner'))
        return Js(False)
    var.get(u"this").put(u'owner', var.get(u'player'))
    return var.get(u'true')
PyJs_anonymous_4_._set_name(u'anonymous')
var.get(u'Card').get(u'prototype').put(u'possess', PyJs_anonymous_4_)
@Js
def PyJs_anonymous_5_(chips, this, arguments, var=var):
    var = Scope({u'this':this, u'chips':chips, u'arguments':arguments}, var)
    var.registers([u'numberOfChipsShortBy', u'chips', u'colorIndex'])
    var.put(u'numberOfChipsShortBy', Js(0.0))
    #for JS loop
    var.put(u'colorIndex', Js(0.0))
    while (var.get(u'colorIndex')<Js(5.0)):
        try:
            var.put(u'numberOfChipsShortBy', var.get(u'Math').callprop(u'max', Js(0.0), (((var.get(u"this").get(u'cost')>>(Js(3.0)*var.get(u'colorIndex')))&Js(7.0))-(var.get(u'chips')&Js(7.0)))), u'+')
            var.put(u'chips', (var.get(u'chips')>>Js(3.0)))
        finally:
                (var.put(u'colorIndex',Js(var.get(u'colorIndex').to_number())+Js(1))-Js(1))
    return ((var.get(u'chips')&Js(7.0))>=var.get(u'numberOfChipsShortBy'))
PyJs_anonymous_5_._set_name(u'anonymous')
var.get(u'Card').get(u'prototype').put(u'canBeBought', PyJs_anonymous_5_)
pass


# Add lib to the module scope
card = var.to_python()