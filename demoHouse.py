import numpy as np
import FactorBP as FB
import scipy.io as sio
import matlab.engine
import time
eng = matlab.engine.start_matlab()

def ComputeAccurancy(Decode, gTruth, NofInliers):
    Ccnt = 0
    for i in range(NofInliers):
        if(Decode[i] == gTruth[i]):
            Ccnt += 1
    return 1.0 * Ccnt / NofInliers

def LoadHouse():
    res = np.zeros([111, 30, 2])
    for i in range(1,112):
        res[i-1] = np.loadtxt('data/cmum/house/label/house%d' %i)
    return res

HouseData = LoadHouse()
start = 0
end = 92
baseline = 90
NofAlgorithms = 9
AlgorithmNames=['Ours', 'BCA', 'BCA-MP', 'BCA-IPFP', 'HGM', 'RRWHM', 'TM', 'OursPW', 'Ours-BCA']


Accuracy = np.zeros([NofAlgorithms, end - baseline - start])
Rtime = np.zeros([NofAlgorithms, end - baseline - start])
Obj = np.zeros([NofAlgorithms, end - baseline - start])
np.random.seed(123456)
for ImageI in range(start, end - baseline):
    PT1 = np.copy(HouseData[ImageI])
    PT2 = np.copy(HouseData[ImageI+baseline])
    NofNodes = 30
    gTruth = np.random.permutation(NofNodes)
    PT1 = PT1[gTruth, :]
    PF1 = np.zeros([NofNodes,1])
    PF2 = np.zeros([NofNodes,2])
    MG1 = FB.MatchingGraph(PT1[0:NofNodes], PF1[0:NofNodes])
    MG2 = FB.MatchingGraph(PT2[0:NofNodes], PF2[0:NofNodes])
    
    G = FB.ConstructMatchingModel(MG1, MG2, 'cmu', True)
    G2 = FB.ConstructMatchingModel(MG1, MG2, 'cmu', False)
    Gvis = FB.ConstructMatchingModel(MG1, MG2, 'cmu', True)
    G.SetVerbose(False)
    
    res1 = FB.BaBSolver(G, 100, 10, 0.005, False)
    res2 = FB.BaBSolver(G2, 600, 10, 0.005, False)


    resBag = eng.runBcagm(nargout=3)
    resBagMP = eng.runBcagmQuad1(1,nargout=3)
    resBagIPFP = eng.runBcagmQuad1(2,nargout=3)
    resHGM = eng.runHGM(nargout=3)
    resRRWHM = eng.runRRWHM(nargout=3)
    resTM = eng.runTensorMatching(nargout=3)
    
    
    
    start_time = time.time()
    ResForBca = sio.loadmat('Temp.mat')
    X0 = np.zeros(NofNodes)
    X0Vec = res1.Decode
    for i in xrange(NofNodes):
        X0[i] = X0Vec[i]
    ResForBca['X0'] = X0
    sio.savemat('Temp.mat', ResForBca)
    resOursBCA = eng.runBcagm(nargout=3)
    time_dur = time.time() - start_time
    
    cDecode = FB.intArray(NofNodes)
    #print(resOursBCA[1][0])
    for i in range(NofNodes):
        cDecode[i] = int(resOursBCA[1][0][i])
    if(res1.Value < Gvis.ComputeObj(cDecode)):
        Accuracy[8][ImageI] = ComputeAccurancy(resOursBCA[1][0], gTruth, NofNodes)
        Obj[8][ImageI] = Gvis.ComputeObj(cDecode)
    else:
        Accuracy[8][ImageI] = ComputeAccurancy(res1.Decode, gTruth, NofNodes)
        Obj[8][ImageI] = res1.Value


    
    Rtime[8][ImageI] = time_dur + res1.Time
    
    
    Accuracy[0][ImageI] = ComputeAccurancy(res1.Decode, gTruth, NofNodes)
    Rtime[0][ImageI] = res1.Time
    Obj[0][ImageI] = res1.Value
    
    Accuracy[7][ImageI] = ComputeAccurancy(res2.Decode, gTruth, NofNodes)
    Rtime[7][ImageI] = res2.Time
    Obj[7][ImageI] = res2.Value

    Accuracy[1][ImageI] = ComputeAccurancy(resBag[1][0], gTruth, NofNodes)
    Rtime[1][ImageI] = resBag[0]
    cDecode = FB.intArray(NofNodes)
    for i in range(NofNodes):
        cDecode[i] = int(resBag[1][0][i])
    Obj[1][ImageI] = Gvis.ComputeObj(cDecode)

    Accuracy[2][ImageI] = ComputeAccurancy(resBagMP[1][0], gTruth, NofNodes)
    Rtime[2][ImageI] = resBagMP[0]
    for i in range(NofNodes):
        cDecode[i] = int(resBagMP[1][0][i])
    Obj[2][ImageI] = Gvis.ComputeObj(cDecode)
    
    Accuracy[3][ImageI] = ComputeAccurancy(resBagIPFP[1][0], gTruth, NofNodes)
    Rtime[3][ImageI] = resBagIPFP[0]
    for i in range(NofNodes):
        cDecode[i] = int(resBagIPFP[1][0][i])
    Obj[3][ImageI] = Gvis.ComputeObj(cDecode)
    
    
    Accuracy[4][ImageI] = ComputeAccurancy(resHGM[1][0], gTruth, NofNodes)
    Rtime[4][ImageI] = resHGM[0]
    for i in range(NofNodes):
        cDecode[i] = int(resHGM[1][0][i])
    Obj[4][ImageI] = Gvis.ComputeObj(cDecode)
    
    
    Accuracy[5][ImageI] = ComputeAccurancy(resRRWHM[1][0], gTruth, NofNodes)
    Rtime[5][ImageI] = resRRWHM[0]
    for i in range(NofNodes):
        cDecode[i] = int(resRRWHM[1][0][i])
    Obj[5][ImageI] = Gvis.ComputeObj(cDecode)

    Accuracy[6][ImageI] = ComputeAccurancy(resTM[1][0], gTruth, NofNodes)
    Rtime[6][ImageI] = resTM[0]
    for i in range(NofNodes):
        cDecode[i] = int(resTM[1][0][i])
    Obj[6][ImageI] = Gvis.ComputeObj(cDecode)

    MaxObj = np.max(Obj[:,ImageI])
    Obj[:,ImageI] /= MaxObj

    for ai in xrange(NofAlgorithms):
        print('%s Accuracy %f Running Time %f Obj %f' %(AlgorithmNames[ai], 
                                                         Accuracy[ai][ImageI],
                                                        Rtime[ai][ImageI],
                                                        Obj[ai][ImageI]))
    print(' Finished Frame: %d' % (ImageI) )
#Todo Ours-BCA
#for ai in xrange(NofAlgorithms):
#    MeanAcc[NofOus][ai] = np.mean(Accuracy[ai])
#    MeanRtime[NofOus][ai] = np.mean(Rtime[ai])
#    MeanObj[NofOus][ai] = np.mean(Obj[ai])
#    print('%s Accuracy %f Running Time %f Obj %f' %(AlgorithmNames[ai], 
#                                                    np.mean(Accuracy[ai]),
#                                                    np.mean(Rtime[ai]),
#                                                    np.mean(Obj[ai])))


