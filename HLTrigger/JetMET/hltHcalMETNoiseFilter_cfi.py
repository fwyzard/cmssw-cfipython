import FWCore.ParameterSet.Config as cms

hltHcalMETNoiseFilter = cms.EDFilter('HLTHcalMETNoiseFilter',
  HcalNoiseRBXCollection = cms.InputTag('hltHcalNoiseInfoProducer'),
  severity = cms.int32(1),
  maxNumRBXs = cms.int32(2),
  numRBXsToConsider = cms.int32(2),
  needEMFCoincidence = cms.bool(True),
  minRBXEnergy = cms.double(50),
  minRatio = cms.double(0.65),
  maxRatio = cms.double(0.98),
  minHPDHits = cms.int32(17),
  minRBXHits = cms.int32(999),
  minHPDNoOtherHits = cms.int32(10),
  minZeros = cms.int32(10),
  minHighEHitTime = cms.double(-9999),
  maxHighEHitTime = cms.double(9999),
  maxRBXEMF = cms.double(0.02),
  minRecHitE = cms.double(1.5),
  minLowHitE = cms.double(10),
  minHighHitE = cms.double(25)
)
