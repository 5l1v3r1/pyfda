# -*- coding: utf-8 -*-
#
# This file is part of the pyFDA project hosted at https://github.com/chipmuenk/pyfda
#
# Copyright © pyFDA Project Contributors
# Licensed under the terms of the MIT License
# (see file LICENSE in root directory for details)
#
# Taken from https://github.com/sriyash25/filter-blocks
# (c) Christopher Felton and Sriyash Caculo

from pyfda.filter_blocks.fda.fir import FilterFIR
import numpy as np


def test_fda_fir():
    """Test basic API parameter passing
    """
    coef = np.empty(100)
    coef.fill(8388607)
    hdlfilter = FilterFIR()
    b = [8388607, 8388607, 8388607, 8388607, 8388607]
    hdlfilter.set_coefficients(coeff_b=b)
    hdlfilter.set_word_format(
        coeff_w=(24, 23, 0), input_w=(24, 23, 0), output_w=(50, 23, 0)
    )
    hdlfilter.set_stimulus(coef)
    hdlfilter.run_sim()
    hdlfilter.convert(hdl='Verilog')


if __name__ == '__main__':
    test_fda_fir()
