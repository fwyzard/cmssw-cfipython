import FWCore.ParameterSet.Config as cms

hltJetCollForElePlusJets = cms.EDProducer('HLTJetCollForElePlusJets',
  HltElectronTag = cms.InputTag('triggerFilterObjectWithRefs'),
  SourceJetTag = cms.InputTag('caloJetCollection'),
  MinJetPt = cms.double(30),
  MaxAbsJetEta = cms.double(2.6),
  MinNJets = cms.uint32(1),
  minDeltaR = cms.double(0.5),
  MinSoftJetPt = cms.double(25),
  MinDeltaEta = cms.double(-1)
)
