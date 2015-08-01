import FWCore.ParameterSet.Config as cms

hltFatJetMassFilterRecoPFJet = cms.EDFilter('HLTFatPFJetMassFilter',
  saveTags = cms.bool(False),
  inputJetTag = cms.InputTag('hltCollection'),
  minMass = cms.double(0),
  fatJetDeltaR = cms.double(1.1),
  maxDeltaEta = cms.double(10),
  maxJetEta = cms.double(3),
  minJetPt = cms.double(30),
  triggerType = cms.int32(85)
)
