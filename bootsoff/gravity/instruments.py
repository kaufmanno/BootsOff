import pandas as pd


def import_cg6(filename, **kwargs):
    """ Import data from CG6
    TODO: The GNSS file should first be merged with the CG-6 File"""

    sep = kwargs.pop('sep', '\t')
    corrections = kwargs.pop('corrections', {'TideCorr': 1, 'TiltCorr': 1, 'na': 0, 'TempCorr': 1, 'DriftCorr': 1})
    # will be used in combination with the code stored in the CG6-data
    keep = kwargs.pop('keep', 'all')

    df = pd.read_csv(filename, sep=sep)

    # Extract Correction codes
    df['CorrDriftCode'] = df['Corrections[drift-temp-na-tide-tilt]'] // 10000
    df['CorrTempCode'] = (df['Corrections[drift-temp-na-tide-tilt]'] % 10000) // 1000
    df['CorrNaCode'] = (df['Corrections[drift-temp-na-tide-tilt]'] % 1000) // 100
    df['CorrTideCode'] = (df['Corrections[drift-temp-na-tide-tilt]'] % 100) // 10
    df['CorrTiltCode'] = df['Corrections[drift-temp-na-tide-tilt]'] % 10

    df['InstrCorrGrav'] = df['RawGrav'] + corrections['TempCorr'] * df['CorrTempCode']*df['TempCorr'] \
                          + corrections['DriftCorr'] * df['CorrDriftCode'] * df['DriftCorr'] \
                          + corrections['TideCorr'] * df['CorrTideCode'] * df['TideCorr'] \
                          + corrections['TiltCorr'] * df['CorrTiltCode'] * df['TiltCorr'] # NOTE: There are no NaCorr column in the CG6-data
    df['datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], utc=True)
    df.drop('Unnamed: 0', axis=1, inplace=True)
    df.set_index('datetime', inplace=True)
    df.sort_index(inplace=True)
    if keep == 'all':
        keep = list(df.columns)
    return df[keep]