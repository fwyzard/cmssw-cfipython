import FWCore.ParameterSet.Config as cms

hltRHemisphere = cms.EDFilter('HLTRHemisphere',
  inputTag = cms.InputTag('hltMCJetCorJetIcone5HF07'),
  minJetPt = cms.double(30),
  maxEta = cms.double(3),
  maxNJ = cms.int32(7),
  acceptNJ = cms.bool(True)
)
