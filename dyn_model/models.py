"""
Class objects for the dyn_model calculations
"""

# Modules
# ------------------------------------------------------------------------------

import json
import pandas as pd
import numpy as np

# Class Objects
# ------------------------------------------------------------------------------


class DataModel:
    """
    Data from battery script tests. Requires the Script class which reads the
    csv file and assigns the data to class attributes.
    """

    def __init__(self, temp, csvfiles):
        """
        Initialize from script data.
        """
        self.temp = temp
        self.s1 = Script(csvfiles[0])
        self.s2 = Script(csvfiles[1])
        self.s3 = Script(csvfiles[2])


class Script:
    """
    Object to represent script data.
    """

    def __init__(self, csvfile):
        """
        Initialize with data from csv file.
        """
        df = pd.read_csv(csvfile)
        time = df['time'].values
        step = df[' step'].values
        current = df[' current'].values
        voltage = df[' voltage'].values
        chgAh = df[' chgAh'].values
        disAh = df[' disAh'].values

        self.time = time
        self.step = step
        self.current = current
        self.voltage = voltage
        self.chgAh = chgAh
        self.disAh = disAh


class ModelOcv:
    """
    Model representing OCV results.
    """
    # pylint: disable=too-many-instance-attributes

    def __init__(self, OCV0, OCVrel, SOC, OCV, SOC0, SOCrel, OCVeta, OCVQ):
        self.OCV0 = np.array(OCV0)
        self.OCVrel = np.array(OCVrel)
        self.SOC = np.array(SOC)
        self.OCV = np.array(OCV)
        self.SOC0 = np.array(SOC0)
        self.SOCrel = np.array(SOCrel)
        self.OCVeta = np.array(OCVeta)
        self.OCVQ = np.array(OCVQ)

    @classmethod
    def load(cls, pfile):
        """
        Load attributes from json file where pfile is string representing
        path to the json file.
        """
        ocv = json.load(open(pfile, 'r'))
        return cls(ocv['OCV0'], ocv['OCVrel'], ocv['SOC'], ocv['OCV'], ocv['SOC0'], ocv['SOCrel'], ocv['OCVeta'], ocv['OCVQ'])


class ModelDyn:
    """
    Model representing results from the dynamic calculations.
    """
    # pylint: disable=too-many-instance-attributes

    def __init__(self):
        self.temps = None
        self.etaParam = None
        self.QParam = None
        self.GParam = None
        self.M0Param = None
        self.MParam = None
        self.R0Param = None
        self.RCParam = None
        self.RParam = None
        self.SOC = None
        self.OCV0 = None
        self.OCVrel = None

    # def __init__(self, temps, etaParam, QParam, GParam, M0Param, MParam, R0Param, RCParam, RParam, SOC, OCV0, OCVrel):
    #     self.temps = np.array(temps)
    #     self.etaParam = np.array(etaParam)
    #     self.QParam = np.array(QParam)
    #     self.GParam = np.array(GParam)
    #     self.M0Param = np.array(M0Param)
    #     self.MParam = np.array(MParam)
    #     self.R0Param = np.array(R0Param)
    #     self.RCParam = np.array(RCParam)
    #     self.RParam = np.array(RParam)
    #     self.SOC = np.array(SOC)
    #     self.OCV0 = np.array(OCV0)
    #     self.OCVrel = np.array(OCVrel)

    def etaParam_at_T(self, temp):
        """Get eta at specified temperatures."""
        index = np.where(self.temps == temp)[0]
        return self.etaParam[index]

    def QParam_at_T(self, temp):
        """Get Q at specified temperatures."""
        index = np.where(self.temps == temp)[0]
        return self.QParam[index]

    def GParam_at_T(self, temp):
        """Get G at sepecified temperatures."""
        index = np.where(self.temps == temp)[0]
        return self. GParam[index]

    def M0Param_at_T(self, temp):
        """Get M0 at specified temperatures."""
        index = np.where(self.temps == temp)[0]
        return self.M0Param[index]

    def MParam_at_T(self, temp):
        """Get M at specified temperatures."""
        index = np.where(self.temps == temp)[0]
        return self.MParam[index]

    def R0Param_at_T(self, temp):
        """Get R0 at specified temperatures."""
        index = np.where(self.temps == temp)[0]
        return self.R0Param[index]

    def RCParam_at_T(self, temp):
        """Get RC at specified temperatures."""
        index = np.where(self.temps == temp)[0]
        return self.RCParam[index]

    def RParam_at_T(self, temp):
        """Get R at specified temperatures."""
        index = np.where(self.temps == temp)[0]
        return self.RParam[index]

    @classmethod
    def load(cls, pfile):
        """
        Load attributes from json file where pfile is string representing
        path to the json file.
        """
        dyn = json.load(open(pfile, 'r'))
        return cls(dyn['temps'], dyn['etaParam'], dyn['QParam'], dyn['GParam'], dyn['M0Param'], dyn['MParam'], dyn['R0Param'], dyn['RCParam'], dyn['RParam'], dyn['SOC'], dyn['OCV0'], dyn['OCVrel'])
