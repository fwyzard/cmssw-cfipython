import FWCore.ParameterSet.Config as cms

hltJetCollectionsForLeptonPlusJets = cms.EDProducer('HLTJetCollectionsForLeptonPlusJets',
  HltLeptonTag = cms.InputTag('triggerFilterObjectWithRefs'),
  SourceJetTag = cms.InputTag('caloJetCollection'),
  minDeltaR = cms.double(0.5)
)
