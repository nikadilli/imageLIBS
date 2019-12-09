import pandas as pd

float_conv = lambda x: float(str(x).replace(',','.'))

def read_libs(path):
    data = pd.read_csv(path, 
                       delimiter=';', 
                       skipfooter=3, 
                       engine='python',
                       converters={0:float_conv},
                       usecols=[0,2,3])

    data.columns=['z', 'x', 'y']
    return data

def get_size(data):
    xmax = data.x.max()
    ymax = data.y.max()
    return (ymax, xmax)

def export(matrix, savename=None):
    m = pd.DataFrame(data=matrix,
                     index=[i for i in range(matrix.shape[0])],
                     columns=[i for i in range(matrix.shape[1])])
    if savename is not None:
        m.to_excel(savename)
        return
    return m
