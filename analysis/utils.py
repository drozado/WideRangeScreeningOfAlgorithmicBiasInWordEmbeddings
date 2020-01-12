import math
import numpy as np
import matplotlib.pyplot as plt #For graphics
import pandas as pd 
import sklearn.metrics
import sklearn
import matplotlib.colors as mcolors
import scipy.stats

       
# Some functions in this script were taken or adapted from from https://github.com/Computational-Content-Analysis-2018/Content-Analysis
# many thanks to the source for making their materials available online

def normalize(vector):
    normalized_vector = vector / np.linalg.norm(vector)
    return normalized_vector

def dimension(model, negatives, positives):
    diff = sum([normalize(model[x]) for x in positives if x in model.wv]) - sum([normalize(model[y]) for y in negatives if y in model.wv])
    for x in (positives+negatives):
        if x not in model.wv:
            print(x, " does not exist in model")
    return normalize(diff)

def dimensionN(model, negatives, positives):
	#it is important to normalize the result of the sums in order to prevent unbalanced poles with different
	#number of elements from skewing the resulting vector aggregate. This method is equivalent to determineAxisFromPerpendicularProjections
    diff = normalize(sum([normalize(model[x]) for x in positives if x in model.wv])) - normalize(sum([normalize(model[y]) for y in negatives if y in model.wv]))
    for x in (positives+negatives):
        if x not in model.wv:
            print(x, " does not exist in model")
    return normalize(diff)    

def vectorizeConstruct(model, construct):
    vectorConstruct = sum([normalize(model[x]) for x in construct])
    return normalize(vectorConstruct)

def getComponents(constructPole1,constructPole2,model):
    a = normalize(sum([normalize(model[x]) for x in constructPole1]))
    b = normalize(sum([normalize(model[x]) for x in constructPole2]))
    a1 = np.dot(a,normalize(b))*normalize(b)
    a2 = a-a1
    return normalize(a1),normalize(a2)
    
def dimensionByVector(model, negative, positive):
    diff = normalize(positive) - normalize(negative)
    return normalize(diff)    

def determineAxisFromPerpendicularProjections(model, constructPole1,constructPole2):
    constructPole1X, constructPole1Y = getComponents(constructPole1,constructPole2,model)
    constructPole2X, constructPole2Y = getComponents(constructPole2,constructPole1,model)
    Axis = dimensionByVector(model, constructPole1Y,constructPole2Y)    
    return Axis, constructPole1X, constructPole1Y, constructPole2X, constructPole2Y    

def makeDF(model, word_list,dimension,dimensionName):
    d=[]
    for word in word_list:
        d.append(sklearn.metrics.pairwise.cosine_similarity(model[word].reshape(1,-1), dimension.reshape(1,-1))[0][0])
    df = pd.DataFrame({dimensionName: d}, index = word_list)
    return df
    
   
def makeDF2D(model, word_list,dimension1,dimension1Name,dimension2,dimension2Name):
    d1Values=[]
    d2Values=[]
    for word in word_list:
        d1Values.append(sklearn.metrics.pairwise.cosine_similarity(model[word].reshape(1,-1), dimension1.reshape(1,-1))[0][0])
        d2Values.append(sklearn.metrics.pairwise.cosine_similarity(model[word].reshape(1,-1), dimension2.reshape(1,-1))[0][0])
    df = pd.DataFrame({dimension1Name: d1Values,dimension2Name: d2Values}, index = word_list)
    return df       
    
    
def calculateCorrelations(dataFrame,printFlag=True):
    spearmanCorr = scipy.stats.spearmanr(dataFrame['Axis'],dataFrame['RealValues'])
    pearsonCorr = scipy.stats.pearsonr(dataFrame['Axis'],dataFrame['RealValues'])
    if printFlag == True:
        print("Spearman: ", spearmanCorr)
        print("Pearson: ", pearsonCorr)
    return spearmanCorr,pearsonCorr

def make_colormap(seq):
    """Return a LinearSegmentedColormap
    seq: a sequence of floats and RGB-tuples. The floats should be increasing
    and in the interval (0,1).
    """
    seq = [(None,) * 3, 0.0] + list(seq) + [1.0, (None,) * 3]
    cdict = {'red': [], 'green': [], 'blue': []}
    for i, item in enumerate(seq):
        if isinstance(item, float):
            r1, g1, b1 = seq[i - 1]
            r2, g2, b2 = seq[i + 1]
            cdict['red'].append([item, r1, r2])
            cdict['green'].append([item, g1, g2])
            cdict['blue'].append([item, b1, b2])
    return mcolors.LinearSegmentedColormap('CustomMap', cdict)   

    
def truncate(number, digits) -> float:
    stepper = pow(10.0, digits)
    return math.trunc(stepper * number) / stepper
    
def pValueAdjustment(pValue):
    if pValue < 0.0001:
        return 'p<0.0001'
    elif pValue < 0.001:
        return 'p<0.001'
    elif pValue < 0.01:
        return 'p<0.01'
    elif pValue < 0.05:
        return 'p<0.05'
    else:
        return 'p='+str(pValue)    
        
def Coloring(Series):
    x = Series.values
    y = x-x.min()
    z = y/y.max()
    
    
    c = mcolors.ColorConverter().to_rgb
    rvb = make_colormap(
    #[c('red'), c('violet'), 0.33, c('violet'), c('blue'), 0.66, c('blue')])
    #[c('blue'), 0.33, c('violet'), 0.66, c('red')])
    [c('red'), 0.33, c('violet'), 0.66, c('blue')])
    
    
    #c = list(plt.cm.rainbow(z))
    #c = list(plt.cm.Dark2(z))
    #c = list(plt.cm.coolwarm(z))
    #c = list(plt.cm.seismic(z))
    #c = list(plt.cm.RdBu_r(z))
    c = list(rvb(z))
    return c
    
def PlotDimensionHOld(ax,df, dim,constructPole1,constructPole2,fontSize=35):
    ax.set_frame_on(False)
    ax.set_title(dim, fontsize = 30,  y=10.08)
    colors = Coloring(df[dim])
    for i, word in enumerate(df.index):
        #r=random.randint(1,50)*0.1
        ax.annotate(word, (df[dim][i],0), color = colors[i], alpha = 0.6, fontsize = fontSize, rotation=60)
#         if i%2==0:
#             ax.annotate(word, (df[dim][i],0.5), color = colors[i], alpha = 0.6, fontsize = 25, rotation=40)
#         else:
#             ax.annotate(word, (df[dim][i],0), color = colors[i], alpha = 0.6, fontsize = 25, rotation=40)

    MaxY = df[dim].max()
    MinY = df[dim].min()
    
    
    bbox_props = dict(boxstyle="square", fc="blue", ec="blue",alpha=0.5, lw=0)
    pole1Text = constructPole1[0]#'\n'.join(constructPole1)
    #pole1Text = '\n'.join(constructPole1)
    ax.annotate(pole1Text, xy=(MinY,0),xytext=(MinY,2), color = "white", alpha = 1, fontsize = 20, rotation=0,bbox=bbox_props)
    bbox_props = dict(boxstyle="square", fc="red", ec="red", alpha=0.5,lw=0)
    pole2Text = constructPole2[0] #'\n'.join(constructPole1)
    ax.annotate(pole2Text, xy=(MaxY,1),xytext=(MaxY,2), color = "white", alpha = 1, fontsize = 20, rotation=0,bbox=bbox_props)    
    
    plt.xlim(MinY,MaxY)
    plt.axhline(0, color='black')
    plt.yticks(())
    plt.xticks(())


def PlotDimensionH(ax,df, dim,constructPole1,constructPole2,fontSize=35,pole1Name=None,pole2Name=None,title="Axis"):
    ax.set_frame_on(False)
    ax.set_title(title, fontsize = 30,  y=10.08)
    colors = Coloring(df[dim])
    for i, word in enumerate(df.index):
        #r=random.randint(1,50)*0.1
        ax.annotate(word, (df[dim][i],0), color = colors[i], alpha = 0.6, fontsize = fontSize, rotation=60)
#         if i%2==0:
#             ax.annotate(word, (df[dim][i],0.5), color = colors[i], alpha = 0.6, fontsize = 25, rotation=40)
#         else:
#             ax.annotate(word, (df[dim][i],0), color = colors[i], alpha = 0.6, fontsize = 25, rotation=40)

    MaxY = df[dim].max()
    MinY = df[dim].min()
    
    
    bbox_props = dict(boxstyle="square", fc="red", ec="red",alpha=0.5, lw=0)
    if pole1Name==None:
        pole1Text = constructPole1[0]#'\n'.join(constructPole1)
    else:
        pole1Text = pole1Name
    #pole1Text = '\n'.join(constructPole1)
    ax.annotate(pole1Text, xy=(MinY,0),xytext=(MinY,2), color = "white", alpha = 1, fontsize = 20, rotation=0,bbox=bbox_props)
    bbox_props = dict(boxstyle="square", fc="blue", ec="blue", alpha=0.5,lw=0)
    if pole2Name==None:
        pole2Text = constructPole2[0]#'\n'.join(constructPole1)
    else:
        pole2Text = pole2Name
    ax.annotate(pole2Text, xy=(MaxY,1),xytext=(MaxY,2), color = "white", alpha = 1, fontsize = 20, rotation=0,bbox=bbox_props)    
    
    plt.xlim(MinY,MaxY)
    plt.axhline(0, color='black')
    plt.yticks(())
    plt.xticks(())







def checkConstructs(model,constructPole1,constructPole2,Axis,topn=10):
        print("Checking Constructs:")
        print("constructPole1: ", constructPole1)
        print("constructPole2: ", constructPole2)
        similarToConstruct1 = model.wv.similar_by_vector(vectorizeConstruct(model,constructPole1),topn)
        similarToConstruct2 = model.wv.similar_by_vector(vectorizeConstruct(model,constructPole2),topn)
        similarToPositiveAxis = model.wv.similar_by_vector(Axis,topn)
        similarToNegativeAxis = model.wv.similar_by_vector(-Axis,topn)
        similarToconstructPole1_0PlusAxis = model.wv.similar_by_vector(model.wv[constructPole1[0]]+Axis,topn)
        similarToconstructPole2_0MinusAxis = model.wv.similar_by_vector(model.wv[constructPole2[0]]-Axis,topn)
        model.wv.similar_by_vector(model.wv['man']+Axis,topn)
        listsOfSimilarities = [similarToConstruct1,similarToConstruct2,similarToPositiveAxis,similarToNegativeAxis,
                              similarToconstructPole1_0PlusAxis,similarToconstructPole2_0MinusAxis]
        names = ['similarToConstruct1','similarToConstruct2','similarToPositiveAxis','similarToNegativeAxis',
                'similarToconstructPole1_0PlusAxis','similarToconstructPole2_0MinusAxis']
        for i,listOfSimilarities in enumerate(listsOfSimilarities):
            print(names[i],end='\n')
            for w in listOfSimilarities:
                print(w,end=' ')
            print("\n---",end='\n')
            
def checkPerpendicularProjections(model,constructPole1,constructPole2,Axis,constructPole1X,                                    constructPole1Y,constructPole2X,constructPole2Y,topn=10):
        print("Checking Perpendicular Projections:")
        print("constructPole1: ", constructPole1)
        print("constructPole2: ", constructPole2)    
        similarToConstruct1Y = model.wv.similar_by_vector(constructPole1Y,topn)
        similarToConstruct1X = model.wv.similar_by_vector(constructPole1X,topn)
        similarToConstruct2Y = model.wv.similar_by_vector(constructPole2Y,topn)
        similarToConstruct2X = model.wv.similar_by_vector(constructPole2X,topn)
        similarToPositiveAxis = model.wv.similar_by_vector(Axis,topn)
        similarToNegativeAxis = model.wv.similar_by_vector(-Axis,topn)
        similarToconstructPole1_0PlusAxis = model.wv.similar_by_vector(model.wv[constructPole1[0]]+Axis,topn)
        similarToconstructPole2_0MinusAxis = model.wv.similar_by_vector(model.wv[constructPole2[0]]-Axis,topn)
        
        listsOfSimilarities = [similarToConstruct1Y,similarToConstruct1X,similarToConstruct2Y,similarToConstruct2X,
                               similarToPositiveAxis,similarToNegativeAxis,
                               similarToconstructPole1_0PlusAxis,similarToconstructPole2_0MinusAxis]
        names = ['similarToConstruct1Y','similarToConstruct1X','similarToConstruct2Y','similarToConstruct2X',
                               'similarToPositiveAxis','similarToNegativeAxis',
                               'similarToconstructPole1_0PlusAxis','similarToconstructPole2_0MinusAxis']
        
        for i,listOfSimilarities in enumerate(listsOfSimilarities):
            print(names[i],end='\n')
            for w in listOfSimilarities:
                print(w,end=' ')
            print("\n---",end='\n')           

def realDataFilter(model,RealDataTemp,printMissingData=1):
    RealData={}
    missing =[]
    for k in RealDataTemp.keys():
        if k in model.wv:
            RealData[k]=RealDataTemp[k]
        else:
            missing.append(k)
    if printMissingData==1:
        print("RealData missing words in model", missing)
    return RealData

def constructsFilter(model,constructPole1,constructPole2,printFlag=True):
    constructPole1Filtered=[w for w in constructPole1 if w in model.wv]
    constructPole2Filtered=[w for w in constructPole2 if w in model.wv]
    constructPole1Missing=[w for w in constructPole1 if w not in model.wv]
    constructPole2Missing=[w for w in constructPole2 if w not in model.wv]
    if printFlag==True:
        print("Missing words from constructPole1", constructPole1Missing)
        print("Missing words from constructPole2", constructPole2Missing)
    return constructPole1Filtered,constructPole2Filtered

def replaceUnderscoreForDash(constructPole1,constructPole2,RealData):
    constructPole1Updated=[]
    constructPole2Updated=[]
    RealDataUpdated={}
    constructPole1Updated= [w.replace('_','-') for w in constructPole1]
    constructPole2Updated= [w.replace('_','-') for w in constructPole2]
    for k in RealData.keys():
        RealDataUpdated[k.replace('_','-')]=RealData[k]
    return constructPole1Updated,constructPole2Updated,RealDataUpdated    
    
def dimensionOld(model, negatives, positives):
    diff = sum([normalize(model[x]) for x in positives]) - sum([normalize(model[y]) for y in negatives])
    return normalize(diff)    
    
    