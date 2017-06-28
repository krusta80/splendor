__all__ = ['noble']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([u'shuffle', u'common', u'nobleStats'])
var.put(u'common', var.get(u'require')(Js(u'./common.js')))
var.put(u'shuffle', var.get(u'require')(Js(u'shuffle-array')))
var.put(u'nobleStats', Js([Js([Js(4.0), Js(0.0), Js(0.0), Js(4.0), Js(0.0)]), Js([Js(0.0), Js(0.0), Js(4.0), Js(0.0), Js(4.0)]), Js([Js(4.0), Js(4.0), Js(0.0), Js(0.0), Js(0.0)]), Js([Js(0.0), Js(4.0), Js(4.0), Js(0.0), Js(0.0)]), Js([Js(0.0), Js(0.0), Js(0.0), Js(4.0), Js(4.0)]), Js([Js(0.0), Js(0.0), Js(3.0), Js(3.0), Js(3.0)]), Js([Js(3.0), Js(3.0), Js(3.0), Js(0.0), Js(0.0)]), Js([Js(3.0), Js(3.0), Js(0.0), Js(3.0), Js(0.0)]), Js([Js(3.0), Js(0.0), Js(0.0), Js(3.0), Js(3.0)]), Js([Js(0.0), Js(3.0), Js(3.0), Js(0.0), Js(3.0)])]))
@Js
def PyJs_anonymous_1_(nobleStats, playerStats, this, arguments, var=var):
    var = Scope({u'this':this, u'playerStats':playerStats, u'arguments':arguments, u'nobleStats':nobleStats}, var)
    var.registers([u'i', u'playerStats', u'nobleStats'])
    #for JS loop
    var.put(u'i', Js(0.0))
    while (var.get(u'i')<Js(5.0)):
        try:
            if (var.get(u'nobleStats').get(var.get(u'i'))>var.get(u'playerStats').get(var.get(u'i'))):
                return Js(False)
        finally:
                (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))
    return var.get(u'true')
PyJs_anonymous_1_._set_name(u'anonymous')
PyJs_Object_0_ = Js({u'nobles':var.get(u'shuffle')(var.get(u'nobleStats')),u'canGetNoble':PyJs_anonymous_1_})
var.get(u'module').put(u'exports', PyJs_Object_0_)
pass


# Add lib to the module scope
noble = var.to_python()