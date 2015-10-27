"""
Try to load all of the MODFLOW examples in ../examples/data/mf2005_test.
These are the examples that are distributed with MODFLOW-2005.
"""

import os
import flopy
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def test_modflow_load():
    pth = os.path.join('..', 'examples', 'data', 'mf2005_test')
    namfiles = [namfile for namfile in os.listdir(pth) if namfile.endswith('.nam')]
    for namfile in namfiles:
        m = flopy.modflow.Modflow.load(namfile, model_ws=pth, verbose=True)
        assert m, 'Could not load namefile {}'.format(namfile)
        m.plot()
        plt.close("all")


    return


if __name__ == '__main__':
    test_modflow_load()
