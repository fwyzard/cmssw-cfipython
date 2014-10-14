import FWCore.ParameterSet.Config as cms

matchGenHFHadron = cms.EDProducer('GenHFHadronMatcher',
  genJets = cms.InputTag('ak5GenJets', '', 'HLT'),
  noBBbarResonances = cms.bool(True),
  onlyJetClusteredHadrons = cms.bool(False),
  flavour = cms.int32(5)
)
