import FactorBP as FBP
import numpy as np
from GenerateTSP import GenerateEuclideanTSP, GenerateSymTSP, GenerateASymTSP


def GetSubtours(AssignMents):
    n = len(AssignMents)
    Visited = [False] * n
    cnt = 0;
    SubTours = []
    while True:
        current = Visited.index(False)
        thiscycle = [current]
        while True:
            Visited[current] = True
            t = AssignMents[current]
            if(Visited[t] == True):
                break
            else:
                current = t;
                thiscycle.append(t)
        SubTours.append(thiscycle)
        cnt = cnt + len(thiscycle)
        if(cnt == n):
            break
    return SubTours

if __name__ == '__main__':
    np.random.seed(123456)
   
    NofNodes = 5
    NofStates = FBP.intArray(NofNodes);
    for i in range(NofNodes):
        NofStates[i] = NofNodes
    G = FBP.CFactorGraph(NofNodes, NofStates)
    G.AddAuctionFactor();
    distMat = GenerateASymTSP(NofNodes)
    for i in range(NofNodes):
        thetai = distMat[i]
        thetaiD = FBP.doubleArray(NofNodes)
        for xi in range(NofNodes):
            thetaiD[xi] = -thetai[xi]
        G.AddNodeBelief(i,thetaiD)
    G.SetVerbose(True)
    G.SetMinDualDecrease(0.000001)
    G.Solve(10)
    res = G.GetDecode()
    DecodedL = [b for b in res];
    print(res)
    SubTours = GetSubtours(DecodedL)
    while(len(SubTours) > 1):
        for SubT in SubTours:
            Nodes = FBP.intArray(len(SubT))
            AssignMents = FBP.intArray(len(SubT))
            for ni in range(len(SubT)):
                Nodes[ni] = SubT[ni]
                AssignMents[ni] = SubT[(ni + 1) % len(SubT)]
            G.AddSubTourFactor(len(SubT), Nodes, AssignMents)

        G.ResetMax();
        G.Solve(100)
        GStore = G.StoreDual()
    

        res1 = G.GetDecode()
        res = FBP.BaBSolver(G, 600, 5, 0.005, True);
        SubTours = GetSubtours(res.Decode)
        G.ReStoreDual(GStore)
        #DecodedL1 = [b for b in res1]
        print(SubTours)
        print(res.Decode)
    #print(DecodedL1)
    #print(res)
