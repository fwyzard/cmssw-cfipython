import FWCore.ParameterSet.Config as cms

hltJetCollectionsForElePlusJets = cms.EDProducer('HLTJetCollectionsForElePlusJets',
  HltElectronTag = cms.InputTag('triggerFilterObjectWithRefs'),
  SourceJetTag = cms.InputTag('caloJetCollection'),
  minDeltaR = cms.double(0.5)
)
