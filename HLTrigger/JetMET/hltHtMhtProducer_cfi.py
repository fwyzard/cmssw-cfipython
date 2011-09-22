import FWCore.ParameterSet.Config as cms

hltHtMhtProducer = cms.EDProducer('HLTHtMhtProducer',
  jetsLabel = cms.InputTag('hltCaloJetCorrected'),
  minNJetHt = cms.int32(0),
  minNJetMht = cms.int32(0),
  minPtJetHt = cms.double(40),
  minPtJetMht = cms.double(30),
  maxEtaJetHt = cms.double(3),
  maxEtaJetMht = cms.double(999),
  useTracks = cms.bool(False),
  tracksLabel = cms.InputTag('hltL3Muons')
)
