# -*- coding: utf-8 -*-
'''
Created on 11 Sep 2015

@author: Kimon Tsitsikas

Copyright © 2015 Kimon Tsitsikas, Delmic

This file is part of Odemis.

Odemis is free software: you can redistribute it and/or modify it under the terms
of the GNU General Public License version 2 as published by the Free Software
Foundation.

Odemis is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
Odemis. If not, see http://www.gnu.org/licenses/.
'''
from __future__ import division, absolute_import

import logging
from odemis import model
from past.builtins import long

class Light(model.Emitter):
    """
    Bright light component. Just pretends to be always on with wide spectrum
    emitted (white).
    """
    def __init__(self, name, role, **kwargs):
        # TODO: allow the user to indicate the power and the spectrum via args?
        # This will create the .powerSupply VA
        model.Emitter.__init__(self, name, role, **kwargs)
        self.powerSupply.value = False  # immediately turn it off

        self._shape = ()
        self.power = model.ListContinuous([0., ], ((0.,), (10.,)), unit="W", cls=(int, long, float),)
        self.power.subscribe(self._updatePower)
        # just one band: white
        # TODO: update spectra VA to support the actual spectra of the lamp
        self.spectra = model.ListVA([(380e-9, 390e-9, 560e-9, 730e-9, 740e-9)],
                                    unit="m", readonly=True)

    def _updatePower(self, value):
        # Set powerSupply VA based on the power value (True in case of max,
        # False in case of min)
        pw = value[0]
        self.powerSupply.value = (pw == self.power.range[1])
