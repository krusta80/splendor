__all__ = ['deck']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([u'shuffle', u'common', u'Card', u'Deck'])
var.put(u'Card', var.get(u'require')(Js(u'./card.js')))
var.put(u'shuffle', var.get(u'require')(Js(u'shuffle-array')))
var.put(u'common', var.get(u'require')(Js(u'./common.js')))
@Js
def PyJs_anonymous_0_(tier, this, arguments, var=var):
    var = Scope({u'tier':tier, u'this':this, u'arguments':arguments}, var)
    var.registers([u'tier'])
    var.get(u"this").put(u'tier', var.get(u'tier'))
    var.get(u"this").put(u'cards', var.get(u"this").callprop(u'prepareCards'))
PyJs_anonymous_0_._set_name(u'anonymous')
var.put(u'Deck', PyJs_anonymous_0_)
var.get(u'module').put(u'exports', var.get(u'Deck'))
@Js
def PyJs_anonymous_1_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([])
    if ((var.get(u"this").get(u'tier')<Js(0.0)) or (var.get(u"this").get(u'tier')>Js(2.0))):
        return var.get(u'console').callprop(u'log', Js(u'ERROR:  Cannot prepare tierless deck!'))
    return var.get(u'shuffle')(var.get(u"this").callprop(u'getCardStats').get(var.get(u"this").get(u'tier')).callprop(u'map', var.get(u"this").get(u'makeCard').callprop(u'bind', var.get(u"this"))))
PyJs_anonymous_1_._set_name(u'anonymous')
var.get(u'Deck').get(u'prototype').put(u'prepareCards', PyJs_anonymous_1_)
@Js
def PyJs_anonymous_2_(cardStats, this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments, u'cardStats':cardStats}, var)
    var.registers([u'cardStats'])
    return var.get(u'Card').create(var.get(u'cardStats').get(u'0'), var.get(u'cardStats').get(u'1'), var.get(u'common').callprop(u'convertCost', var.get(u'cardStats').get(u'2')), var.get(u'cardStats').get(u'3'))
PyJs_anonymous_2_._set_name(u'anonymous')
var.get(u'Deck').get(u'prototype').put(u'makeCard', PyJs_anonymous_2_)
@Js
def PyJs_anonymous_3_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([])
    def PyJs_LONG_4_(var=var):
        return Js([Js([Js([Js(u'B'), Js(3.0), Js([Js(0.0), Js(3.0), Js(3.0), Js(3.0), Js(5.0)]), Js(2.0)]), Js([Js(u'G'), Js(3.0), Js([Js(3.0), Js(0.0), Js(3.0), Js(5.0), Js(3.0)]), Js(2.0)]), Js([Js(u'R'), Js(3.0), Js([Js(5.0), Js(3.0), Js(0.0), Js(3.0), Js(3.0)]), Js(2.0)]), Js([Js(u'W'), Js(3.0), Js([Js(3.0), Js(3.0), Js(5.0), Js(0.0), Js(3.0)]), Js(2.0)]), Js([Js(u'b'), Js(3.0), Js([Js(3.0), Js(5.0), Js(3.0), Js(3.0), Js(0.0)]), Js(2.0)]), Js([Js(u'B'), Js(4.0), Js([Js(3.0), Js(0.0), Js(0.0), Js(6.0), Js(3.0)]), Js(2.0)]), Js([Js(u'G'), Js(4.0), Js([Js(6.0), Js(3.0), Js(0.0), Js(3.0), Js(0.0)]), Js(2.0)]), Js([Js(u'R'), Js(4.0), Js([Js(3.0), Js(6.0), Js(3.0), Js(0.0), Js(0.0)]), Js(2.0)]), Js([Js(u'W'), Js(4.0), Js([Js(0.0), Js(0.0), Js(3.0), Js(3.0), Js(6.0)]), Js(2.0)]), Js([Js(u'b'), Js(4.0), Js([Js(0.0), Js(3.0), Js(6.0), Js(0.0), Js(3.0)]), Js(2.0)]), Js([Js(u'B'), Js(4.0), Js([Js(0.0), Js(0.0), Js(0.0), Js(7.0), Js(0.0)]), Js(2.0)]), Js([Js(u'G'), Js(4.0), Js([Js(7.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0)]), Js(2.0)]), Js([Js(u'R'), Js(4.0), Js([Js(0.0), Js(7.0), Js(0.0), Js(0.0), Js(0.0)]), Js(2.0)]), Js([Js(u'W'), Js(4.0), Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(7.0)]), Js(2.0)]), Js([Js(u'b'), Js(4.0), Js([Js(0.0), Js(0.0), Js(7.0), Js(0.0), Js(0.0)]), Js(2.0)]), Js([Js(u'B'), Js(5.0), Js([Js(3.0), Js(0.0), Js(0.0), Js(7.0), Js(0.0)]), Js(2.0)]), Js([Js(u'G'), Js(5.0), Js([Js(7.0), Js(3.0), Js(0.0), Js(0.0), Js(0.0)]), Js(2.0)]), Js([Js(u'R'), Js(5.0), Js([Js(0.0), Js(7.0), Js(3.0), Js(0.0), Js(0.0)]), Js(2.0)]), Js([Js(u'W'), Js(5.0), Js([Js(0.0), Js(0.0), Js(0.0), Js(3.0), Js(7.0)]), Js(2.0)]), Js([Js(u'b'), Js(5.0), Js([Js(0.0), Js(0.0), Js(7.0), Js(0.0), Js(3.0)]), Js(2.0)])]), Js([Js([Js(u'B'), Js(3.0), Js([Js(6.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0)]), Js(1.0)]), Js([Js(u'G'), Js(3.0), Js([Js(0.0), Js(6.0), Js(0.0), Js(0.0), Js(0.0)]), Js(1.0)]), Js([Js(u'R'), Js(3.0), Js([Js(0.0), Js(0.0), Js(6.0), Js(0.0), Js(0.0)]), Js(1.0)]), Js([Js(u'W'), Js(3.0), Js([Js(0.0), Js(0.0), Js(0.0), Js(6.0), Js(0.0)]), Js(1.0)]), Js([Js(u'b'), Js(3.0), Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(6.0)]), Js(1.0)]), Js([Js(u'B'), Js(2.0), Js([Js(5.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0)]), Js(1.0)]), Js([Js(u'G'), Js(2.0), Js([Js(0.0), Js(5.0), Js(0.0), Js(0.0), Js(0.0)]), Js(1.0)]), Js([Js(u'R'), Js(2.0), Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(5.0)]), Js(1.0)]), Js([Js(u'W'), Js(2.0), Js([Js(0.0), Js(0.0), Js(5.0), Js(0.0), Js(0.0)]), Js(1.0)]), Js([Js(u'b'), Js(2.0), Js([Js(0.0), Js(0.0), Js(0.0), Js(5.0), Js(0.0)]), Js(1.0)]), Js([Js(u'B'), Js(2.0), Js([Js(3.0), Js(0.0), Js(0.0), Js(5.0), Js(0.0)]), Js(1.0)]), Js([Js(u'G'), Js(2.0), Js([Js(5.0), Js(3.0), Js(0.0), Js(0.0), Js(0.0)]), Js(1.0)]), Js([Js(u'R'), Js(2.0), Js([Js(0.0), Js(0.0), Js(0.0), Js(3.0), Js(5.0)]), Js(1.0)]), Js([Js(u'W'), Js(2.0), Js([Js(0.0), Js(0.0), Js(5.0), Js(0.0), Js(3.0)]), Js(1.0)]), Js([Js(u'b'), Js(2.0), Js([Js(0.0), Js(5.0), Js(3.0), Js(0.0), Js(0.0)]), Js(1.0)]), Js([Js(u'B'), Js(2.0), Js([Js(0.0), Js(0.0), Js(1.0), Js(2.0), Js(4.0)]), Js(1.0)]), Js([Js(u'G'), Js(2.0), Js([Js(2.0), Js(0.0), Js(0.0), Js(4.0), Js(1.0)]), Js(1.0)]), Js([Js(u'R'), Js(2.0), Js([Js(4.0), Js(2.0), Js(0.0), Js(1.0), Js(0.0)]), Js(1.0)]), Js([Js(u'W'), Js(2.0), Js([Js(0.0), Js(1.0), Js(4.0), Js(0.0), Js(2.0)]), Js(1.0)]), Js([Js(u'b'), Js(2.0), Js([Js(1.0), Js(4.0), Js(2.0), Js(0.0), Js(0.0)]), Js(1.0)]), Js([Js(u'B'), Js(1.0), Js([Js(2.0), Js(2.0), Js(3.0), Js(0.0), Js(0.0)]), Js(1.0)]), Js([Js(u'G'), Js(1.0), Js([Js(3.0), Js(0.0), Js(0.0), Js(2.0), Js(2.0)]), Js(1.0)]), Js([Js(u'R'), Js(1.0), Js([Js(0.0), Js(0.0), Js(2.0), Js(2.0), Js(3.0)]), Js(1.0)]), Js([Js(u'W'), Js(1.0), Js([Js(0.0), Js(3.0), Js(2.0), Js(0.0), Js(2.0)]), Js(1.0)]), Js([Js(u'b'), Js(1.0), Js([Js(2.0), Js(2.0), Js(0.0), Js(3.0), Js(0.0)]), Js(1.0)]), Js([Js(u'B'), Js(1.0), Js([Js(2.0), Js(3.0), Js(0.0), Js(0.0), Js(3.0)]), Js(1.0)]), Js([Js(u'G'), Js(1.0), Js([Js(0.0), Js(2.0), Js(3.0), Js(3.0), Js(0.0)]), Js(1.0)]), Js([Js(u'R'), Js(1.0), Js([Js(3.0), Js(0.0), Js(2.0), Js(0.0), Js(3.0)]), Js(1.0)]), Js([Js(u'W'), Js(1.0), Js([Js(3.0), Js(0.0), Js(3.0), Js(2.0), Js(0.0)]), Js(1.0)]), Js([Js(u'b'), Js(1.0), Js([Js(0.0), Js(3.0), Js(0.0), Js(3.0), Js(2.0)]), Js(1.0)])]), Js([Js([Js(u'B'), Js(1.0), Js([Js(0.0), Js(0.0), Js(4.0), Js(0.0), Js(0.0)]), Js(0.0)]), Js([Js(u'G'), Js(1.0), Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(4.0)]), Js(0.0)]), Js([Js(u'R'), Js(1.0), Js([Js(0.0), Js(0.0), Js(0.0), Js(4.0), Js(0.0)]), Js(0.0)]), Js([Js(u'W'), Js(1.0), Js([Js(0.0), Js(4.0), Js(0.0), Js(0.0), Js(0.0)]), Js(0.0)]), Js([Js(u'b'), Js(1.0), Js([Js(4.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0)]), Js(0.0)]), Js([Js(u'B'), Js(0.0), Js([Js(0.0), Js(1.0), Js(1.0), Js(1.0), Js(1.0)]), Js(0.0)]), Js([Js(u'G'), Js(0.0), Js([Js(1.0), Js(0.0), Js(1.0), Js(1.0), Js(1.0)]), Js(0.0)]), Js([Js(u'R'), Js(0.0), Js([Js(1.0), Js(1.0), Js(0.0), Js(1.0), Js(1.0)]), Js(0.0)]), Js([Js(u'W'), Js(0.0), Js([Js(1.0), Js(1.0), Js(1.0), Js(0.0), Js(1.0)]), Js(0.0)]), Js([Js(u'b'), Js(0.0), Js([Js(1.0), Js(1.0), Js(1.0), Js(1.0), Js(0.0)]), Js(0.0)]), Js([Js(u'B'), Js(0.0), Js([Js(0.0), Js(1.0), Js(2.0), Js(1.0), Js(1.0)]), Js(0.0)]), Js([Js(u'G'), Js(0.0), Js([Js(1.0), Js(0.0), Js(1.0), Js(1.0), Js(2.0)]), Js(0.0)]), Js([Js(u'R'), Js(0.0), Js([Js(1.0), Js(1.0), Js(0.0), Js(2.0), Js(1.0)]), Js(0.0)]), Js([Js(u'W'), Js(0.0), Js([Js(1.0), Js(2.0), Js(1.0), Js(0.0), Js(1.0)]), Js(0.0)]), Js([Js(u'b'), Js(0.0), Js([Js(2.0), Js(1.0), Js(1.0), Js(1.0), Js(0.0)]), Js(0.0)]), Js([Js(u'B'), Js(0.0), Js([Js(0.0), Js(2.0), Js(2.0), Js(1.0), Js(0.0)]), Js(0.0)]), Js([Js(u'G'), Js(0.0), Js([Js(1.0), Js(0.0), Js(2.0), Js(0.0), Js(2.0)]), Js(0.0)]), Js([Js(u'R'), Js(0.0), Js([Js(0.0), Js(1.0), Js(0.0), Js(2.0), Js(2.0)]), Js(0.0)]), Js([Js(u'W'), Js(0.0), Js([Js(2.0), Js(2.0), Js(0.0), Js(0.0), Js(1.0)]), Js(0.0)]), Js([Js(u'b'), Js(0.0), Js([Js(2.0), Js(0.0), Js(1.0), Js(2.0), Js(0.0)]), Js(0.0)]), Js([Js(u'B'), Js(0.0), Js([Js(0.0), Js(0.0), Js(0.0), Js(1.0), Js(2.0)]), Js(0.0)]), Js([Js(u'G'), Js(0.0), Js([Js(1.0), Js(0.0), Js(0.0), Js(2.0), Js(0.0)]), Js(0.0)]), Js([Js(u'R'), Js(0.0), Js([Js(2.0), Js(1.0), Js(0.0), Js(0.0), Js(0.0)]), Js(0.0)]), Js([Js(u'W'), Js(0.0), Js([Js(0.0), Js(0.0), Js(2.0), Js(0.0), Js(1.0)]), Js(0.0)]), Js([Js(u'b'), Js(0.0), Js([Js(0.0), Js(2.0), Js(1.0), Js(0.0), Js(0.0)]), Js(0.0)]), Js([Js(u'B'), Js(0.0), Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(3.0)]), Js(0.0)]), Js([Js(u'G'), Js(0.0), Js([Js(0.0), Js(0.0), Js(3.0), Js(0.0), Js(0.0)]), Js(0.0)]), Js([Js(u'R'), Js(0.0), Js([Js(0.0), Js(0.0), Js(0.0), Js(3.0), Js(0.0)]), Js(0.0)]), Js([Js(u'W'), Js(0.0), Js([Js(3.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0)]), Js(0.0)]), Js([Js(u'b'), Js(0.0), Js([Js(0.0), Js(3.0), Js(0.0), Js(0.0), Js(0.0)]), Js(0.0)]), Js([Js(u'B'), Js(0.0), Js([Js(1.0), Js(3.0), Js(1.0), Js(0.0), Js(0.0)]), Js(0.0)]), Js([Js(u'G'), Js(0.0), Js([Js(3.0), Js(1.0), Js(0.0), Js(1.0), Js(0.0)]), Js(0.0)]), Js([Js(u'R'), Js(0.0), Js([Js(0.0), Js(0.0), Js(1.0), Js(1.0), Js(3.0)]), Js(0.0)]), Js([Js(u'W'), Js(0.0), Js([Js(1.0), Js(0.0), Js(0.0), Js(3.0), Js(1.0)]), Js(0.0)]), Js([Js(u'b'), Js(0.0), Js([Js(0.0), Js(1.0), Js(3.0), Js(0.0), Js(1.0)]), Js(0.0)]), Js([Js(u'B'), Js(0.0), Js([Js(0.0), Js(2.0), Js(0.0), Js(0.0), Js(2.0)]), Js(0.0)]), Js([Js(u'G'), Js(0.0), Js([Js(2.0), Js(0.0), Js(2.0), Js(0.0), Js(0.0)]), Js(0.0)]), Js([Js(u'R'), Js(0.0), Js([Js(0.0), Js(0.0), Js(2.0), Js(2.0), Js(0.0)]), Js(0.0)]), Js([Js(u'W'), Js(0.0), Js([Js(2.0), Js(0.0), Js(0.0), Js(0.0), Js(2.0)]), Js(0.0)]), Js([Js(u'b'), Js(0.0), Js([Js(0.0), Js(2.0), Js(0.0), Js(2.0), Js(0.0)]), Js(0.0)])])]).callprop(u'reverse')
    return PyJs_LONG_4_()
PyJs_anonymous_3_._set_name(u'anonymous')
var.get(u'Deck').get(u'prototype').put(u'getCardStats', PyJs_anonymous_3_)


# Add lib to the module scope
deck = var.to_python()