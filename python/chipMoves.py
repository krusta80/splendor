__all__ = ['chipMoves']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([u'doubleChipArray', u'extractChips', u'hasThreeOrFewerBits', u'giveBackArray', u'generateSingleChipPileArray', u'interweaveZeroes', u'generateGiveBackCombos', u'countChips', u'generateGiveBacks', u'findGiveBackCombos', u'getSingles', u'generateSingleChipCombos', u'generateDoubleChipCombos', u'getDoubles', u'singleChipArray', u'generateDoubleChipPileArray'])
@Js
def PyJsHoisted_extractChips_(x, this, arguments, var=var):
    var = Scope({u'this':this, u'x':x, u'arguments':arguments}, var)
    var.registers([u'i', u'x', u'j', u'chips'])
    var.put(u'chips', Js([]))
    #for JS loop
    var.put(u'i', Js(0.0))
    while (var.get(u'i')<Js(6.0)):
        try:
            #for JS loop
            var.put(u'j', Js(0.0))
            while (var.get(u'j')<(var.get(u'x')&Js(7.0))):
                try:
                    var.get(u'chips').callprop(u'push', (Js(1.0)<<(Js(3.0)*var.get(u'i'))))
                finally:
                        (var.put(u'j',Js(var.get(u'j').to_number())+Js(1))-Js(1))
            var.put(u'x', (var.get(u'x')>>Js(3.0)))
        finally:
                (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))
    return var.get(u'chips')
PyJsHoisted_extractChips_.func_name = u'extractChips'
var.put(u'extractChips', PyJsHoisted_extractChips_)
@Js
def PyJsHoisted_hasThreeOrFewerBits_(i, this, arguments, var=var):
    var = Scope({u'i':i, u'this':this, u'arguments':arguments}, var)
    var.registers([u'i', u'bitCount'])
    var.put(u'bitCount', Js(0.0))
    while (var.get(u'i')>Js(0.0)):
        var.put(u'bitCount', (var.get(u'i')&Js(1.0)), u'+')
        var.put(u'i', (var.get(u'i')>>Js(1.0)))
    return (var.get(u'bitCount')<=Js(3.0))
PyJsHoisted_hasThreeOrFewerBits_.func_name = u'hasThreeOrFewerBits'
var.put(u'hasThreeOrFewerBits', PyJsHoisted_hasThreeOrFewerBits_)
@Js
def PyJsHoisted_generateSingleChipPileArray_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([u'x', u'singleChipPileCombos'])
    var.put(u'singleChipPileCombos', Js([]))
    #for JS loop
    var.put(u'x', Js(0.0))
    while (var.get(u'x')<Js(32.0)):
        try:
            var.get(u'singleChipPileCombos').callprop(u'push', var.get(u'generateSingleChipCombos')(var.get(u'x')))
        finally:
                (var.put(u'x',Js(var.get(u'x').to_number())+Js(1))-Js(1))
    return var.get(u'singleChipPileCombos')
PyJsHoisted_generateSingleChipPileArray_.func_name = u'generateSingleChipPileArray'
var.put(u'generateSingleChipPileArray', PyJsHoisted_generateSingleChipPileArray_)
@Js
def PyJsHoisted_interweaveZeroes_(i, this, arguments, var=var):
    var = Scope({u'i':i, u'this':this, u'arguments':arguments}, var)
    var.registers([u'i', u'interwoven', u'maskBit'])
    var.put(u'interwoven', Js(0.0))
    var.put(u'maskBit', Js(0.0))
    while (var.get(u'i')>Js(0.0)):
        var.put(u'interwoven', (var.get(u'interwoven')|((var.get(u'i')&Js(1.0))<<(Js(3.0)*(var.put(u'maskBit',Js(var.get(u'maskBit').to_number())+Js(1))-Js(1))))))
        var.put(u'i', (var.get(u'i')>>Js(1.0)))
    return var.get(u'interwoven')
PyJsHoisted_interweaveZeroes_.func_name = u'interweaveZeroes'
var.put(u'interweaveZeroes', PyJsHoisted_interweaveZeroes_)
@Js
def PyJsHoisted_generateGiveBackCombos_(x, this, arguments, var=var):
    var = Scope({u'this':this, u'x':x, u'arguments':arguments}, var)
    var.registers([u'x', u'giveBackCombos'])
    PyJs_Object_5_ = Js({})
    var.put(u'giveBackCombos', PyJs_Object_5_)
    var.get(u'findGiveBackCombos')(var.get(u'extractChips')(var.get(u'x')), Js(0.0), Js(0.0), (var.get(u'countChips')(var.get(u'x'))-Js(10.0)), var.get(u'giveBackCombos'))
    return var.get(u'Object').callprop(u'keys', var.get(u'giveBackCombos'))
PyJsHoisted_generateGiveBackCombos_.func_name = u'generateGiveBackCombos'
var.put(u'generateGiveBackCombos', PyJsHoisted_generateGiveBackCombos_)
@Js
def PyJsHoisted_countChips_(x, this, arguments, var=var):
    var = Scope({u'this':this, u'x':x, u'arguments':arguments}, var)
    var.registers([u'i', u'totalChips', u'x'])
    var.put(u'totalChips', Js(0.0))
    #for JS loop
    var.put(u'i', Js(0.0))
    while (var.get(u'i')<Js(6.0)):
        try:
            var.put(u'totalChips', (var.get(u'x')&Js(7.0)), u'+')
            var.put(u'x', (var.get(u'x')>>Js(3.0)))
        finally:
                (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))
    return var.get(u'totalChips')
PyJsHoisted_countChips_.func_name = u'countChips'
var.put(u'countChips', PyJsHoisted_countChips_)
@Js
def PyJsHoisted_generateGiveBacks_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([u'x', u'chipCount', u'giveBacks'])
    var.put(u'giveBacks', Js([]))
    pass
    #for JS loop
    var.put(u'x', Js(0.0))
    while (var.get(u'x')<((Js(1.0)<<Js(18.0))-Js(2.0))):
        try:
            var.put(u'chipCount', var.get(u'countChips')(var.get(u'x')))
            if ((var.get(u'chipCount')>=Js(11.0)) and (var.get(u'chipCount')<=Js(13.0))):
                var.get(u'giveBacks').put(var.get(u'x'), var.get(u'generateGiveBackCombos')(var.get(u'x')))
        finally:
                (var.put(u'x',Js(var.get(u'x').to_number())+Js(1))-Js(1))
    return var.get(u'giveBacks')
PyJsHoisted_generateGiveBacks_.func_name = u'generateGiveBacks'
var.put(u'generateGiveBacks', PyJsHoisted_generateGiveBacks_)
@Js
def PyJsHoisted_findGiveBackCombos_(chips, nextChipIndex, combo, overflow, giveBackCombos, this, arguments, var=var):
    var = Scope({u'arguments':arguments, u'nextChipIndex':nextChipIndex, u'combo':combo, u'this':this, u'overflow':overflow, u'chips':chips, u'giveBackCombos':giveBackCombos}, var)
    var.registers([u'nextChipIndex', u'i', u'combo', u'overflow', u'chips', u'giveBackCombos'])
    if (var.get(u'overflow')<=Js(0.0)):
        return var.get(u'giveBackCombos').put(var.get(u'combo'), var.get(u'combo'))
    #for JS loop
    var.put(u'i', var.get(u'nextChipIndex'))
    while (var.get(u'i')<((var.get(u'chips').get(u'length')-var.get(u'overflow'))+Js(1.0))):
        try:
            var.get(u'findGiveBackCombos')(var.get(u'chips'), (var.get(u'i')+Js(1.0)), (var.get(u'combo')+var.get(u'chips').get(var.get(u'i'))), (var.get(u'overflow')-Js(1.0)), var.get(u'giveBackCombos'))
        finally:
                (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))
PyJsHoisted_findGiveBackCombos_.func_name = u'findGiveBackCombos'
var.put(u'findGiveBackCombos', PyJsHoisted_findGiveBackCombos_)
@Js
def PyJsHoisted_getSingles_(x, this, arguments, var=var):
    var = Scope({u'this':this, u'x':x, u'arguments':arguments}, var)
    var.registers([u'singles', u'x', u'colorIndex'])
    var.put(u'singles', Js(0.0))
    #for JS loop
    var.put(u'colorIndex', Js(0.0))
    while (var.get(u'colorIndex')<Js(5.0)):
        try:
            var.put(u'singles', (var.get(u'singles')<<Js(1.0)))
            if ((var.get(u'x')&Js(7.0))>Js(0.0)):
                (var.put(u'singles',Js(var.get(u'singles').to_number())+Js(1))-Js(1))
            var.put(u'x', (var.get(u'x')>>Js(3.0)))
        finally:
                (var.put(u'colorIndex',Js(var.get(u'colorIndex').to_number())+Js(1))-Js(1))
    return var.get(u'singles')
PyJsHoisted_getSingles_.func_name = u'getSingles'
var.put(u'getSingles', PyJsHoisted_getSingles_)
@Js
def PyJsHoisted_generateSingleChipCombos_(x, this, arguments, var=var):
    var = Scope({u'this':this, u'x':x, u'arguments':arguments}, var)
    var.registers([u'i', u'x', u'singleChipCombos'])
    var.put(u'singleChipCombos', Js([]))
    #for JS loop
    var.put(u'i', Js(0.0))
    while (var.get(u'i')<=var.get(u'x')):
        try:
            if var.get(u'hasThreeOrFewerBits')(var.get(u'i')):
                var.get(u'singleChipCombos').callprop(u'push', var.get(u'interweaveZeroes')(var.get(u'i')))
        finally:
                (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))
    return var.get(u'singleChipCombos')
PyJsHoisted_generateSingleChipCombos_.func_name = u'generateSingleChipCombos'
var.put(u'generateSingleChipCombos', PyJsHoisted_generateSingleChipCombos_)
@Js
def PyJsHoisted_generateDoubleChipCombos_(x, this, arguments, var=var):
    var = Scope({u'this':this, u'x':x, u'arguments':arguments}, var)
    var.registers([u'i', u'x', u'doubleChipCombos'])
    var.put(u'doubleChipCombos', Js([]))
    #for JS loop
    var.put(u'i', Js(0.0))
    while (var.get(u'i')<Js(5.0)):
        try:
            if (var.get(u'x')&((Js(1.0)<<var.get(u'i'))>Js(0.0))):
                var.get(u'doubleChipCombos').callprop(u'push', (Js(1.0)<<((Js(3.0)*var.get(u'i'))+Js(1.0))))
        finally:
                (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))
    return var.get(u'doubleChipCombos')
PyJsHoisted_generateDoubleChipCombos_.func_name = u'generateDoubleChipCombos'
var.put(u'generateDoubleChipCombos', PyJsHoisted_generateDoubleChipCombos_)
@Js
def PyJsHoisted_getDoubles_(x, this, arguments, var=var):
    var = Scope({u'this':this, u'x':x, u'arguments':arguments}, var)
    var.registers([u'doubles', u'colorIndex', u'x'])
    var.put(u'doubles', Js(0.0))
    #for JS loop
    var.put(u'colorIndex', Js(0.0))
    while (var.get(u'colorIndex')<Js(5.0)):
        try:
            var.put(u'doubles', (var.get(u'doubles')<<Js(1.0)))
            if ((var.get(u'x')&Js(7.0))>Js(3.0)):
                (var.put(u'doubles',Js(var.get(u'doubles').to_number())+Js(1))-Js(1))
            var.put(u'x', (var.get(u'x')>>Js(3.0)))
        finally:
                (var.put(u'colorIndex',Js(var.get(u'colorIndex').to_number())+Js(1))-Js(1))
    return var.get(u'doubles')
PyJsHoisted_getDoubles_.func_name = u'getDoubles'
var.put(u'getDoubles', PyJsHoisted_getDoubles_)
@Js
def PyJsHoisted_generateDoubleChipPileArray_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([u'doubleChipPileCombos', u'x'])
    var.put(u'doubleChipPileCombos', Js([]))
    #for JS loop
    var.put(u'x', Js(0.0))
    while (var.get(u'x')<Js(32.0)):
        try:
            var.get(u'doubleChipPileCombos').callprop(u'push', var.get(u'generateDoubleChipCombos')(var.get(u'x')))
        finally:
                (var.put(u'x',Js(var.get(u'x').to_number())+Js(1))-Js(1))
    return var.get(u'doubleChipPileCombos')
PyJsHoisted_generateDoubleChipPileArray_.func_name = u'generateDoubleChipPileArray'
var.put(u'generateDoubleChipPileArray', PyJsHoisted_generateDoubleChipPileArray_)
var.put(u'singleChipArray', var.get(u'generateSingleChipPileArray')())
var.put(u'doubleChipArray', var.get(u'generateDoubleChipPileArray')())
var.put(u'giveBackArray', var.get(u'generateGiveBacks')())
@Js
def PyJs_anonymous_1_(middleChipsCount, playerChipsCount, this, arguments, var=var):
    var = Scope({u'this':this, u'middleChipsCount':middleChipsCount, u'arguments':arguments, u'playerChipsCount':playerChipsCount}, var)
    var.registers([u'middleChipsCount', u'combinedTakeAndGiveBack', u'combinedTakeArray', u'playerChipsCount'])
    var.put(u'combinedTakeAndGiveBack', Js([]))
    var.put(u'combinedTakeArray', var.get(u'singleChipArray').get(var.get(u'getSingles')(var.get(u'middleChipsCount'))).callprop(u'concat', var.get(u'doubleChipArray').get(var.get(u'getDoubles')(var.get(u'middleChipsCount')))))
    @Js
    def PyJs_anonymous_2_(takeOption, this, arguments, var=var):
        var = Scope({u'takeOption':takeOption, u'this':this, u'arguments':arguments}, var)
        var.registers([u'takeOption', u'giveBackOptions'])
        var.put(u'giveBackOptions', var.get(u'giveBackArray').get((var.get(u'playerChipsCount')+var.get(u'takeOption'))))
        if var.get(u'giveBackOptions').neg():
            return var.get(u'combinedTakeAndGiveBack').callprop(u'push', ((var.get(u'takeOption')+Js(u','))+Js(0.0)))
        @Js
        def PyJs_anonymous_3_(giveBackOption, this, arguments, var=var):
            var = Scope({u'this':this, u'arguments':arguments, u'giveBackOption':giveBackOption}, var)
            var.registers([u'giveBackOption'])
            if PyJsStrictEq((var.get(u'takeOption')&var.get(u'giveBackOption')),Js(0.0)):
                var.get(u'combinedTakeAndGiveBack').callprop(u'push', ((var.get(u'takeOption')+Js(u','))+var.get(u'giveBackOption')))
        PyJs_anonymous_3_._set_name(u'anonymous')
        var.get(u'giveBackOptions').callprop(u'forEach', PyJs_anonymous_3_)
    PyJs_anonymous_2_._set_name(u'anonymous')
    var.get(u'combinedTakeArray').callprop(u'forEach', PyJs_anonymous_2_)
    return var.get(u'combinedTakeAndGiveBack')
PyJs_anonymous_1_._set_name(u'anonymous')
@Js
def PyJs_anonymous_4_(middleChipsCount, playerChipsCount, this, arguments, var=var):
    var = Scope({u'this':this, u'middleChipsCount':middleChipsCount, u'arguments':arguments, u'playerChipsCount':playerChipsCount}, var)
    var.registers([u'middleChipsCount', u'playerChipsCount', u'colorIndex', u'take', u'options'])
    var.put(u'take', ((var.get(u'middleChipsCount')>>Js(15.0))&Js(1.0)))
    var.put(u'options', Js([]))
    if PyJsStrictEq(var.get(u'take'),Js(0.0)):
        return Js([Js(u'0,0')])
    else:
        if (var.get(u'countChips')(var.get(u'playerChipsCount'))<Js(10.0)):
            return Js([((Js(1.0)<<Js(15.0))+Js(u',0'))])
    #for JS loop
    var.put(u'colorIndex', Js(0.0))
    while (var.get(u'colorIndex')<Js(5.0)):
        try:
            if ((var.get(u'playerChipsCount')&(Js(7.0)<<(Js(3.0)*var.get(u'colorIndex'))))>Js(0.0)):
                var.get(u'options').callprop(u'push', (((Js(1.0)<<Js(15.0))+Js(u','))+(Js(1.0)<<(Js(3.0)*var.get(u'colorIndex')))))
        finally:
                (var.put(u'colorIndex',Js(var.get(u'colorIndex').to_number())+Js(1))-Js(1))
    return var.get(u'options')
PyJs_anonymous_4_._set_name(u'anonymous')
PyJs_Object_0_ = Js({u'getChipTakingOptions':PyJs_anonymous_1_,u'getReserveOptions':PyJs_anonymous_4_})
var.get(u'module').put(u'exports', PyJs_Object_0_)
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass


# Add lib to the module scope
chipMoves = var.to_python()